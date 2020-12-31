---
layout: operator
title: gyroidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/gyroidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.gyroidSdf/
op:
  name: gyroidSdf
  summary: Gyroid shape, which is an infinitely connected periodic surface.
  detail: |
    The Gyroid is constructed using overlapping sine and cosine waves.
    See [wikipedia](https://en.wikipedia.org/wiki/Gyroid) for more information.
  opType: raytk.operators.sdf.gyroidSdf
  category: sdf
  parameters:
    - name: Coordtype
      label: Coord Type
      summary: |
        Switches between 2D and 3D gyroids.
      menuOptions:
        - name: vec2
          label: 2D
        - name: vec3
          label: 3D
    - name: Contexttype
      label: Context Type
      summary: |
        Advanced parameter that should usually just be set to `Context`.
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
    - name: Translate
      label: Translate
      summary: |
        Moves the shape as a whole.
    - name: Scale
      label: Scale
      summary: |
        Spacing of the shape in each dimension.
    - name: Enableperiod
      label: Enable Period
      summary: |
        Whether to specify periods for the waves.
    - name: Period1
      label: Period 1
      summary: |
        Period of the first waves on each axis.
    - name: Period2
      label: Period 2
      summary: |
        Period of the second waves on each axis.
    - name: Enablephase
      label: Enable Phase
      summary: |
        Whether to specify phase shift for the waves.
    - name: Phase1
      label: Phase 1
      summary: |
        Phase shift of the first waves on each axis.
    - name: Phase2
      label: Phase 2
      summary: |
        Phase shift of the second waves on each axis.
    - name: Bias
      label: Bias
    - name: Thickness
      label: Thickness
      summary: |
        Expands the surfaces producing thicker shapes.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# gyroidSdf

Category: sdf



Gyroid shape, which is an infinitely connected periodic surface.

The Gyroid is constructed using overlapping sine and cosine waves.
See [wikipedia](https://en.wikipedia.org/wiki/Gyroid) for more information.