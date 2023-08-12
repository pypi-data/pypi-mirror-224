import pandas as pd
from typing import Optional


class RecognizeCommonReference:
    @staticmethod
    def recognize_refs(docs_df: pd.DataFrame, 
                       refs_df: pd.DataFrame, 
                       compare_cols: list[str], 
                       strict = True,
                       drop_duplicates = False):
        # drop rows with missing values
        if strict is True:
            docs_df = docs_df.dropna(subset = compare_cols)
            refs_df = refs_df.dropna(subset = compare_cols)
        
        if drop_duplicates is True:
            docs_df = docs_df.drop_duplicates(subset = compare_cols)
        
        docs_df = docs_df[['doc_index']+compare_cols]
        refs_df = refs_df[['doc_index', 'ref_index']+compare_cols]
        shared_df = pd.merge(refs_df, docs_df, how='left', on=compare_cols, suffixes = ('_x', '_y')).dropna(subset='doc_index_y')
        shared_df = shared_df.astype({'doc_index_y': 'int64'})
        cited_refs_series = shared_df.groupby('doc_index_x')['doc_index_y'].apply(list)
        cited_refs_series = cited_refs_series.apply(lambda x: sorted(x))
        local_refs_series = shared_df['ref_index'].reset_index(drop=True)
        return cited_refs_series, local_refs_series


class RecognizeReference():
    @staticmethod
    def recognize_wos_reference(docs_df: pd.DataFrame,
                                refs_df: pd.DataFrame):
        def merge_lists(list1: Optional[list[int]], list2: Optional[list[int]]):
            if isinstance(list1, list) and isinstance(list2, list):
                return list1 + list2
            else:
                if isinstance(list1, list):
                    return list1
                else:
                    return list2
        
        # DOI exists
        compare_cols_doi = ['DI']
        result_doi = RecognizeCommonReference.recognize_refs(docs_df, refs_df, compare_cols_doi)

        # DOI not exists
        compare_cols = ['First_AU', 'PY', 'J9', 'BP']
        result = RecognizeCommonReference.recognize_refs(docs_df[docs_df['DI'].isna()], refs_df[refs_df['DI'].isna()], compare_cols)
        cited_refs_series = result_doi[0].combine(result[0], merge_lists)
        local_refs_series = pd.concat([result_doi[1], result[1]])
        return cited_refs_series, local_refs_series
    
    @staticmethod
    def recognize_cssci_reference(docs_df: pd.DataFrame,
                                  refs_df: pd.DataFrame):
        compare_cols = ['First_AU', 'TI']
        return RecognizeCommonReference.recognize_refs(docs_df, refs_df, compare_cols)
    
    @staticmethod
    def recognize_scopus_reference(docs_df: pd.DataFrame,
                                   refs_df: pd.DataFrame):
        compare_cols = ['First_AU', 'TI']
        return RecognizeCommonReference.recognize_refs(docs_df, refs_df, compare_cols, drop_duplicates=True)