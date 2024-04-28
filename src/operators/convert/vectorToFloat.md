Converts a vector value field to a float field, e.g. using one part of the vector.

## Parameters

* `Enable`
* `Usepart`: Which part of the vector to use for the float field.
  * `x`
  * `y`
  * `z`
  * `w`
  * `lengthxy`: Use the length of the XY parts of the vector.
  * `lengthxyz`: Use the length of the XYZ parts of the vector.
  * `lengthxyzw`: Use the length of all 4 parts of the vector.
  * `minxy`: Minimum of the X and Y.
  * `minxyz`:  Minimum of the X, Y, and Z.
  * `minxyzw`: Minimum of all 4 parts.
  * `maxxy`: Maximum of the X and Y.
  * `maxxyz`: Maximum of the X, Y, and Z.
  * `maxxyzw`: Maximum of all 4 parts.
  * `avgxy`: Average of X and Y.
  * `avgxyz`: Average of X, Y, and Z.
  * `avgxyzw`: Average of all 4 parts.
  * `hue`: Treat the vector as an RGB color and get the hue.
  * `sat`: Treat the vector as an RGB color and get the saturation.
  * `val`: Treat the vector as an RGB color and get the value (as in HSV).
  * `luma`: Treat the vector as an RGB color and get the luminance.
  * `sumxy`: Add the X and Y parts.
  * `sumxyz`: Add the X, Y, and Z parts.
  * `sumxyzw`: Add all 4 parts.

## Inputs

* `definition_in`: 