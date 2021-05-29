Performs a transform multiple times, optionally reflecting across axes in between the steps.

This can be used to create KIFS fractals (kaleidoscopic iterated function systems).

## Parameters

* `Enable`
* `Iterations`
* `Reflectmode`
  * `none`
  * `xyz`
  * `x`
  * `y`
  * `z`
  * `xy`
  * `yz`
  * `zx`
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
* `Customcode`
* `Floatparam1`
* `Floatparam2`
* `Floatparam3`
* `Floatparam4`
* `Vecparam1`
* `Vecparam2`
* `Vecparam3`
* `Vecparam4`

## Inputs

* `definition_in`: 
* `rotate_definition_in`: Optional field used to control rotation. The field is evaluated before each iteration, and the resulting value is added to the `Rotate` parameter. If the field uses 2D/3D coordinates, the current position is used. If the field uses 1D coordinates, it is passed `i / (n-1)`, where `i` is the loop iteration, and `n` is the total number of iterations.