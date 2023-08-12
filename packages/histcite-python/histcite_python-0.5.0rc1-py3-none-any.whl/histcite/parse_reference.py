import re
from typing import Optional, Literal
from dataclasses import dataclass, asdict


@dataclass
class WosField:
    First_AU: Optional[str]
    PY: Optional[str] = None
    J9: Optional[str] = None
    VL: Optional[str] = None
    BP: Optional[str] = None
    DI: Optional[str] = None
    doc_index: Optional[int] = None


@dataclass
class CssciField:
    First_AU: Optional[str]
    TI: Optional[str] = None
    SO: Optional[str] = None
    PY: Optional[str] = None
    VL: Optional[str] = None
    doc_index: Optional[int] = None


@dataclass
class ScopusField:
    First_AU: Optional[str]
    TI: Optional[str] = None
    SO: Optional[str] = None
    VL: Optional[str] = None
    IS: Optional[str] = None
    BP: Optional[str] = None
    EP: Optional[str] = None
    PY: Optional[str] = None
    doc_index: Optional[int] = None


class ParseReference:
    def __init__(self, doc_index):
        self.doc_index = doc_index

    def _parse_wos_ref(self, cr: str) -> Optional[dict[str, Optional[str]]]:
        # refs contain another language except english or AU is anonymous
        if re.search(r'[\[\]]', cr):
            return None
        
        # don't parse patent
        if 'Patent No.' in cr:
            return None
        
        AU, PY, J9, VL, BP, DI = None, None, None, None, None, None
        
        if ', DOI ' in cr:
            # contain only one DOI
            if 'DOI [' not in cr:
                DI_match = re.search(r'DOI (10.*)$', cr)
                DI = DI_match[1] if DI_match else None
            # contain two or more DOI
            else:
                DI_match = re.search(r'DOI \[(.*)\]', cr)
                DI = DI_match[1] if DI_match else None
            cr = re.sub(r', DOI.*', '', cr)
        
        BP_match = re.search(r', [Pp]([A-Za-z]?\d+)$', cr)
        if BP_match:
            BP = BP_match[1]
            cr = re.sub(r', [Pp][A-Za-z]?\d+', '', cr)

        cr = re.sub(r'[,\.] PROCEEDINGS(?=, )', '', cr, flags=re.I)
        if VL_match := re.search(r', V([\d-]+)$', cr):
            VL = VL_match[1]
            sub_pattern = r', V[\d-]+$'
        
        elif re.search(r', VOL[s\.]? ', cr, re.I):
            VL_match = re.search(r', VOL[s\.]? ([\w\- ]+)$', cr, re.I)
            VL = VL_match[1] if VL_match else None
            sub_pattern = r', V[Oo][Ll].*'
        
        elif VL_match := re.search(r'(?<=[A-Z\.]), V([\w\. ]+)$', cr):
            VL = VL_match[1]
            sub_pattern = r'(?<=[A-Z\.]), V[\w\. ]+$'

        else:
            sub_pattern = None
        
        if sub_pattern:
            cr = re.sub(sub_pattern, '', cr)
        
        dot_count = cr.count(', ')
        if dot_count == 2:
            AU, PY, J9 = cr.split(', ')
        elif dot_count > 2:
            PY_pattern = r', (\d{4}), '
            if re.search(PY_pattern, cr):
                AU, PY, J9 = re.split(PY_pattern, cr, 1)
        else:
            return None
        
        if DI:
            DI = DI.lower()
            if len(re.findall(', ', DI)) == 1:
                try:
                    DI1, DI2 = DI.replace('doi ', '').split(', ')
                except:
                    return None
                if DI1 == DI2:
                    DI = DI1
                else:
                    DI = None
        
        if PY and not re.match(r'^\d{4}$', PY):
            PY = None
        return asdict(WosField(AU, PY, J9, VL, BP, DI, self.doc_index))

    def _parse_cssci_ref(self, cr: str) -> Optional[dict[str, Optional[str]]]:
        """only parse chinese reference"""
        dot_pattern = re.compile(r'(?<!\d)\.(?!\d)|(?<=\d)\.(?!\d)|(?<!\d)\.(?=\d)|(?<=\d{4})\.(?=\d)|(?<=\d)\.(?=\d{4})')
        
        if re.search(r'[\u4e00-\u9fa5]', cr):
            dot_count = len(dot_pattern.findall(cr))

            # 中间部分双圆点
            if re.search(r'[^\d]\.{2,}', cr):
                return None

            # 学位论文
            elif ":学位论文." in cr:
                try:
                    _, AU, TI, other = cr.split('.')
                except:
                    return None
                else:
                    TI = TI.replace(':学位论文', '')
                    SO, PY = other.split(',')
                    PY = PY.split(':')[0]
                    result =  CssciField(AU, TI, SO, PY, None)
                    
            # 国家标准
            elif 'GB/T' in cr:
                if cr[-3:] == "出版社":
                    _, AU, other = cr.split('.', 2)
                    TI, SO = other.rsplit('.', 1)
                    result =  CssciField(AU, TI, SO, None, None)
                else:
                    _, AU, TI = cr.split('.', 2)
                    result =  CssciField(AU, TI, None, None, None)

            # 规范
            elif re.search(r':DB\d{2}/T', cr):
                _, AU, other = cr.split('.', 2)
                TI, PY = other.rsplit('.', 1)
                result =  CssciField(AU, TI, None, PY, None)

            # 报刊
            elif re.search(r'\.\d{1,2}\.\d{1,2}(?:\(|$)', cr):
                try:
                    _, AU, TI, SO, other = re.split(dot_pattern, cr, 4)
                except:
                    return None
                else:
                    result = CssciField(AU, TI, SO, None, None)

            # 专利1
            elif re.search(r'\.CN\d{9}[A-Z]$', cr):
                TI = cr.split('.', 1)[1]
                result =  CssciField(None, TI, None, None, None)
            # 专利2
            elif re.search(r'^\d+\.一种', cr):
                date_pattern = re.compile(r'\d{4}\-\d{1,2}\-\d{1,2}')
                TI = cr.split('.', 1)[1]
                date = date_pattern.search(cr)
                if date:
                    PY = date[0].split('-')[0]
                else:
                    PY = None
                TI = date_pattern.sub('', TI).strip('.()')
                result = CssciField(None, TI, None, PY, None)

            # 网络文献
            elif re.search(r'\.\d{4}$', cr):
                if dot_count == 3:
                    _, AU, TI, PY = re.split(dot_pattern, cr)
                elif dot_count == 4:
                    _, AU, TI, SO, PY = re.split(dot_pattern, cr)
                else:
                    return None
                result = CssciField(AU, TI, None, PY, None)

            # 期刊1
            elif dot_count == 5:
                _, AU, TI, SO, PY, VL = re.split(dot_pattern, cr)
                result = CssciField(AU, TI, SO, PY, VL)
            # 期刊2
            elif dot_count == 4:
                _, AU, TI, SO, _ = re.split(dot_pattern, cr)
                result = CssciField(AU, TI, SO, None, None)

            # 专著
            elif dot_count == 3:
                _, AU, TI, SO = re.split(dot_pattern, cr)
                result = CssciField(AU, TI, SO, None, None)

            # 其他
            elif dot_count == 2:
                _, AU, TI = re.split(dot_pattern, cr)
                result = CssciField(AU, TI, None, None, None)

            elif dot_count == 1:
                _, TI = re.split(dot_pattern, cr)
                result = CssciField(None, TI, None, None, None)
            else:
                return None
            
            result.doc_index = self.doc_index
            return asdict(result)

    def _parse_scopus_ref(self, cr: str) -> Optional[dict[str, Optional[str]]]:
        if re.search(r'^[^A-Z\*\']', cr):
            return None
        
        if re.search(r'[\[\]]', cr):
            return None
        
        if cr.count(', ') < 2:
            return None

        # Publication year
        PY_match = re.search(r', \((\d{4})\)$', cr)
        if PY_match:
            PY = PY_match[1]
            cr = cr.rsplit(', ', 1)[0]
        else:
            return None
        
        First_AU, TI, SO, VL, IS, BP, EP = None, None, None, None, None, None, None
        
        # remove version info
        # IBM SPSS Statistics for Windows, Version 22.0, (2013)
        cr = re.sub(r', version [\d\.]+(?=,)', '', cr, flags=re.I)

        # remove doi info
        # Zietlow A.L., Schluter M.K., Nonnenmacher N., Muller M., Reck C., Maternal self-confidence postpartum and at pre-school age: the role of depression, anxiety disorders and maternal attachment insecurity. Maternal and Child Health, doi:10.1007/s10995-014-1431-1, (2014)
        # Comparing family accommodation in pediatric obsessive–compulsive disorder, anxiety disorders, and non-anxious children. Depress Anxiety, doi:10.1002/da.22251
        cr = re.sub(r', doi:.*(?=,|$)', '', cr, flags=re.I)
        
        # remove retrieval info
        # Antecedents and consequences of perceived control during the transition to adulthood, Retrieved from ProQuest dissertations & theses, (2008)
        cr = re.sub(r'[\.,] Retrieved.*(?=,)', '', cr, flags=re.I)
        
        # NCS-R lifetime prevalence estimates, Available from:, (2011); 
        cr = re.sub(r', Available from:(?=,)', '' , cr, flags=re.I)

        # Page number
        # Davis M., The role of the amygdala in conditioned and unconditioned fear and anxiety, The amygdala: A functional analysis (pp. 213-287)
        # Conflict resolution: A cognitive perspective. In H. Max (Ed.), Negotiation, decision making and conflict management (pp, 116–134)
        if PP_match := re.search(r'(?:, | \()[Pp]{2}[\.,] ([\w\-]+)\)?', cr):
            PP = PP_match[1]
            try:
                BP, EP = re.split(r'-', PP, 1)
            except:
                BP, EP = None, None
            cr = re.sub(r'(?:, | \()[Pp]{2}.*', '', cr)
        
        # Volume and Issue
        # Flannery-Schroeder E.C., Group versus individual cognitive behavioural treatment for anxiety-disordered children, Dissertation Abstracts International, 58, 10B
        # Yiend J., Mathews A., Anxiety and attention to threatening pictures, The Quarterly Journal of Experimental Psychology, 54 A, 3
        if VL_IS_match := re.search(r', (\d+\s?[A-Za-z]*, [\w\s\-\.\–]+)$', cr):
            VL, IS = VL_IS_match[1].split(', ')
            cr = cr.rsplit(', ', 2)[0]
        
        # Tiller J.W., Bouwer C., Behnke K., Moclobemide and fluoxetine for panic disorder, Eur Arch Psychiatry Clin Neurosci, 249, SUPPL. 1, (1999);
        elif IS_match := re.search(r', ([\w-]* ?suppl\.? ?[\w-]*)$', cr, re.I):
            IS = IS_match[1]
            cr = cr.rsplit(', ', 1)[0]
        
        # Mishra V., Baines M., Wenstone R., Shenkin A., Markers of oxidative damage, antioxidant status and clinical outcome in critically ill patients, Ann Clin Biochem, 42, PART. 4
        # Holmes A.P., Friston K.J., Generalisability, random effects & population inference, NeuroImage, 7, PART II
        elif IS_match := re.search(r', (\d* ?PART\.? [A-Z\d]+)$', cr, re.I):
            IS = IS_match[1]
            cr = cr.rsplit(', ', 1)[0]
        
        # Depression Guideline Panel: Vol. 2, treatment of major depression, Clinical Practice Guideline, No. 5, (1993)
        elif IS_match := re.search(r', ([Nn]o\. \d+)$', cr):
            IS = IS_match[1]
            cr = cr.rsplit(', ', 1)[0]

        if VL_match := re.search(r', (\d+)$', cr):
            VL = VL_match[1]
            cr = cr.rsplit(', ', 1)[0]
        
        # Robinson C.C., Mandleco B., Frost Olsen S., Hart C.H., The parenting styles and dimensions questionnaire (PSDQ), Handbook of family measurement techniques, Vol. 2: Instruments and index, (2001)
        elif VL_match := re.search(r', ([Vv]ol\. [\w\s\.:]+)$', cr):
            VL = VL_match[1]
            cr = cr.rsplit(', ', 1)[0]
        
        # Author
        full_name_pattern = r'^(?:[a-zA-Z][a-zA-Z\-\.\']*\s)+[A-Z][a-zA-Z\-\.\']*(, |$)'
        if re.search(r'Et al\.', cr, flags=re.I):
            First_AU = cr.split(', ')[0]
            cr = re.sub(r'^.*Et al\.,?\s?', '', cr, flags=re.I)

        elif '., ' in cr:
            AU = cr.rsplit('., ', 1)[0]
            if ',' in AU:
                First_AU = AU.split(', ')[0]
            else:
                First_AU = AU + '.'
            cr = cr.replace(f'{AU}., ', '')

        elif re.search(r'^(?:[A-Z][a-zA-Z]*\s)+[A-Z][a-zA-Z]*(?=, )', cr):
            First_AU = cr.split(', ',1)[0]
            cr = cr.replace(f'{First_AU}, ', '')

        elif re.search(r'^[A-Z-]+, (?=[A-Z])', cr):
            First_AU = cr.split(', ',1)[0]
            cr = cr.replace(f'{First_AU}, ', '')
        
        elif re.search(full_name_pattern, cr):
            First_AU = re.split(', ', cr, 1)[0]
            while re.search(full_name_pattern, cr):
                cr = re.sub(full_name_pattern, '', cr, 1)

        else:
            return None

        # Title and Source
        if cr != '':
            comma_pattern = r', (?![^\[]*\]|[^(]*\))'
            comma_count = len(re.findall(comma_pattern, cr))
            if comma_count == 0:
                TI = cr
            elif comma_count == 1:
                TI, SO = re.split(comma_pattern, cr)
            else:
                # conference ref
                if re.search(r'[Cc]onference|Conf\.|[Pp]roceeding|Proc\.|[Cc]ommittee|[Ss]ymposium|[Cc]onvention|[Cc]ongress', cr):
                    TI, SO = cr.split(', ', 1)
                
                # match source
                elif SO_match := re.search(r', ([A-Z\d][\w\s\.\-&:]+)$',cr):
                    SO = SO_match[1]
                    TI = cr.replace(f', {SO}', '')
                
                # match title
                elif TI_match:= re.search(r'^(([^\.\s]+ ){3,}[^\.\sA-Z]+), [A-Z]',cr):
                    TI = TI_match[1]
                    SO = cr.replace(f'{TI}, ', '')

                elif re.search(r'^[A-Z][^A-Z]+$',cr):
                    TI = cr
                
                else:
                    return None
        return asdict(ScopusField(First_AU, TI, SO, VL, IS, BP, EP, PY, self.doc_index))

    def parse_cr_cell(self, cr_cell: str, source_type: Literal['wos', 'cssci', 'scopus']) -> Optional[list[dict[str, Optional[str]]]]:
        sep = '; '
        try:
            cr_list = re.split(sep, cr_cell)
        except:
            return None
        
        parsed_cr_list: list[Optional[dict[str, Optional[str]]]]
        if source_type == "wos":
            parsed_cr_list = [self._parse_wos_ref(i) for i in cr_list]
        elif source_type == "cssci":
            parsed_cr_list = [self._parse_cssci_ref(i) for i in cr_list]
        elif source_type == "scopus":
            parsed_cr_list = [self._parse_scopus_ref(i) for i in cr_list]
        else:
            raise ValueError('Invalid source type')
        parse_cr_list = [cr for cr in parsed_cr_list if cr is not None]
        return parse_cr_list