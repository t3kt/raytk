---
layout: operator
title: noiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/noiseField
redirect_from:
  - /reference/opType/raytk.operators.field.noiseField/
op:
  name: noiseField
  summary: A float or vector field that uses one of several noise functions.
  opType: raytk.operators.field.noiseField
  category: field
  parameters:
    - name: Noisetype
      label: Noise Type
      menuOptions:
        - name: TDSimplexNoise2d
          label: Simplex 2D
        - name: TDSimplexNoise3d
          label: Simplex 3D
        - name: TDSimplexNoise4d
          label: Simplex 4D
        - name: TDPerlinNoise2d
          label: Perlin 2D
        - name: TDPerlinNoise3d
          label: Perlin 3D
        - name: TDPerlinNoise4d
          label: Perlin 4D
    - name: Coordtype
      label: Coord Type
      menuOptions:
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Axis
      label: Axis
      menuOptions:
        - name: x
          label: X
        - name: y
          label: Y
        - name: z
          label: Z
    - name: Translate
      label: Translate
    - name: Scale
      label: Scale
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# noiseField

Category: field



A float or vector field that uses one of several noise functions.