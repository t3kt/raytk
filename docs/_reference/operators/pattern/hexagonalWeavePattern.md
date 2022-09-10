---
layout: operator
title: hexagonalWeavePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalWeavePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalWeavePattern/
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
    coordTypes:
    - vec2
    - vec3
    label: Color 1 Field / Replacement Color
    name: color1Field
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
    label: Color 2 Field
    name: color2Field
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
    label: Background Color Field
    name: bgColorField
    returnTypes:
    - float
    - vec4
  name: hexagonalWeavePattern
  opType: raytk.operators.pattern.hexagonalWeavePattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Two Layer
      name: twolayer
    name: Pattern
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending
  - label: Randomize
    name: Randomize
  - label: Seed
    name: Seed
  - label: Format
    menuOptions:
    - label: Color
      name: color
    - label: Custom Override Color
      name: customcolor
    name: Format
  - label: Color 1
    name: Color1
  - label: Color 2
    name: Color2
  - label: Background Color
    name: Bgcolor
  thumb: assets/images/reference/operators/pattern/hexagonalWeavePattern_thumb.png
  variables:
  - label: axialdist
    name: axialdist
  - label: mask
    name: mask

---
