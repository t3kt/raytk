A mapping function that can change a value only when it's zero or very close to it, where it replaces the value with a small constant.

Then, rather than doing a conditional branch which introduces a discontinuity, you can smoothly blend your value with your Threshold.

This is based on Inigo Quilez's [article](https://iquilezles.org/www/articles/functions/functions.htm).

## Parameters

* `Contexttype`
  * `none`
  * `Context`
  * `MaterialContext`
  * `CameraContext`
  * `LightContext`
* `Threshold`: The value above which things will be unchanged.
* `Basevalue`: The constant value to use when the input is zero.