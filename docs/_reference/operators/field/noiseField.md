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
    name: Noisetype
  - label: Coord Type
    menuOptions:
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Context Type
    menuOptions:
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Amplitude
    name: Amplitude
  - label: Offset
    name: Offset
  summary: A float or vector field that uses one of several noise functions.

---

# noiseField

Category: field



A float or vector field that uses one of several noise functions.