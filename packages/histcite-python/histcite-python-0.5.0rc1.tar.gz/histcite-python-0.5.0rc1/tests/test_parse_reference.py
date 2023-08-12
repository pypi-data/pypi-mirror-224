from histcite.parse_reference import ParseReference


def test_wos_cr():
    cr_cell = 'Bengio Y, 2001, ADV NEUR IN, V13, P932; Chang Y, 2003, IEEE INTERNATIONAL WORKSHOP ON ANALYSIS AND MODELING OF FACE AND GESTURES, P28; Chen Z., 2000, 6 INT C SPOK LANG PR; CORTES C, 1995, MACH LEARN, V20, P273, DOI 10.1007/BF00994018'
    parsed_refs_list = ParseReference(0).parse_cr_cell(cr_cell, 'wos')
    assert isinstance(parsed_refs_list, list)
    assert len(parsed_refs_list)==4
    assert parsed_refs_list[0]['First_AU']=='Bengio Y'
    assert parsed_refs_list[1]['PY']=='2003'
    assert parsed_refs_list[2]['J9']=='6 INT C SPOK LANG PR'
    assert parsed_refs_list[3]['BP']=='273'

def test_cssci_cr():
    cr = '1.严栋.基于物联网的智慧图书馆.图书馆学刊.2010.32(7)'
    parsed_ref = ParseReference(0)._parse_cssci_ref(cr)
    assert parsed_ref is not None
    assert parsed_ref['First_AU']=='严栋'
    assert parsed_ref['TI']=='基于物联网的智慧图书馆'
    assert parsed_ref['VL']=='32(7)'

def test_scopus_cr():
    cr = 'Negri E, Fumagalli L, Macchi M., A Review of the Roles of Digital Twin in CPS-based Production Systems, Procedia Manufacturing, 11, pp. 939-948, (2017)'
    parsed_ref = ParseReference(0)._parse_scopus_ref(cr)
    assert parsed_ref is not None
    assert parsed_ref['First_AU']=='Negri E'
    assert parsed_ref['SO']=='Procedia Manufacturing'
    assert parsed_ref['VL']=='11'
    assert parsed_ref['EP']=='948'
    assert parsed_ref['PY']=='2017'