---
layout: operator
title: tilingPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/tilingPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.tilingPattern/
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
    coordTypes:
    - vec2
    - vec3
    label: Vertex Radius Field
    name: vertexRadiusField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    - vec3
    label: Outline Thickness Field
    name: outlineThicknessField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
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
    coordTypes:
    - vec2
    - vec3
    label: Poly Color 3 Field
    name: polyColor3Field
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
    coordTypes:
    - vec2
    - vec3
    label: Outline Color Field
    name: outlineColorField
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
    coordTypes:
    - vec2
    - vec3
    label: Dual Outline Color Field
    name: dualOutlineColorField
    returnTypes:
    - float
    - vec4
  name: tilingPattern
  opType: raytk.operators.pattern.tilingPattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Rhombitrihexagonal
      name: rhombitrihexagonal
    - label: Truncated Square
      name: truncatedsquare
    - label: Hexagonal
      name: hexagonal
    - label: Trihexagonal
      name: trihexagonal
    - label: Truncated Hexagonal
      name: truncatedhexagonal
    - label: Triangular
      name: triangular
    - label: Square
      name: square
    - label: Truncated Trihexagonal
      name: truncatedtrihexagonal
    - label: Snub Trihexagonal
      name: snubtrihexagonal
    - label: Snub Square
      name: snubsquare
    name: Pattern
  - label: Format
    menuOptions:
    - label: Poly Color
      name: polycolor
    - label: Dual Tiling Poly Color
      name: dualpolycolor
    - label: Poly Number, Refl Side, Outline
      name: polyreflline
    name: Format
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Vertex Radius
    name: Vertexradius
  - label: Outline Thickness
    name: Outlinethickness
  - label: Outline Blending
    name: Outlineblending
  - label: Poly Color 1
    name: Polycolor1
  - label: Poly Color 2
    name: Polycolor2
  - label: Poly Color 3
    name: Polycolor3
  - label: Outline Color
    name: Outlinecolor
  - label: Dual Outline Color
    name: Dualoutlinecolor
  status: beta

---
