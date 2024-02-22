---
layout: operator
title: arrowSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/arrowSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.arrowSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Point Coords Field
    name: points
    returnTypes:
    - vec4
  name: arrowSdf2d
  opType: raytk.operators.sdf2d.arrowSdf2d
  parameters:
  - label: From Point
    name: Pointa
    readOnlyHandling: baked
    regularHandling: runtime
  - label: To Point
    name: Pointb
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Head Thickness
    name: Headthickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Head Ratio
    name: Headratio
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/arrowSdf2d_thumb.png

---
