---
layout: operator
title: stepField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/stepField
redirect_from:
  - /reference/opType/raytk.operators.field.stepField/
op:
  category: field
  detail: 'This can be used to apply one color to the left of some point and another
    color on the right side of that point.

    It can also smooth out the transition between the two values.'
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
    label: Coordinate Field
    name: coordField
    returnTypes:
    - float
    - vec4
    summary: Optional field whose value is used instead of coordinates when checking
      which side of the threshold a point is on.
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
    label: Edge Field
    name: edgeField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
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
    label: Low Value Field
    name: lowValue
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - edgeField
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
    label: High Value Field
    name: highValue
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - edgeField
    - lowValue
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
    label: Blend Amount Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - edgeField
    - lowValue
    - highValue
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
    label: Blend Function
    name: blendFunction
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - edgeField
    - lowValue
    - highValue
    - blendingField
  name: stepField
  opType: raytk.operators.field.stepField
  parameters:
  - label: Enable
    name: Enable
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
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: Distance From Origin
      name: dist
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Edge
    name: Edge
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Reverse
    name: Reverse
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Enable Blend
    name: Enableblend
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Blend
    name: Blend
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Return Type
    menuOptions:
    - label: Float
      name: float
    - label: Vector
      name: vec4
    name: Returntype
  - label: Low Value
    name: Value1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Value used when below `Edge`
  - label: High Value
    name: Value2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Value used when above `Edge`
  - name: Contexttype
  summary: A field that switches between two values at a threshold point.
  thumb: assets/images/reference/operators/field/stepField_thumb.png

---


A field that switches between two values at a threshold point.

This can be used to apply one color to the left of some point and another color on the right side of that point.
It can also smooth out the transition between the two values.