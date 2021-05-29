Restricts which render stages an operator is used in.


This can be used for optimization, by switching off expensive ROPs for shadows.
It can also be used to have shapes that are invisible but still cast shadows.

In cases where the main operator is not being included, this will produce either the alternative operator input (if connected), or a default value otherwise.
The default value is "non-hit" for SDFs, and `0` / `vec4(0)` etc for other types.

## Parameters

* `Enable`
* `Includeprimary`: Whether the operator should 
* `Includeshadow`
* `Includereflect`
* `Includematerial`
* `Includeocclusion`

## Inputs

* `definition_in`: 
* `alternate_definition_in`: 