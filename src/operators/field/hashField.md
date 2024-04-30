Advanced field that produces randomized values.

This should typically be used with an input that provides numbers that the randomization should be based on, but it can be used without an input in which case it uses spatial position as the basis.

A typical use case for this operator would be something like randomizing a property within each cell of a `modulo2D`. The cell coordinates, accessed using a `variableReference`, would be passed into the `hashField`, which would produce random numbers that could be mapped to control the radius of a cylinder for example.

The available hash functions have different types of inputs and outputs. Some take a single number input and produce a single number. Others take a single number and produce vectors. And still others take in a vector with multiple parts to produce single numbers, etc.

Each hash function has a different range of values that it will produce. Their labels in the parameter menu contain information about how they behave.

The label suffixes are in the format `(<coord> -> <return>)`, where the first part is the type of coordinates or input value that it uses and the second is the type of value that it produces.

Types labeled `X` mean it only uses/produces a single number, the X part of vectors.

Types labeled `XYZ` mean it uses/produces 3 parts of vectors.

Types marked with `[U]` mean unsigned integers, which treat all negative numbers as zero, and produce whole numbers ranging from 0 to 4294967295. 

Types without `[U]` mean floats, which can be any number. For outputs, that typically means a 0..1 or -1..1 range.

Based on [Hash Functions for GPU Rendering](https://www.shadertoy.com/view/XlGcRh) by markjarzynski.

More details avaiable [here](http://jcgt.org/published/0009/03/02/).

## Parameters

* `Function`
  * `bbs`
  * `city11`
  * `city12`
  * `city13`
  * `city14`
  * `esgtsa`
  * `fast`
  * `hashwithoutsine11`
  * `hashwithoutsine12`
  * `hashwithoutsine13`
  * `hashwithoutsine21`
  * `hashwithoutsine22`
  * `hashwithoutsine23`
  * `hashwithoutsine31`
  * `hashwithoutsine32`
  * `hashwithoutsine33`
  * `hashwithoutsine41`
  * `hashwithoutsine42`
  * `hashwithoutsine43`
  * `hashwithoutsine44`
  * `hybridtaus`
  * `ign`
  * `iqint1`
  * `iqint2`
  * `iqint3`
  * `jkiss32`
  * `lcg`
  * `md5`
  * `murmur311`
  * `murmur312`
  * `murmur313`
  * `murmur314`
  * `pcg`
  * `pcg2d`
  * `pcg3d`
  * `pcg3d16`
  * `pcg4d`
  * `pseudo`
  * `ranlim32`
  * `superfast11`
  * `superfast21`
  * `superfast31`
  * `superfast41`
  * `trig21`
  * `wang11`
  * `xorshift128`
  * `xorshift32`
  * `xxhash321`
  * `xxhash322`
* `Coordtype`
  * `auto`
  * `float`
  * `vec2`
  * `vec3`
  * `vec4`

## Inputs

* `coordField`: 