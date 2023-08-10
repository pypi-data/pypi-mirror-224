# fhir.smart.scopes
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/fhir.smart.scopes)
![PyPI - License](https://img.shields.io/pypi/l/fhir.smart.scopes)


A simple wrapper around [SMART on FHIR scopes](http://hl7.org/fhir/smart-app-launch/STU2.1/scopes-and-launch-context.html#scopes-for-requesting-fhir-resources) to treat them as Python 
sets.

This implementation is based on Smart App Launch Implementation Guide 
(v2.1.0: STU 2.1) which in turn is based on FHIR R4. Finer grained 
**query parameters** within scopes **are not supported**, as there is
obvious easy way to implement them (e.g. combine different search parameters 
and preserve their overall intention) and further our use-case currently does
not provide a need for this functionality (feel encouraged to open a PR).

## Installation
```shell
pip install fhir.smart.scopes
```

## Usage
```python
from fhir.smart.scopes import scopes

a = scopes('launch offline_access patient/Medication.rs')
b = scopes('patient/Medication.cruds')
a & b
# patient/Medication.rs
a | b
# patient/Medication.cruds offline_access launch
```
The initial usecase expanded from a SMART on FHIR auth server implementation 
were we wanted to check the requested scopes against a predefined set of scopes
and optionally restrict a set of scopes by the predefined set:
```python
from fhir.smart.scopes import scopes

allowed = scopes('fhirUser launch/patient offline_access patient/Patient.rs patient/Medication.rs')
requested = 'launch/patient online_access patient/*.cruds'

permit = scopes(requested).intersection(allowed)
# launch/patient patient/Medication.rs patient/Patient.rs
```


## Interface 
All functions that would be expected for a 
[set type](https://python-reference.readthedocs.io/en/latest/docs/sets/) 
can be used, except the below-mentioned:
- Constructors: `scopes()` is the only supported initialization method 
available, set comprehension and literal syntax cannot be used. Initialize
ether with no arguments to obtain an empty scopes set, with a space seperated
string or an iterable with scopes.  
Only valid scopes can be initialized.
  ```python
  scopes()
  # 
  scopes('fhirUser openid')
  # fhirUser openid
  scopes(['fhirUser', 'patient/Observation.cru'])
  # patient/Observation.cru fhirUser
  scopes('invalidScope')
  # Traceback [...] ValueError
  ```
- Methods:
  - adding elements with `add` and `update` as you would expect them to work
  - deleting elements with `discard`, `remove`, `pop`, `clear`
  - obtain boolean information about scopes by `issuperset` (``), `issubset`
  and `isdisjoint`
  - use set operations `difference`, `intersection`, `symmetric_difference`, 
  `union` and assignments `difference_update`, `intersection_update`, 
  `symmetric_difference_update`
  - copy the scopes set with `copy`
- Operators:
  - add elements with `|=`
  - relational operators `==`, `!=`, `<=`, `<`, `>=`, `>`
  - operations `-`, `&`, `^`, `|`
  - assignment operations `-=`, `&=`, `^=`
- Functions:
  - len is supported and gives you the amount of 'atomic scopes' see below TODO
  - following function are somewhat meaningless in this context and therefore
  **not supported** (undefined behaviour): `min`, `max`, `sum`, `sorted`, 
  `reversed`, `all`, `any`, `enumerate`, `zip`

## Inner workings
This wrapper works by handling scopes as tuples of three things:
- Level or Top-level scope: e.g. *fhirUser*, *launch/Patient* or the *patient*
part of *patient/\*.cruds*
- Resource: a FHIR resource that is affected or None in the case of a top-level
scope, e.g. *Observation*
- Permission: one of the five permissions in *cruds*  

Internally scopes get stored in the super's set as these three-valued tuples
(atomic scopes) and this projects scopes type is responsible for validating 
given scope strings, extracting all atomic scope tuples out of them, and then
hide this inner structure when using set operations.

As an example, the following calls reveals this internal structure:
```python
>>> s = scopes('fhirUser patient/Patient.rs')
>>> s
fhirUser patient/Patient.rs
>>> set(s)
{('fhirUser', None, None), ('patient', 'Patient', 's'), ('patient', 'Patient', 'r')}
```
