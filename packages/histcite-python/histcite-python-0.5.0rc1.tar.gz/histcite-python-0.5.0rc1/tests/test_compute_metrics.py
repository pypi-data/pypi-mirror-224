import pytest
import pandas as pd
from typing import Literal
from histcite.compute_metrics import ComputeMetrics


@pytest.mark.skip(reason='This is a function factory')
def test_statistics(docs_df_path: str, refs_df_path: str, citation_relationship_path: str, source_type: Literal['wos','cssci','scopus']):
    def new_func():
        docs_df = pd.read_csv(docs_df_path, dtype_backend='pyarrow')
        refs_df = pd.read_csv(refs_df_path, dtype_backend='pyarrow')
        citation_relationship = pd.read_csv(citation_relationship_path, dtype_backend='pyarrow')
        cm = ComputeMetrics(docs_df, citation_relationship, refs_df, source_type)
        return cm._generate_keywords_df()
    return new_func

def test_wos_statistics():
    docs_df_path = 'tests/wos_docs_df.csv'
    refs_df_path = 'tests/wos_refs_df.csv'
    citation_relationship_path = 'tests/wos_citation_relationship.csv'
    keywords_df = test_statistics(docs_df_path, refs_df_path, citation_relationship_path, 'wos')()
    assert isinstance(keywords_df.index[0], str)

def test_cssci_statistics():
    docs_df_path = 'tests/cssci_docs_df.csv'
    refs_df_path = 'tests/cssci_refs_df.csv'
    citation_relationship_path = 'tests/cssci_citation_relationship.csv'
    keywords_df = test_statistics(docs_df_path, refs_df_path, citation_relationship_path, 'cssci')()
    assert isinstance(keywords_df.index[0], str)

def test_scopus_statistics():
    docs_df_path = 'tests/scopus_docs_df.csv'
    refs_df_path = 'tests/scopus_refs_df.csv'
    citation_relationship_path = 'tests/scopus_citation_relationship.csv'
    keywords_df = test_statistics(docs_df_path, refs_df_path, citation_relationship_path, 'scopus')()
    assert isinstance(keywords_df.index[0], str)