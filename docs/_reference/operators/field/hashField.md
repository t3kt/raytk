---
layout: operator
title: hashField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/hashField
redirect_from:
  - /reference/opType/raytk.operators.field.hashField/
op:
  category: field
  detail: "This should typically be used with an input that provides numbers that\
    \ the randomization should be based on, but it can be used without an input in\
    \ which case it uses spatial position as the basis.\n\nA typical use case for\
    \ this operator would be something like randomizing a property within each cell\
    \ of a `modulo2D`. The cell coordinates, accessed using a `variableReference`,\
    \ would be passed into the `hashField`, which would produce random numbers that\
    \ could be mapped to control the radius of a cylinder for example.\n\nThe available\
    \ hash functions have different types of inputs and outputs. Some take a single\
    \ number input and produce a single number. Others take a single number and produce\
    \ vectors. And still others take in a vector with multiple parts to produce single\
    \ numbers, etc.\n\nEach hash function has a different range of values that it\
    \ will produce. Their labels in the parameter menu contain information about how\
    \ they behave.\n\nThe label suffixes are in the format `(<coord> -> <return>)`,\
    \ where the first part is the type of coordinates or input value that it uses\
    \ and the second is the type of value that it produces.\n\nTypes labeled `X` mean\
    \ it only uses/produces a single number, the X part of vectors.\n\nTypes labeled\
    \ `XYZ` mean it uses/produces 3 parts of vectors.\n\nTypes marked with `[U]` mean\
    \ unsigned integers, which treat all negative numbers as zero, and produce whole\
    \ numbers ranging from 0 to 4294967295. \n\nTypes without `[U]` mean floats, which\
    \ can be any number. For outputs, that typically means a 0..1 or -1..1 range.\n\
    \nBased on [Hash Functions for GPU Rendering](https://www.shadertoy.com/view/XlGcRh)\
    \ by markjarzynski.\n\nMore details avaiable [here](http://jcgt.org/published/0009/03/02/)."
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  name: hashField
  opType: raytk.operators.field.hashField
  parameters:
  - label: Function
    menuOptions:
    - label: BBS  (X[u] -> X[u])
      name: bbs
    - label: CityHash32 (1D)  (X[u] -> X[u])
      name: city11
    - label: CityHash32 (2D)  (XY[u] -> X[u])
      name: city12
    - label: CityHash32 (3D)  (XYZ[u] -> X[u])
      name: city13
    - label: CityHash32 (4D)  (XYZW[u] -> X[u])
      name: city14
    - label: Schechter and Bridson  (X[u] -> X[u])
      name: esgtsa
    - label: UE4 RandFast  (XY -> X)
      name: fast
    - label: Hash w/o Sine 1:1  (X -> X)
      name: hashwithoutsine11
    - label: Hash w/o Sine 2:1  (XY -> X)
      name: hashwithoutsine12
    - label: Hash w/o Sine 3:1  (XYZ -> X)
      name: hashwithoutsine13
    - label: Hash w/o Sine 1:2  (X -> XY)
      name: hashwithoutsine21
    - label: Hash w/o Sine 2:2  (XY -> XY)
      name: hashwithoutsine22
    - label: Hash w/o Sine 3:2  (XYZ -> XY)
      name: hashwithoutsine23
    - label: Hash w/o Sine 1:3  (X -> XYZ)
      name: hashwithoutsine31
    - label: Hash w/o Sine 2:3  (XY -> XYZ)
      name: hashwithoutsine32
    - label: Hash w/o Sine 3:3  (XYZ -> XYZ)
      name: hashwithoutsine33
    - label: Hash w/o Sine 1:4  (X -> XYZW)
      name: hashwithoutsine41
    - label: Hash w/o Sine 2:4  (XY -> XYZW)
      name: hashwithoutsine42
    - label: Hash w/o Sine 3:4  (XYZ -> XYZW)
      name: hashwithoutsine43
    - label: Hash w/o Sine 4:4  (XYZW -> XYZW)
      name: hashwithoutsine44
    - label: Hybrid Taus  (XYZW[u] -> X)
      name: hybridtaus
    - label: Interleaved Gradient  (XY -> X)
      name: ign
    - label: Integer Hash I  (X[u] -> X[u])
      name: iqint1
    - label: Integer Hash II  (XYZ[u] -> XYZ[u])
      name: iqint2
    - label: Integer Hash III  (XY[u] -> X[u])
      name: iqint3
    - label: JKiss32  (XY[u] -> X[u])
      name: jkiss32
    - label: Linear Congruential  (X[u] -> X[u])
      name: lcg
    - label: MD5GPU  (XYZW[u] -> XYZW[u])
      name: md5
    - label: Murmur Hash 3 1:1  (X[u] -> X[u])
      name: murmur311
    - label: Murmur Hash 3 2:1  (XY[u] -> X[u])
      name: murmur312
    - label: Murmur Hash 3 3:1  (XYZ[u] -> X[u])
      name: murmur313
    - label: Murmur Hash 3 4:1  (XYZW[u] -> X[u])
      name: murmur314
    - label: PCG Random  (X[u] -> X[u])
      name: pcg
    - label: PCG 2D  (XY[u] -> XY[u])
      name: pcg2d
    - label: PCG 3D  (XYZ[u] -> XYZ[u])
      name: pcg3d
    - label: PCG 3D 16  (XYZ[u] -> XYZ[u])
      name: pcg3d16
    - label: PCG 4D  (XYZW[u] -> XYZW[u])
      name: pcg4d
    - label: UE4 PseudoRandom  (XY -> X)
      name: pseudo
    - label: RanLim 32  (X[u] -> X[u])
      name: ranlim32
    - label: SuperFastHash 1:1  (X[u] -> X[u])
      name: superfast11
    - label: SuperFastHash 2:1  (XY[u] -> X[u])
      name: superfast21
    - label: SuperFastHash 3:1  (XYZ[u] -> X[u])
      name: superfast31
    - label: SuperFastHash 4:1  (XYZW[u] -> X[u])
      name: superfast41
    - label: Trig 2:1  (XY -> X)
      name: trig21
    - label: Wang 1:1  (X[u] -> X[u])
      name: wang11
    - label: 128-bit XOR Shift  (XYZW[u] -> X[u])
      name: xorshift128
    - label: 32-bit XOR Shift  (X[u] -> X[u])
      name: xorshift32
    - label: 32-bit XX Hash 1:1  (X[u] -> X[u])
      name: xxhash321
    - label: 32-bit XX Hash 2:1  (XY[u] -> X[u])
      name: xxhash322
    name: Function
    readOnlyHandling: baked
    regularHandling: baked
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    - label: 4D
      name: vec4
    name: Coordtype
  status: beta
  summary: Advanced field that produces randomized values.

---


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