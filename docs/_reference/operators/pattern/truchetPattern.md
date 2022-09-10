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
    label: Path Color Field / Custom Color Field
    name: pathColorField
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
    name: curveField
    returnTypes:
    - float
  name: truchetPattern
  opType: raytk.operators.pattern.truchetPattern
  parameters:
  - label: Translate
    name: Translate
  - label: Size
    name: Size
  - label: Curve
    name: Curve
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending
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
  - label: Background Color
    name: Bgcolor
  - label: Seed
    name: Seed
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
