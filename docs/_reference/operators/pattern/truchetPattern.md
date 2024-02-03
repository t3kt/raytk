---
layout: operator
title: truchetPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/truchetPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.truchetPattern/
op:
  category: pattern
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
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    supportedVariables:
    - cell
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
    - vec3
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - thicknessField
    supportedVariables:
    - cell
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
    - vec3
    label: Curve Field
    name: curveField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    supportedVariables:
    - cell
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
    - vec3
    label: Path Color Field / Custom Color Field
    name: pathColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - curveField
    supportedVariables:
    - cell
    - edgedist
    - contour
    - depth
    - normangle
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
    - vec3
    label: Background Color Field
    name: bgColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - curveField
    - pathColorField
    supportedVariables:
    - cell
    - edgedist
    - contour
    - depth
    - normangle
  name: truchetPattern
  opType: raytk.operators.pattern.truchetPattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Curve
    name: Curve
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Format
    menuOptions:
    - label: Contour
      name: contour
    - label: Edge Distance
      name: edgedist
    - label: Color & Depth
      name: colordepth
    - label: Color & Depth * Contour
      name: colordepthcontour
    - label: Custom Override Color
      name: customcolor
    name: Format
  - label: Path Color
    name: Pathcolor
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Background Color
    name: Bgcolor
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Seed
    name: Seed
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/pattern/truchetPattern_thumb.png
  variables:
  - label: cell
    name: cell
  - label: contour
    name: contour
  - label: normangle
    name: normangle
  - label: depth
    name: depth
  - label: edgedist
    name: edgedist

---
