---
layout: operator
title: hilbertCurveTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/hilbertCurveTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.hilbertCurveTransform/
op:
  category: filter
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
    - vec2
    - vec3
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
    supportedVariables:
    - localuv
    - cell
    - localcell
  name: hilbertCurveTransform
  opType: raytk.operators.filter.hilbertCurveTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Axis
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: The axis facing the plane along which space is repeated.
  - label: Steps
    name: Steps
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/filter/hilbertCurveTransform_thumb.png
  variables:
  - label: Local UV
    name: localuv
  - label: Cell Number
    name: cell
  - label: Cell Local Number
    name: localcell

---
