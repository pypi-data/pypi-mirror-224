from src.fhir.smart.scopes import scopes

a = scopes('openid patient/Encounter.crud')
b = scopes('launch/patient patient/Encounter.uds')
c = scopes('patient/Encounter.u')
d = scopes()


def test_intersect():
    assert type(a.intersection(b)) is scopes and type(a & b) is scopes
    assert len(a.intersection(b)) == 2
    assert len(a.intersection(b).intersection(c)) == 1
    assert len(a.intersection(d)) == 0
    assert a.intersection(c) == scopes('patient/Encounter.u')
    assert a.intersection(b) == a & b


def test_difference():
    assert type(a.difference(b)) is scopes and type(a - b) is scopes
    assert len(a.difference(b)) == 3
    assert len(a.difference(b).difference(c)) == 3
    assert len(a.difference(d)) == 5
    assert a.difference(c) == scopes('openid patient/Encounter.crd')
    assert a.difference(b) == a - b


def test_union():
    assert type(a.union(b)) is scopes and type(a | b) is scopes
    assert len(a.union(b)) == 7
    assert len(a.union(b).union(c)) == 7
    assert len(scopes() | d) == 0
    assert (a.union(b) ==
            scopes('openid launch/patient patient/Encounter.cruds'))


def test_symmetric_difference():
    assert type(a.symmetric_difference(b)) is scopes and type(a ^ b) is scopes
    assert len(a.symmetric_difference(b)) == 5
    assert a ^ b == scopes('openid launch/patient patient/Encounter.crs')
    assert a ^ d == a


def test_symmetric_difference_update():
    _a = a.copy()
    _a.symmetric_difference_update(b)
    assert type(_a) is scopes
    assert _a == a.symmetric_difference(b)
    __a = a.copy()
    __a ^= b
    assert _a == __a


def test_difference_update():
    _a = a.copy()
    _a.difference_update(b)
    assert type(_a) is scopes
    assert _a == a.difference(b)
    __a = a.copy()
    __a -= b
    assert _a == __a


def test_intersection_update():
    _a = a.copy()
    _a.intersection_update(b)
    assert type(_a) is scopes
    assert _a == a.intersection(b)
    __a = a.copy()
    __a &= b
    assert _a == __a
