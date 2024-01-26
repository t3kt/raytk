---
layout: operator
title: gridPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/gridPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.gridPattern/
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
    label: Spacing Field
    name: spacingField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
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
    - spacingField
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
    - spacingField
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
    - vec2
    - vec3
    label: Fill Color Field
    name: fillColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - spacingField
    - thicknessField
    - blendingField
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
    label: Edge Color Field
    name: edgeColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - spacingField
    - thicknessField
    - blendingField
    - fillColorField
  name: gridPattern
  opType: raytk.operators.pattern.gridPattern
  parameters:
  - label: Format
    menuOptions:
    - label: Grid Edges
      name: edge
    - label: Grid Distance
      name: dist
    - label: Grid Normalized Distance
      name: normdist
    - label: Grid Color
      name: color
    name: Format
  - label: Translate
    name: Translate
  - label: Spacing
    name: Spacing
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending
  - label: Fill Color
    name: Fillcolor
  - label: Edge Color
    name: Edgecolor
  status: beta
  summary: Rectangular grid pattern.
  thumb: assets/images/reference/operators/pattern/gridPattern_thumb.png

---


Rectangular grid pattern.