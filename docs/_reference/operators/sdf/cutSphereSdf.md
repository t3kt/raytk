---
layout: operator
title: cutSphereSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/cutSphereSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.cutSphereSdf/
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
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
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
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - thicknessField
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
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - radiusField
    - thicknessField
    - offsetField
  name: cutSphereSdf
  opType: raytk.operators.sdf.cutSphereSdf
  parameters:
  - label: Shape
    menuOptions:
    - label: Solid
      name: solid
    - label: Hollow
      name: hollow
    name: Shape
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Cut Offset
    name: Offset
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Thickness
    name: Thickness
  - label: Rotate
    name: Rotate
    readOnlyHandling: macro
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf/cutSphereSdf_thumb.png

---
