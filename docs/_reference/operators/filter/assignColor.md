---
layout: operator
title: assignColor
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/assignColor
redirect_from:
  - /reference/opType/raytk.operators.filter.assignColor/
op:
  category: filter
  detail: Various types of materials and fields can access and use the surface color
    attributes.
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF or Volume
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    - Volume
    summary: SDF definition to which the color is applied.
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
    - float
    - vec2
    - vec3
    - vec4
    label: Color Field
    name: colorField
    returnTypes:
    - float
    - vec4
    summary: Optional field used to calculate the color instead of the `Color` parameter.
    supportedVariableInputs:
    - inputOp1
    supportedVariables:
    - sdf
  keywords:
  - color
  - material
  - modularmat
  - surface
  name: assignColor
  opType: raytk.operators.filter.assignColor
  parameters:
  - label: Enable
    name: Enable
  - label: Color
    name: Color
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Assign When
    menuOptions:
    - label: Always
      name: always
    - label: Only If Unassigned
      name: missing
    name: Condition
    readOnlyHandling: baked
    regularHandling: runtime
  shortcuts:
  - ac
  summary: Assigns a surface color attribute to an SDF surface.
  thumb: assets/images/reference/operators/filter/assignColor_thumb.png
  variables:
  - label: SDF Surface
    name: sdf

---


Assigns a surface color attribute to an SDF surface.

Various types of materials and fields can access and use the surface color attributes.