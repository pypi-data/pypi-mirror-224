import pytest
import pandas as pd
from typing import Literal
from histcite.network_graph import GraphViz


@pytest.mark.skip(reason='This is a function factory')
def test_graph(docs_df_path: str, citation_relationship_path: str, source_type: Literal['wos','cssci','scopus']):
    def new_func():
        docs_df = pd.read_csv(docs_df_path, dtype_backend='pyarrow')
        citation_relationship = pd.read_csv(citation_relationship_path, dtype_backend='pyarrow')
        doc_indices = citation_relationship.sort_values('LCS', ascending=False).index[:10].tolist()
        G = GraphViz(docs_df, citation_relationship, source_type)
        graph_dot_file = G.generate_dot_file(doc_indices)
        return graph_dot_file
    return new_func

def test_wos_graph():
    docs_df_path = 'tests/wos_docs_df.csv'
    citation_relationship_path = 'tests/wos_citation_relationship.csv'
    graph_dot_file = test_graph(docs_df_path, citation_relationship_path, 'wos')()
    assert graph_dot_file[:7] == 'digraph'

def test_cssci_graph():
    docs_df_path = 'tests/cssci_docs_df.csv'
    citation_relationship_path = 'tests/cssci_citation_relationship.csv'
    graph_dot_file = test_graph(docs_df_path, citation_relationship_path, 'cssci')()
    assert graph_dot_file[:7] == 'digraph'

def test_scopus_graph():
    docs_df_path = 'tests/scopus_docs_df.csv'
    citation_relationship_path = 'tests/scopus_citation_relationship.csv'
    graph_dot_file = test_graph(docs_df_path, citation_relationship_path, 'scopus')()
    assert graph_dot_file[:7] == 'digraph'