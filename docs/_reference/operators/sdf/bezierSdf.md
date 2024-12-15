---
layout: operator
title: bezierSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/bezierSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.bezierSdf/
op:
  category: sdf
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
    label: Point 1 Field
    name: point1Field
    returnTypes:
    - vec4
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
    label: Point 2 Field
    name: point2Field
    returnTypes:
    - vec4
    supportedVariableInputs:
    - point1Field
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
    label: Point 3 Field
    name: point3Field
    returnTypes:
    - vec4
    supportedVariableInputs:
    - point1Field
    - point2Field
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - point1Field
    - point2Field
    - point3Field
    supportedVariables:
    - normoffset
  keywords:
  - bezier
  - curve
  - line
  name: bezierSdf
  opType: raytk.operators.sdf.bezierSdf
  parameters:
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 3
    name: Point3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius Start
    name: Radiusstart
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius End
    name: Radiusend
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/bezierSdf_thumb.png
  variables:
  - label: Offset Along Curve (0..1)
    name: normoffset

---
