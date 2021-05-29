Transforms space with rotation.

The operator has 2 main modes: a single rotation around an axis, or 3 separate rotations around each axis.

## Parameters

* `Enable`
* `Rotatemode`
  * `axis`: Apply a single rotation around an axis. This is also implicitly used if the input uses 2D coordinates.
  * `euler`: Apply 3 separate rotations around each axis.
* `Axis`: The direction of the axis around which to rotate. This is a vector pointing along the axis.
* `Rotate`: The amount of rotation to use when in single-axis mode. This is specified in degrees (0..360).
* `Rord`: The order of the 3 axis rotations.
  * `xyz`
  * `xzy`
  * `yxz`
  * `yzx`
  * `zxy`
  * `zyx`
* `Rot`: The amount of rotation along each axis, in degrees (0..360).
* `Usepivot`: Optionally pivot the rotation around a specific point instead of around the origin (0, 0, 0).
* `Pivot`: The point around which to apply the rotation. For 2D coordinates, only the X and Y parts are used.

## Inputs

* `definition_in`: 
* `rotate_definition_in`: Optional field that can be used to control the amount of rotation. If in single axis mode, this must produce a single float value, which is added to the `Rotate` parameter. If in 3 axis mode, it can either produce a single value, which is multiplied with each of the axis rotations. Or it can produce vectors which are added to the axis rotations.
* `pivot_definition_in`: Optional field that can be used to control the pivot point.