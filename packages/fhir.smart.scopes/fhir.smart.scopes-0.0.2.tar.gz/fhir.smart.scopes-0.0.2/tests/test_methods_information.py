from src.fhir.smart.scopes import scopes, ALL_RESOUCES


def test_len():
    assert len(scopes()) == 0
    assert len(scopes('launch')) == 1
    assert len(scopes('patient/Observation.cruds')) == 5
    assert len(scopes('patient/*.cruds')) == 5*len(ALL_RESOUCES)


def test_str():
    assert str(scopes('launch')) == 'launch'

    assert 'launch/patient' in str(scopes('launch launch/patient')) and \
           'launch' in str(scopes('launch launch/patient'))
    s = scopes('patient/*.cruds')
    assert len(s) == 5*len(ALL_RESOUCES)
    assert str(s) == 'patient/*.cruds'

    s = scopes('system/Medication.rs')
    assert len(s) == 2
    assert str(s) == 'system/Medication.rs'

    s = scopes('user/*.r')
    assert len(s) == len(ALL_RESOUCES)
    assert str(s) == 'user/*.r'
    s.remove('user/Medication.r')
    assert len(s) == len(ALL_RESOUCES) - 1
    assert len(str(s)) > len('user/*.r')


def test_in():
    assert 'launch' in scopes('launch')
    assert ('patient/Observation.r' in
            scopes('patient/Observation.cruds'))
    assert ('patient/Observation.d' not in
            scopes('patient/Observation.crus'))
    assert ('patient/Observation.r' in
            scopes('patient/Observation.crus launch offline_access'))
    assert ('patient/Observation.r' not in
            scopes('patient/Observation.us launch offline_access'))
    assert ('patient/Observation.u' in
            scopes('patient/Observation.crus launch offline_access'))
    assert ('patient/Other.r' not in
            scopes('patient/Observation.crus launch offline_access'))
    assert ('patient/Observation.rs' in
            scopes('patient/Observation.cruds'))


def test_not_in():
    assert 'launch/patient' not in scopes('launch')
    assert 'patient/Encounter.r' not in scopes('patient/Observation.crus')
    assert 'patient/Other.r' not in scopes('patient/Observation.crus')
    assert 'patient/Observation.us' not in scopes('patient/Observation.cr')
    assert 'patient/Observation.us' not in scopes('patient/Observation.cru')


def test_issuperset():
    assert scopes('launch').issuperset(scopes('launch'))
    assert scopes('launch patient/Encounter.r').issuperset(scopes('launch'))
    assert not scopes('patient/Encounter.r').issuperset(scopes('launch'))
    assert not scopes('patient/Encounter.r') > scopes('launch')
    assert not scopes('launch') > scopes('launch')
    assert scopes('launch patient/Encounter.r') > scopes('launch')


def test_issubset():
    assert scopes('launch').issubset(scopes('launch'))
    assert scopes('launch').issubset(scopes('launch patient/Encounter.r'))
    assert not scopes('launch').issubset(scopes('patient/Encounter.cruds'))
    assert not scopes('launch') < scopes('launch')
    assert scopes('launch') <= scopes('launch')
    assert scopes('launch') < scopes('launch patient/Encounter.r')


def test_isdisjoint():
    assert scopes('launch').isdisjoint(scopes('patient/Encounter.r'))
    assert (scopes('patient/Observation.cruds')
            .isdisjoint(scopes('patient/Encounter.cruds')))
    assert not (scopes('patient/Encounter.cru launch/patient')
                .isdisjoint(scopes('patient/Encounter.cruds')))
