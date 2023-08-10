from __future__ import annotations
import itertools
import re

ALL_RESOUCES = {'Account', 'ActivityDefinition', 'ActorDefinition',
                'AdministrableProductDefinition', 'AdverseEvent',
                'AllergyIntolerance', 'Appointment', 'AppointmentResponse',
                'ArtifactAssessment', 'AuditEvent', 'Basic', 'Binary',
                'BiologicallyDerivedProduct',
                'BiologicallyDerivedProductDispense', 'BodyStructure',
                'Bundle', 'CapabilityStatement', 'CarePlan', 'CareTeam',
                'ChargeItem', 'ChargeItemDefinition', 'Citation', 'Claim',
                'ClaimResponse', 'ClinicalImpression', 'ClinicalUseDefinition',
                'CodeSystem', 'Communication', 'CommunicationRequest',
                'CompartmentDefinition', 'Composition', 'ConceptMap',
                'Condition', 'ConditionDefinition', 'Consent', 'Contract',
                'Coverage', 'CoverageEligibilityRequest',
                'CoverageEligibilityResponse', 'DetectedIssue', 'Device',
                'DeviceAssociation', 'DeviceDefinition', 'DeviceDispense',
                'DeviceMetric', 'DeviceRequest', 'DeviceUsage',
                'DiagnosticReport', 'DocumentReference', 'Encounter',
                'EncounterHistory', 'Endpoint', 'EnrollmentRequest',
                'EnrollmentResponse', 'EpisodeOfCare', 'EventDefinition',
                'Evidence', 'EvidenceReport', 'EvidenceVariable',
                'ExampleScenario', 'ExplanationOfBenefit',
                'FamilyMemberHistory', 'Flag', 'FormularyItem', 'GenomicStudy',
                'Goal', 'GraphDefinition', 'Group', 'GuidanceResponse',
                'HealthcareService', 'ImagingSelection', 'ImagingStudy',
                'Immunization', 'ImmunizationEvaluation',
                'ImmunizationRecommendation', 'ImplementationGuide',
                'Ingredient', 'InsurancePlan', 'InventoryItem',
                'InventoryReport', 'Invoice', 'Library', 'Linkage', 'List',
                'Location', 'ManufacturedItemDefinition', 'Measure',
                'MeasureReport', 'Medication', 'MedicationAdministration',
                'MedicationDispense', 'MedicationKnowledge',
                'MedicationRequest', 'MedicationStatement',
                'MedicinalProductDefinition', 'MessageDefinition',
                'MessageHeader', 'MolecularSequence', 'NamingSystem',
                'NutritionIntake', 'NutritionOrder', 'NutritionProduct',
                'Observation', 'ObservationDefinition', 'OperationDefinition',
                'OperationOutcome', 'Organization', 'OrganizationAffiliation',
                'PackagedProductDefinition', 'Parameters', 'Patient',
                'PaymentNotice', 'PaymentReconciliation', 'Permission',
                'Person', 'PlanDefinition', 'Practitioner', 'PractitionerRole',
                'Procedure', 'Provenance', 'Questionnaire',
                'QuestionnaireResponse', 'RegulatedAuthorization',
                'RelatedPerson', 'RequestOrchestration', 'Requirements',
                'ResearchStudy', 'ResearchSubject', 'RiskAssessment',
                'Schedule', 'SearchParameter', 'ServiceRequest', 'Slot',
                'Specimen', 'SpecimenDefinition', 'StructureDefinition',
                'StructureMap', 'Subscription', 'SubscriptionStatus',
                'SubscriptionTopic', 'Substance', 'SubstanceDefinition',
                'SubstanceNucleicAcid', 'SubstancePolymer', 'SubstanceProtein',
                'SubstanceReferenceInformation', 'SubstanceSourceMaterial',
                'SupplyDelivery', 'SupplyRequest', 'Task',
                'TerminologyCapabilities', 'TestPlan', 'TestReport',
                'TestScript', 'Transport', 'ValueSet', 'VerificationResult',
                'VisionPrescription'}
TOP_SCOPES = {'openid', 'fhirUser', 'launch', 'offline_access',
              'online_access'}
LAUNCH_SCOPES = {'launch/' + res.lower() for res in ALL_RESOUCES}
PERM_LVL = {'patient', 'user', 'system'}
RE_SCOPE_STR = r'^(patient|user|system)\/([^.]+).(c?r?u?d?s?)$'
scope_re = re.compile(RE_SCOPE_STR)


def _explode(scope_string):
    """
    Takes a scope string and returns the maximal set of scopes in their
    'atomic' form: [(level, resource, permission)], where level is
    ether patient, user, system or any launch or top level scope like openid;
    resource is the affected FHIR resource (None for launch and top level
    scopes); permission is one letter of "cruds"
    :param scope:
    :return:
    """
    for scope in scope_string.strip().split(' '):
        if not scope.startswith('launch/') and '/' in scope:
            m = scope_re.fullmatch(scope)
            if m is None:
                raise ValueError
            lvl, res, pem = m.groups()
            res = ALL_RESOUCES if res == '*' else [res]
            for r, p in itertools.product(res, pem):
                yield lvl, r, p
        else:
            yield scope, None, None


def _format(scope_tuple):
    lvl, res, pem = scope_tuple
    return lvl + (f'/{res}.{pem}' if res is not None else '')


def _sort_pem(pem):
    alpha = 'cruds'
    return ''.join(sorted(pem, key=lambda x: alpha.index(x)))


class scopes(set):
    """
    Represents SMART on FHIR scopes. It is used similarly to the Python
    built-in set type. Internally *atomic* scopes are stored,
    e.g. *patient/Observation.r* and *patient/Observation.u*, but you can
    initialize this type with the familiar SMART scopes string and also get
    a condensed version again by converting to string.

    Use the type constructor: scopes(), scopes(['openid', 'launch']),
    scopes('openid patient/Observation.cru')

    The definition of scopes is taken from the official SMART App Launch
    documentation v2.1.0, retrieved from
    `<https://build.fhir.org/ig/HL7/smart-app-launch/scopes-and-launch-context.html>`_.
    Note that experimental features of scopes, like the use of search
    parameters within scopes, is not supported, and scopes given containing
    this features will not be positively validated.
    """

    def __init__(self, values=None):
        super().__init__()
        if values is None or len(values) == 0:
            return
        if type(values) is str:
            list(map(self.add, values.split(' ')))
        elif type(values) is tuple:
            self._add_tuple(values)
        else:
            if type(values[0]) is str:
                list(map(self.add, values))
            else:
                self._add_tuples(values)

    def add(self, element):
        for lvl, res, pem in _explode(element):
            if (lvl not in TOP_SCOPES and lvl not in LAUNCH_SCOPES
                    and lvl not in PERM_LVL):
                raise ValueError
            elif res is not None and res not in ALL_RESOUCES:
                raise ValueError
            elif pem is not None and pem not in 'cruds':
                raise ValueError
            elif lvl == 'offline_access' and 'online_access' in self or \
                    lvl == 'online_access' and 'offline_access' in self:
                raise ValueError
            super().add((lvl, res, pem))

    def update(self, *other):
        for o in other:
            if type(o) is not scopes:
                raise ValueError
            self._add_tuples(o._get_tuples())

    def __ior__(self, other):
        self.update(other)
        return self

    def discard(self, element):
        for lvl, res, pem in _explode(element):
            super().discard((lvl, res, pem))

    def remove(self, element):
        for lvl, res, pem in _explode(element):
            super().remove((lvl, res, pem))

    def pop(self):
        return _format(super().pop())

    def __contains__(self, item):
        return all([super(scopes, self).__contains__(s)
                    for s in _explode(item)])

    def _add_tuples(self, tuples):
        list(map(super(scopes, self).add, tuples))

    def _get_tuples(self):
        yield from super(scopes, self).__iter__()

    def _add_tuple(self, _tuple):
        super(scopes, self).add(_tuple)

    def copy(self):
        return scopes(list(super().__iter__()))

    def __repr__(self):
        return self.__str__()

    def __str__(self):
        """ Returns a space seperated, compressed version of the scopes."""
        r = []
        s = set(super(scopes, self).__iter__())
        while s:
            lvl, res, pem = s.pop()
            s.add((lvl, res, pem))

            if lvl in TOP_SCOPES or lvl in LAUNCH_SCOPES:
                r.append(lvl)
                s.remove((lvl, res, pem))
            else:
                # is it a * resource?
                if set(_explode(f'{lvl}/*.{pem}')) <= s:
                    res = '*'

                # are there more permissions?
                for _pem in set('cruds') - {pem}:
                    if set(_explode(f'{lvl}/{res}.{_pem}')) <= s:
                        pem += _pem

                new_scope = f'{lvl}/{res}.{_sort_pem(pem)}'
                r.append(new_scope)
                s -= set(_explode(new_scope))

        return ' '.join(r)

    def intersection(self, *others):
        return scopes(list(super(scopes, self).intersection(*others)))

    def __and__(self, *others):
        return self.intersection(*others)

    def difference(self, *others):
        return scopes(list(super(scopes, self).difference(*others)))

    def __sub__(self, *others):
        return self.difference(*others)

    def union(self, *others):
        return scopes(list(super(scopes, self).union(*others)))

    def __or__(self, *others):
        return self.union(*others)

    def symmetric_difference(self, other):
        return scopes(list(super(scopes, self).symmetric_difference(other)))

    def __xor__(self, other):
        return self.symmetric_difference(other)

    def formatted_iter(self):
        for i in super().__iter__():
            yield _format(i)
