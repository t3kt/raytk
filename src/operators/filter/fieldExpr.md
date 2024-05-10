Modifies field values using a custom expression.

The Expression parameter's menu contains common examples.

Writing expressions:

* To access a value from input 1, use a function call like `inputOp1(p, ctx)`
  * The `p` part is the spatial coordinate, so you can modify it with something like `inputOp1(p + vec3(1, 0, 0), ctx)`, which would move that field to the left.
  * The `ctx` part is required as the second argument to the function.
* Other inputs are available as `inputOp2(...)` etc
* The two slider parameters are available as `THIS_Param1` and `THIS_Param2`
* The two vector parameters are available as `THIS_Vecparam1` and `THIS_Vecparam2`
  * To get at an individual part of one of the vector params, you can use `THIS_Vecparam1.y`

## Parameters

* `Enable`
* `Expression`
  * `sqrt`
  * `abs`
  * `sign`
  * `cos`
  * `sin`
  * `tan`
  * `acos`
  * `asin`
  * `atan`
  * `atan2`
  * `cosh`
  * `sinh`
  * `tanh`
  * `log2`
  * `ln`
  * `exp`
  * `exp2`
  * `powb`
  * `powxy`
* `Param1`
* `Param2`
* `Vecparam1`
* `Vecparam2`
* `Coordtype`
  * `useinput`
  * `float`
  * `vec2`
  * `vec3`
* `Returntype`
  * `useinput`
  * `Sdf`
  * `vec4`
  * `float`
  * `Ray`
  * `Light`
* `Contexttype`
  * `useinput`
  * `auto`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
  * `RayContext`

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `definition_in_3`: 
* `definition_in_4`: 