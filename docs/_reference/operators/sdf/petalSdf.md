---
layout: operator
title: petalSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/petalSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.petalSdf/
op:
  category: sdf
  detail: Based on [Echeveria](https://www.shadertoy.com/view/wlVGRz) by tdhooper.
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
    label: Thickness Field
    name: thicknessField
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
    label: Width Field
    name: widthField
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
    label: Wrap Field
    name: wrapField
    returnTypes:
    - float
  name: petalSdf
  opType: raytk.operators.sdf.petalSdf
  parameters:
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Thickness of the petal. Smaller values also cause the end to flatten
      out.
  - label: Width
    name: Width
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Width of the petal.
  - label: Wrap
    name: Wrap
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Different vertical slices of the sphere that it is based on. Low values
      keep the petal short at the base. Large values keep the petal short at the top.
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The radius of the sphere that the petal is based on.
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
    summary: Rotates the petal around the y axis.
  summary: A flower petal or leaf shape.
  thumb: assets/images/reference/operators/sdf/petalSdf_thumb.png

---


A flower petal or leaf shape.

Based on [Echeveria](https://www.shadertoy.com/view/wlVGRz) by tdhooper.