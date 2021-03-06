Texture field that uses surface normals (or other blending techniques) to apply a texture facing each axis.

On a cube centered at the origin, this has the effect of placing the texture on each side of the cube.
For a sphere, when using normal blending, the texture for each axis will smoothly blend as the surface normal shifts from one axis to another.

Textures are centered at 0,0 with coordinates ranging from -0.5 to 0.5.

## Parameters

* `Enable`
* `Returntype`: Type of value to produce.
  * `float`: Single float value (from the R channel).
  * `vec4`: RGBA values.
* `Translate`
* `Scale`
* `Useseparatetextures`: Whether to use a single texture for all axes, or a separate texture for each axis.
* `Texture`
* `Texturex`
* `Texturey`
* `Texturez`
* `Extendmode`: How to handle coordinates outside the texture's bounds.
  * `hold`: Clamp the coordinates so that the last pixel on each side is extended out infinitely.
  * `zero`: Produces values of 0 outside the bounds.
  * `repeat`: Tiles the texture.
  * `mirror`: Tiles the texture, but flips alternating copies of it.
* `Blendmode`: How to combine the colors from each axis.
  * `normals`: Use surface normals to blend the colors. Note that this can cause issues with material local positioning.
  * `add`: Add the colors from each axis.
  * `max`: Maximum for each channel from each axis.
  * `avg`: Average the colors from each axis.