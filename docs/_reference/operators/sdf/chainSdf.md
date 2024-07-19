---
layout: operator
title: chainSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/chainSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.chainSdf/
op:
  category: sdf
  detail: Based on [Link - distance](https://www.shadertoy.com/view/wlXSD7) by iq.
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
    - vec3
    label: Length Field
    name: lengthField
    returnTypes:
    - float
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
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
  name: chainSdf
  opType: raytk.operators.sdf.chainSdf
  parameters:
  - label: Length
    name: Length
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Length of each chain link.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width / rounding radius of the chain links.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of each link.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
  summary: Chain made of links, with infinite length.
  thumb: assets/images/reference/operators/sdf/chainSdf_thumb.png

---


Chain made of links, with infinite length.

Based on [Link - distance](https://www.shadertoy.com/view/wlXSD7) by iq.