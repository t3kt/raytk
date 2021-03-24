Reshapes the values produced by a field by applying a function.

If the source field produces float values, the function is just applied to those values.
If the source field produces vector values, the function is applied individually to each channel in the produced values.
If the source is an SDF, the function is applied to the distance value in the SDF result.

## Parameters

* `Enable`

## Inputs

* `source_definition_in`: The field or SDF whose results will be reshaped.
* `function_definition_in`: The function that is applied to the results of the source field. In cases where the source field produces vectors but the function only works of single values, the function will be called 4 times. That can end up costly if the function is complex, though most function ops are relatively cheap.