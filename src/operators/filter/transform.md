Transform the coordinates of the input, with rotation, scaling, and translation.

Various parts of the transform can be switched off to improve performance, and the sequence of transform steps can be reordered.
It either uses the origin (0,0,0) as the pivot point, or can use another pivot point.

## Parameters

* `Enable`
* `Enabletranslate`
* `Enablerotate`
* `Enablescale`
* `Enablepivot`
* `Translate`
* `Rotate`
* `Scale`
* `Uniformscale`
* `Pivot`
* `Transformorder`
  * `srt`
  * `str`
  * `rst`
  * `rts`
  * `tsr`
  * `trs`
* `Rotateorder`
  * `xyz`
  * `xzy`
  * `yxz`
  * `yzx`
  * `zxy`
  * `zyx`
* `Scaletype`
  * `separate`
  * `uniform`
* `Target`
  * `coords`
  * `sdfuv`
  * `sdfuv2`
  * `matuv`
  * `value`

## Inputs

* `definition_in`: 
* `rotateField`: 
* `translateField`: 
* `scaleField`: 