import os
import re
import pandas as pd
from typing import Literal, Callable


class ReadWosFile:
    @staticmethod
    def _extract_first_author(au_field: pd.Series) -> pd.Series:
        return au_field.str.split(pat=';',n=1,expand=True)[0].str.replace(',','')

    @staticmethod
    def _read_wos_file(file_path: str) -> pd.DataFrame:
        use_cols = ['AU', 'TI', 'SO', 'DT', 'CR', 'DE', 'C3',
                    'NR', 'TC', 'Z9', 'J9', 'PY', 'VL', 'BP', 'DI', 'UT']
        df = ReadGeneralFile._read_csv(file_path, use_cols, '\t')
        df.insert(1, 'First_AU', ReadWosFile._extract_first_author(df['AU']))
        df['source file'] = os.path.basename(file_path)
        return df


class ReadCssciFile:
    @staticmethod
    def _extract_org(org_cell: str) -> str:
        org_set = set(re.findall(r'](.*?)(?:/|$)', org_cell))
        org_list = [i.replace('.', '') for i in org_set]
        return '; '.join(org_list)
    
    @staticmethod
    def _read_cssci_file(file_path: str) -> pd.DataFrame:
        with open(file_path, 'r') as f:
            text = f.read()
        
        body_text = text.split('\n\n\n', 1)[1]
        contents = {}
        original_fields = ['来源篇名', '来源作者', '基    金', '期    刊', '机构名称', '第一作者', '年代卷期', '关 键 词', '参考文献']
        for field in original_fields:
            if field != '参考文献':
                field_pattern = f'【{field}】(.*?)\n'
                contents[field] = re.findall(field_pattern, body_text)
            else:
                field_pattern = '【参考文献】\n(.*?)\n?'+'-'*5
                contents[field] = re.findall(field_pattern, body_text, flags=re.S)
        
        df = pd.DataFrame.from_dict(contents)
        # 重命名列标签
        column_mapping = {
            '来源篇名': 'TI',
            '来源作者': 'AU',
            '基    金': 'FU',
            '期    刊': 'SO',
            '机构名称': 'C3',
            '第一作者': 'First_AU',
            '年代卷期': 'PY&VL&BP&EP', 
            '关 键 词': 'DE',
            '参考文献': 'CR'}
        df.rename(columns=column_mapping, inplace=True)

        df['AU'] = df['AU'].str.replace('/', '; ')
        df['DE'] = df['DE'].str.replace('/', '; ')
        df['PY'] = df['PY&VL&BP&EP'].str.extract(r'^(\d{4}),', expand=False)
        df['C3'] = df['C3'].apply(ReadCssciFile._extract_org)
        df['CR'] = df['CR'].str.replace('\n', '; ')
        df['NR'] = df['CR'].str.count('; ')
        df.insert(2, 'First_AU', df.pop('First_AU'))
        df['source file'] = os.path.basename(file_path)
        return df


class ReadScopusFile:
    @staticmethod
    def _read_scopus_file(file_path: str) -> pd.DataFrame:
        use_cols = ['Authors', 'Author full names', 'Title', 'Year', 'Source title', 'Volume', 'Issue',
                    'Page start', 'Page end', 'Cited by', 'DOI', 'Author Keywords', 'References', 'Document Type', 'EID']
        
        df = ReadGeneralFile._read_csv(file_path, use_cols)
        # 重命名列标签
        column_mapping = {
            'Authors': 'AU',
            'Title': 'TI',
            'Year': 'PY',
            'Source title': 'SO',
            'Volume': 'VL',
            'Issue': 'IS',
            'Page start': 'BP',
            'Page end': 'EP',
            'Cited by': 'TC',
            'DOI': 'DI',
            'Author Keywords': 'DE',
            'References': 'CR',
            'Document Type': 'DT',
            }
        df.rename(columns=column_mapping, inplace=True)
        
        df['NR'] = df['CR'].str.count('; ')
        df.insert(1, 'First_AU', df['AU'].str.split(pat=';', n=1, expand=True)[0])
        df['source file'] = os.path.basename(file_path)
        return df

class ReadGeneralFile:
    @staticmethod
    def _read_csv(file_path: str, use_cols: list[str], sep: str = ',') -> pd.DataFrame:
        try:
            df = pd.read_csv(
                file_path,
                sep=sep,
                header=0,
                on_bad_lines='skip',
                usecols=use_cols,
                dtype_backend="pyarrow")
            return df
        except ValueError:
            file_name = os.path.basename(file_path)
            raise ValueError(f'File {file_name} is not a valid csv file')

class ReadFile:
    def __init__(self, folder_path: str, source_type: Literal['wos', 'cssci', 'scopus']):
        self.folder_path = folder_path
        self.source_type = source_type

        # obtain valid file name list
        if source_type == 'wos':
            file_name_list = [i for i in os.listdir(folder_path) if i[:9] == 'savedrecs']
        elif source_type == 'cssci':
            file_name_list = [i for i in os.listdir(folder_path) if i[:3] == 'LY_']
        elif source_type == 'scopus':
            file_name_list = [i for i in os.listdir(folder_path) if i[:6] == 'scopus']
        else:
            raise ValueError('Invalid source type')
        file_name_list.sort()
        self.file_path_list = [os.path.join(folder_path, file_name) for file_name in file_name_list]

    def _concat_table(self, read_file_func: Callable[[str], pd.DataFrame]) -> pd.DataFrame:
        file_count = len(self.file_path_list)
        if file_count > 1:
            return pd.concat([read_file_func(file_path) for file_path in self.file_path_list], ignore_index=True, copy=False)
        elif file_count == 1:
            return read_file_func(self.file_path_list[0])
        else:
            raise FileNotFoundError('No valid file in the folder')

    def read_all(self) -> pd.DataFrame:
        """concat multi dataframe and drop duplicate rows"""
        if self.source_type == 'wos':
            docs_df = self._concat_table(ReadWosFile._read_wos_file)
        elif self.source_type == 'cssci':
            docs_df = self._concat_table(ReadCssciFile._read_cssci_file)
        elif self.source_type == 'scopus':
            docs_df = self._concat_table(ReadScopusFile._read_scopus_file)
        else:
            raise ValueError('Invalid source type')
        
        # drop duplicate rows
        original_num = docs_df.shape[0]
        if self.source_type == 'wos':
            check_cols = ['UT']
        elif self.source_type == 'cssci':
            check_cols = ['TI', 'First_AU']
        elif self.source_type == 'scopus':
            check_cols = ['EID']
        else:
            raise ValueError('Invalid source type')
        docs_df.drop_duplicates(subset=check_cols, ignore_index=True, inplace=True) 
        current_num = docs_df.shape[0]
        print(f'共读取 {original_num} 条数据，去重后剩余 {current_num} 条')
        docs_df.insert(0, 'doc_index', docs_df.index)
        return docs_df