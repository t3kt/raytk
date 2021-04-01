A material element that provides specular light contribution.

## Parameters

* `Returntype`: Whether the lighting should have coloration or just a brightness level.
  * `float`
  * `vec4`
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