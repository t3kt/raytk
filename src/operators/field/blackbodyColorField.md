Field that produces colors using a model of blackbody radiation from physics.

The operator uses a temperature value, either from a parameter of an input field, and determines the glow color that temperature would produce.

Based on [Tunnel Beauty](https://www.shadertoy.com/view/Mt3GW2) by aiekick.

Details on [wikipedia](https://en.wikipedia.org/wiki/Black_body).

## Parameters

* `Temp`: Constant value to use for the temperature, everywhere in space. This is only used if there is no input temperature field.
* `Tempunit`: How to interpret temperature values.
  * `norm`: Normalized to a 0..1 range.
  * `deg`: Degrees kelvin.
* `Exp`: Tighness of the transition curve from dark to light.

## Inputs

* `tempField`: 