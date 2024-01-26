---
layout: operator
title: ringsSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/ringsSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.ringsSdf/
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
    label: Spacing Field
    name: spacingField
    returnTypes:
    - float
    supportedVariables:
    - normangle
    - angle
    - axispos
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
    label: Shift Field
    name: shiftField
    returnTypes:
    - float
    supportedVariableInputs:
    - spacingField
    supportedVariables:
    - normangle
    - angle
    - axispos
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
    - vec2
    label: Cross Section Shape SDF
    name: crossSection
    returnTypes:
    - float
    - Sdf
    supportedVariableInputs:
    - spacingField
    - shiftField
    supportedVariables:
    - normangle
    - angle
    - axispos
    - ring
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
    - spacingField
    - shiftField
    - crossSection
    supportedVariables:
    - normangle
    - angle
    - axispos
    - ring
  name: ringsSdf
  opType: raytk.operators.sdf.ringsSdf
  parameters:
  - label: Plane
    menuOptions:
    - label: YZ
      name: x
    - label: ZX
      name: y
    - label: XY
      name: z
    name: Axis
    summary: Axis that faces the plane where coordinates are mirrored.
  - label: Shape
    menuOptions:
    - label: Circle
      name: circle
    - label: Square
      name: square
    - label: Diamond
      name: diamond
    name: Shape
  - label: Spacing
    name: Spacing
  - label: Offset
    name: Shift
  - label: Thickness
    name: Thickness
  variables:
  - label: angle
    name: angle
  - label: normangle
    name: normangle
  - label: axispos
    name: axispos
  - label: ring
    name: ring

---
