---
layout: operator
title: trefoilKnotSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/trefoilKnotSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.trefoilKnotSdf/
op:
  category: sdf
  detail: Based on [Trefoil Knot Explained](https://www.shadertoy.com/view/M3tXW4)
    by ruudhelderman.
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
    supportedVariables:
    - angle
    - normangle
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
    supportedVariables:
    - angle
    - normangle
  name: trefoilKnotSdf
  opType: raytk.operators.sdf.trefoilKnotSdf
  parameters:
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
    regularHandling: semibaked
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  summary: Trefoil knot SDF.
  thumb: assets/images/reference/operators/sdf/trefoilKnotSdf_thumb.png
  variables:
  - label: Angle (0-360)
    name: angle
  - label: Normalized Angle (0-1)
    name: normangle

---


Trefoil knot SDF.

Based on [Trefoil Knot Explained](https://www.shadertoy.com/view/M3tXW4) by ruudhelderman.