SDF for a box, optionally infinite one one axis.

## Parameters

* `Boxtype`: The type of box function.
  * `boxcheap`: A bit more efficient but slightly less accurate.
  * `box`: More accurate but slightly less efficient.
* `Infiniteaxis`: Axis along which the box should stretch infinitely.
  * `none`: Regular box.
  * `x`: Box is infinite along the x axis.
  * `y`: Box is infinite along the y axis.
  * `z`: Box is infinite along the z axis.
* `Translate`: Move the center of the box.
* `Scale`: The size of the box in each dimension.
* `Uniformscale`: Scaling applied to all dimensions of the `Scale`.
* `Inspect`