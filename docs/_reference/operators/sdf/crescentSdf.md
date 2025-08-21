---
layout: operator
title: crescentSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/crescentSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.crescentSdf/
op:
  category: sdf
  detail: Based on [Croissant SDF](https://www.shadertoy.com/view/NdlBD4) by erratac.
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
    - PopContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  name: crescentSdf
  opType: raytk.operators.sdf.crescentSdf
  parameters:
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Radius of the main curve of the crescent.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the crescent.
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Rotates the crescent around the axis that it's curving around.
  summary: Rounded crescent shape.
  thumb: assets/images/reference/operators/sdf/crescentSdf_thumb.png

---


Rounded crescent shape.

Based on [Croissant SDF](https://www.shadertoy.com/view/NdlBD4) by erratac.