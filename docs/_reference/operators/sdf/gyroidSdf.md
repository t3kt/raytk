---
layout: operator
title: gyroidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/gyroidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.gyroidSdf/
op:
  category: sdf
  detail: 'The Gyroid is constructed using overlapping sine and cosine waves.

    See [wikipedia](https://en.wikipedia.org/wiki/Gyroid) for more information.'
  name: gyroidSdf
  opType: raytk.operators.sdf.gyroidSdf
  parameters:
  - label: Coord Type
    menuOptions:
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
    summary: Switches between 2D and 3D gyroids.
  - menuOptions:
    - name: none
    - name: Context
    - name: MaterialContext
    - name: CameraContext
    - name: LightContext
    name: Contexttype
    summary: Advanced parameter that should usually just be set to `Context`.
  - label: Translate
    name: Translate
    summary: Moves the shape as a whole.
  - label: Scale
    name: Scale
    summary: Spacing of the shape in each dimension.
  - label: Enable Period
    name: Enableperiod
    summary: Whether to specify periods for the waves.
  - label: Period 1
    name: Period1
    summary: Period of the first waves on each axis.
  - label: Period 2
    name: Period2
    summary: Period of the second waves on each axis.
  - label: Enable Phase
    name: Enablephase
    summary: Whether to specify phase shift for the waves.
  - label: Phase 1
    name: Phase1
    summary: Phase shift of the first waves on each axis.
  - label: Phase 2
    name: Phase2
    summary: Phase shift of the second waves on each axis.
  - label: Bias
    name: Bias
  - label: Thickness
    name: Thickness
    summary: Expands the surfaces producing thicker shapes.
  summary: Gyroid shape, which is an infinitely connected periodic surface.

---


Gyroid shape, which is an infinitely connected periodic surface.

The Gyroid is constructed using overlapping sine and cosine waves.
See [wikipedia](https://en.wikipedia.org/wiki/Gyroid) for more information.