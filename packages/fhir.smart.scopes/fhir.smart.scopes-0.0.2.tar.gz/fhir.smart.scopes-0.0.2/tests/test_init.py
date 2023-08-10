import pytest

from src.fhir.smart.scopes import scopes, ALL_RESOUCES


def test_construction():
    assert isinstance(scopes(), scopes)
    assert isinstance(scopes(), set)


def test_malformed_init():
    with pytest.raises(ValueError):
        scopes('thing/*.rs')  # faulty level
    with pytest.raises(ValueError):
        scopes('patient/Car.rs')  # non-existing resource
    with pytest.raises(ValueError):
        scopes('patient/*.x')  # faulty permission
    with pytest.raises(ValueError):
        scopes('patient/*.sr')  # permissions out of order
    with pytest.raises(ValueError):
        scopes('launch/Patient')  # missing permission
    with pytest.raises(ValueError):
        scopes('launch/car')  # unknown resource
    with pytest.raises(ValueError):
        s = scopes('offline_access')
        s.add('online_access')  # exclusive scopes
    with pytest.raises(ValueError):  # search params not supported
        scopes('system/Observation.rs?patient.birthdate=1990&patient=9')


def test_alternative_init():
    scopes([('patient', 'Observation', 'r')])
    scopes(['launch'])
    ...


def test_simple_init():
    assert len(scopes('patient/Observation.r')) == 1
    assert len(scopes('patient/Observation.rs')) == 2
    assert len(scopes('patient/Observation.cruds')) == 5
    assert len(scopes('patient/*.r')) == len(ALL_RESOUCES)
    assert len(scopes('launch/patient')) == 1
    assert len(scopes('launch/patient launch/patient')) == 1
