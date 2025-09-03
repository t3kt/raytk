---
layout: operator
title: knitPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/knitPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.knitPattern/
op:
  category: pattern
  detail: Note that this pattern has a lot of fine detail which does not work well
    for things like offsetting SDF surfaces, unless the Texture Amount is set to 0.
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
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
  name: knitPattern
  opType: raytk.operators.pattern.knitPattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the pattern.
  - label: Texture Amount
    name: Texamount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of roughness in the pattern.
  - label: Texture Density
    name: Texdensity
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Tightness of the roughness.
  status: beta
  summary: Woven yarn pattern.
  thumb: assets/images/reference/operators/pattern/knitPattern_thumb.png

---


Woven yarn pattern.

Note that this pattern has a lot of fine detail which does not work well for things like offsetting SDF surfaces, unless the Texture Amount is set to 0.