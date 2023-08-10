import pytest

from src.fhir.smart.scopes import scopes


def test_discard():
    a = scopes('launch system/Medication.rs')
    assert len(a) == 3
    a.discard('launch')
    a.discard('unrelated')
    assert len(a) == 2
    a.discard('system/Medication.rs')
    assert len(a) == 0


def test_remove():
    a = scopes('launch user/Medication.cruds')
    a.remove('launch')
    assert len(a) == 5
    with pytest.raises(KeyError):
        a.remove('unlrelated')
    assert len(a) == 5
    a.remove('user/Medication.cru')
    assert len(a) == 2


def test_pop():
    a = scopes('launch user/Medication.cruds')
    b = a.copy()
    r = a.pop()
    assert len(a) == 5 and r not in a and r in b


def test_clear():
    a = scopes('launch user/Medication.cruds')
    a.clear()
    assert len(a) == 0
    b = scopes()
    b.clear()
    assert len(b) == 0
