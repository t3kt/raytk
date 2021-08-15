Use a field to modify the normals (bump mapping) used by shading elements in a modular material.

This must be used *within* the modular material network, rather than on an SDF that
uses such a material. In other words, insert it between an operator like `diffuseContrib`
and the `modularMat`.

This can be combined with a `noiseField` or `textureField` to apply bump mapping to a surface.

## Parameters

* `Enable`
* `Mode`: How the modifier values are applied to the normals.
  * `add`: The modifier values are added to the normals.
  * `mul`: The normals are multiplied by the modifier values.
* `Mix`: Mix between the original normals and the modified normals.

## Inputs

* `shading_element_in`: Shading element that will use the modified normals. This should be something like `diffuseContrib` or `specularContrib`.
* `modifier_field_in`: Field used to modify the normals.