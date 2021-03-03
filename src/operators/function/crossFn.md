Cross-fades between two input functions, either based on a parameter or on a third function.

A mix value of 0 is the first, 1 is the second. Values outside that range will linearly scale, as though the two input values are two points and a line extends off in the same direction on each end.


## Parameters

* `Enable`
* `Mix`: Cross-fade between the first two inputs. This is not used if the third input is connected.

## Inputs

* `definition_in`: 
* `definition_in_2`: 
* `mix_definition_in`: Function used to get the mix value used to blend between the first two inputs.