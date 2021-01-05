Smoothly blends/morphs between up to 4 SDFs.

The blend index only considers inputs that are connected, so if you connect the second and fourth inputs, it will treat the second as 0 and the fourth as 1.

## Parameters

* `Enable`
* `Blend`: Which input or combination of inputs to use. If this value is 0, the first connected input is used. 0.5 is half way between the first and second connected inputs, etc.
* `Inspect`