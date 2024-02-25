---
layout: operator
title: hexagonalGridPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalGridPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalGridPattern/
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
    label: Poly Color 1 Field
    name: polyColor1Field
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
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
    label: Poly Color 2 Field
    name: polyColor2Field
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
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
    label: Poly Color 3 Field
    name: polyColor3Field
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
  name: hexagonalGridPattern
  opType: raytk.operators.pattern.hexagonalGridPattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Hex Grid
      name: hexgrid
    - label: Hex Distance
      name: hexdist
    - label: Hex 3 Pattern
      name: hex3
    - label: Hex 3 Color Pattern
      name: hex3color
    name: Pattern
    readOnlyHandling: baked
    regularHandling: baked
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 1
    name: Polycolor1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 2
    name: Polycolor2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 3
    name: Polycolor3
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/hexagonalGridPattern_thumb.png

---
