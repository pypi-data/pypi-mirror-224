from src.fhir.smart.scopes import scopes


def test_copy():
    assert len(scopes().copy()) == 0
    assert 'launch' in scopes('launch').copy()
    a = scopes('launch patient/Observation.cruds')
    b = a.copy()
    assert a == b
    b.add('patient/Encounter.rs')
    assert a < b and a != b
