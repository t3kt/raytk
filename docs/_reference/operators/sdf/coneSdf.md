---
layout: operator
title: coneSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/coneSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.coneSdf/
op:
  category: sdf
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
    label: Base Position Field
    name: baseField
    returnTypes:
    - vec4
    summary: Value field that can be used to vary the height of the cone.
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
    label: Height Field
    name: heightField
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius (both base and top) of
      the cone.
    supportedVariableInputs:
    - baseField
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
    label: Top Position Field
    name: topField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - baseField
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
    supportedVariableInputs:
    - baseField
    - heightField
    - topField
  name: coneSdf
  opType: raytk.operators.sdf.coneSdf
  parameters:
  - name: Enable
  - label: Shape
    menuOptions:
    - label: Cone
      name: cone
    - label: Capped Cone
      name: cappedcone
    name: Shape
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Choose between a regular cone and a capped cone without a tip.
  - label: Base Position
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Move the center of the shape.
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The height of the cone.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the base of the cone.
  - label: Top Radius
    name: Radius2
    summary: The radius of the top of the cone, if using a capped cone.
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
    regularHandling: runtime
  - label: Mode
    menuOptions:
    - label: Axis and Height
      name: axis
    - label: Base and Top Points
      name: points
    name: Mode
    readOnlyHandling: baked
    regularHandling: baked
  - label: Top Position
    name: Top
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Defines a cone or capped cone shape.
  thumb: assets/images/reference/operators/sdf/coneSdf_thumb.png
  variables:
  - label: axispos
    name: axispos
  - label: normoffset
    name: normoffset
  - label: normangle
    name: normangle

---


Defines a cone or capped cone shape.