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
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending
  - label: Poly Color 1
    name: Polycolor1
  - label: Poly Color 2
    name: Polycolor2
  - label: Poly Color 3
    name: Polycolor3
  thumb: assets/images/reference/operators/pattern/hexagonalGridPattern_thumb.png

---
