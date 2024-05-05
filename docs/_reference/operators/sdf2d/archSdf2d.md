---
layout: operator
title: archSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/archSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.archSdf2d/
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - vec4
    summary: Field used to multiply the width and height of the shape.
  name: archSdf2d
  opType: raytk.operators.sdf2d.archSdf2d
  parameters:
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width and height of the shape. The width is also used as the radius of
      the top curve.
  summary: Arched doorway shape with a rounded top and rectangular bottom.
  thumb: assets/images/reference/operators/sdf2d/archSdf2d_thumb.png

---


Arched doorway shape with a rounded top and rectangular bottom.