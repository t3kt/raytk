Shifts contextual time for upstream operators, either by a fixed amount or using a value field.

## Parameters

* `Enable`
* `Shift`: Fixed offset to apply to contextual time of upstream operators.
* `Intervaltype`: The unit and part of time to shift.
  * `seconds`: Shifts timeline time by seconds (also updates timeline frame).
  * `frames`: Shifts timeline time by frames (also updates timeline seconds).
  * `absseconds`: Shifts absolute time by seconds (also updates absolute seconds).
  * `absframes`: Shifts absolute time by frames (also updates absolute frame).

## Inputs

* `definition_in`: 
* `shift_definition_in`: Value field used to add to the `Shift` value.
