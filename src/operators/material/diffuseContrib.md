A material element that provides diffuse light contribution.

## Parameters

* `Color`
* `Level`
* `Method`: The type of diffuse shading to use. Different methods support different combinations of the other parameters.
  * `lambert`
  * `orennayar`
* `Roughness`
* `Albedo`
* `Usecolor`: Whether to produce color or just a brightness value.
* `Uselightcolor`: Whether to apply the light color to the color produced by this element.
* `Enableshadow`: Whether to apply the shadow to the color/level produced by this element.