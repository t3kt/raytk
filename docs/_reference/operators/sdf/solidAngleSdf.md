---
layout: operator
title: solidAngleSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/solidAngleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.solidAngleSdf/
op:
  category: sdf
  detail: Similar to `coneSdf` but with the base rounded.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Angle Field
    name: angleField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  keywords:
  - cone
  - pie
  - slice
  - wedge
  name: solidAngleSdf
  opType: raytk.operators.sdf.solidAngleSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the tip of the shape.
  - label: Angle
    name: Angle
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The angle width of the slice.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the sphere that the shape is based one, equivalent to the
      distance from the tip to the base.
  summary: A conical slice of a sphere.
  thumb: assets/images/reference/operators/sdf/solidAngleSdf_thumb.png

---


A conical slice of a sphere.

Similar to `coneSdf` but with the base rounded.