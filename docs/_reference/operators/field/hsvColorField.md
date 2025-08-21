---
layout: operator
title: hsvColorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/hsvColorField
redirect_from:
  - /reference/opType/raytk.operators.field.hsvColorField/
op:
  category: field
  detail: By default, the X axis is used for the hue.
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
    label: Hue Field
    name: hueField
    returnTypes:
    - float
    summary: Optional field that can calculate the hue setting based on position or
      other attributes.
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
    label: Saturation Field
    name: saturationField
    returnTypes:
    - float
    summary: Optional field that can calculate the saturation setting based on position
      or other attributes.
    supportedVariableInputs:
    - hueField
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
    label: Value Field
    name: valueField
    returnTypes:
    - float
    summary: Optional field that can calculate the value setting based on position
      or other attributes.
    supportedVariableInputs:
    - hueField
    - saturationField
  name: hsvColorField
  opType: raytk.operators.field.hsvColorField
  parameters:
  - label: Hue Offset
    name: Hueoffset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Saturation
    name: Saturation
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Value
    name: Value
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - name: Contexttype
  summary: A field that uses HSV-based parameters to produce colors.
  thumb: assets/images/reference/operators/field/hsvColorField_thumb.png

---


A field that uses HSV-based parameters to produce colors.

By default, the X axis is used for the hue.