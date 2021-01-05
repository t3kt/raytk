Bends space, along a main axis, towards a second axis.

For example, bends sideways (towards X) depending on the vertical position (along Y).

## Parameters

* `Enable`
* `Direction`: Chooses the axis to bend along and the axis to bend towards.
  * `xyz`
  * `xzy`
  * `yxz`
  * `yzx`
  * `zxy`
  * `zyx`
* `Amount`: Amount of bending.
* `Shift`: Shifts the axis to bend along and the axis to bend towards.
* `Inspect`

## Inputs

* `definition_in`
* `definition_in_2` *Bend Field*: Value field that determines how much to bend. If this accepts 1D coords, it is passed the position along the bend axis. For 2D coords, both the bend axis and the bend direction are passed. For 3D coords, the relative XYZ position is passed.