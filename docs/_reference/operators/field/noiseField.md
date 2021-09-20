---
layout: operator
title: noiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/noiseField
redirect_from:
  - /reference/opType/raytk.operators.field.noiseField/
op:
  category: field
  detail: 'Some of these may be costly to compute, so pay attention to frame rate
    when using them.


    The different types of noise use different types of coordinates. If the type of
    coordinate used

    by `Noisetype` doesn''t match the `Coordtype`, any missing parts will be replaced
    with zeros.

    When the `Coordtype` is 3D but the `Noisetype` only uses 2D, the `Axis` parameter
    determines

    which parts of the coordinates are used.


    For types that use 4D coordinates, the `Translate` and `Scale` parameters can
    still be used to control the 4th coordinate.'
  images:
  - assets/images/reference/operators/field/noiseField_3d.png
  - assets/images/reference/operators/field/noiseField_3d_cheap_random.png
  - assets/images/reference/operators/field/noiseField_cheap_random.png
  - assets/images/reference/operators/field/noiseField_float_coord.png
  - assets/images/reference/operators/field/noiseField_perlin_2d.png
  - assets/images/reference/operators/field/noiseField_perlin_4d_in_2d.png
  - assets/images/reference/operators/field/noiseField_simplex_3d_in_2d.png
  - assets/images/reference/operators/field/noiseField_vector_coord.png
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
  name: noiseField
  opType: raytk.operators.field.noiseField
  parameters:
  - label: Noise Type
    menuOptions:
    - label: Simplex 2D
      name: TDSimplexNoise2d
    - label: Simplex 3D
      name: TDSimplexNoise3d
    - label: Simplex 4D
      name: TDSimplexNoise4d
    - label: Perlin 2D
      name: TDPerlinNoise2d
    - label: Perlin 3D
      name: TDPerlinNoise3d
    - label: Perlin 4D
      name: TDPerlinNoise4d
    - label: Classic Perlin 2D
      name: classicperlin2d
    - label: Classic Perlin 3D
      name: classicperlin3d
    - label: Classic Perlin 4D
      name: classicperlin4d
    - label: Simplex 2D
      name: simplex2d
    - label: Simplex 3D
      name: simplex3d
    - label: Simplex 4D
      name: simplex4d
    - label: Cheap Random Lookup
      name: cheapNoiseLookup
    name: Noisetype
    summary: The type of noise function.
  - label: Coord Type
    menuOptions:
    - label: float
      name: float
    - label: vec2
      name: vec2
    - label: vec3
      name: vec3
    name: Coordtype
    summary: The type of coordinates that the op supports.
  - name: Contexttype
  - label: Axis
    menuOptions:
    - description: Use Y and Z.
      label: X
      name: x
    - description: Use Z and X.
      label: Y
      name: y
    - description: Use X and Y.
      label: Z
      name: z
    name: Axis
    summary: When the `Noisetype` uses 2D coordinates but `Coordtype` is 3D, this
      is used to choose which plane of the coordinates are used.
  - label: Translate
    name: Translate
    summary: Offsets the coordinates used to calculate noise.
  - label: Scale
    name: Scale
    summary: Scales the coordinates used to calculate noise.
  - label: Amplitude
    name: Amplitude
    summary: Multiplies the amount produced by the noise.
  - label: Offset
    name: Offset
    summary: Offsets (adds to) the amount produced by the noise.
  summary: A float or vector field that uses one of several noise functions.

---


A float or vector field that uses one of several noise functions.

Some of these may be costly to compute, so pay attention to frame rate when using them.

The different types of noise use different types of coordinates. If the type of coordinate used
by `Noisetype` doesn't match the `Coordtype`, any missing parts will be replaced with zeros.
When the `Coordtype` is 3D but the `Noisetype` only uses 2D, the `Axis` parameter determines
which parts of the coordinates are used.

For types that use 4D coordinates, the `Translate` and `Scale` parameters can still be used to control the 4th coordinate.