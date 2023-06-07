Combines three 2D fields based on vectors like surface normals.

## Parameters

* `Translate`
* `Scale`
* `Usenormals`: Modifies the amount of each field that's used based on how directly the surface normals are facing that plane. For example, the XY field is used most on parts that are facing forwards or backwards.
* `Blendmode`: How the values from each field are combined.
  * `add`
  * `max`
  * `avg`
* `Returntype`
  * `auto`
  * `float`
  * `vec4`

## Inputs

* `uvField`: Alternative way to provide the coordinates used by the fields rather than just using the position in space. Each input field gets two of the axes of the coordinates provided (e.g. the XY field gets the x and y).
* `normalField`: Field that provides the surface normals used to adjust the influence of each plane. Typically this should be a `normalField` or a `variableReference` that accesses a surface normal within a material.
* `xyField`: 
* `yzField`: 
* `zxField`: 