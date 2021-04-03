A material element that provides specular light contribution.

## Parameters

* `Color`
* `Level`
* `Method`: The type of specular shading to use. Different methods support different combinations of the other parameters.
  * `phong`
  * `blinnphong`
  * `beckmann`
  * `cooktorrance`
  * `gaussian`
  * `ggx`
* `Shininess`
* `Roughness`
* `Fresnel`
* `Usecolor`: Whether to produce color or just a brightness value.
* `Uselightcolor`: Whether to apply the light color to the color produced by this element.
* `Enableshadow`: Whether to apply the shadow to the color/level produced by this element.