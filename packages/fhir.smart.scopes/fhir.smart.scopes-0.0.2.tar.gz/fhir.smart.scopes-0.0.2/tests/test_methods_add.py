import pytest

from src.fhir.smart.scopes import scopes


def test_add():
    a = scopes()
    assert len(a) == 0
    a.add('launch')
    a.add('launch')
    assert len(a) == 1 and 'launch' in a
    a.add('system/Medication.rs')
    assert len(a) == 3
    with pytest.raises(ValueError):
        a.add('unrelated')


def test_update():
    a = scopes('launch system/Medication.rs')
    b = scopes('launch user/Medication.cruds')
    assert len(a) == 3 and len(b) == 6
    c = scopes()
    c.update(a, b)
    assert len(c) == 8
    with pytest.raises(ValueError):
        c.update('launch')
    c.update(scopes())
    assert len(c) == 8
    a |= b
    assert type(a) is scopes
    assert a == c
