---
layout: operator
title: extrudeBezier
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/extrudeBezier
redirect_from:
  - /reference/opType/raytk.operators.filter.extrudeBezier/
op:
  category: filter
  detail: Based on (`BezierExtrude` by Del)[https://www.shadertoy.com/view/7dyBz3].
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
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - point1Field
    - point2Field
    - point3Field
    supportedVariables:
    - normoffset
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
  name: extrudeBezier
  opType: raytk.operators.filter.extrudeBezier
  parameters:
  - label: Enable
    name: Enable
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
  status: beta
  summary: Extrudes 3D space along the path of a bezier curve.
  thumb: assets/images/reference/operators/filter/extrudeBezier_thumb.png
  variables:
  - label: Normalized Spline Offset (0..1)
    name: normoffset

---


Extrudes 3D space along the path of a bezier curve.

Based on (`BezierExtrude` by Del)[https://www.shadertoy.com/view/7dyBz3].