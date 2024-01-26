---
layout: operator
title: lineSeriesSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/lineSeriesSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.lineSeriesSdf/
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
    label: Point A Field
    name: pointAField
    returnTypes:
    - vec4
    supportedVariables:
    - stepindex
    - normstepindex
    - normoffset
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
    label: Point B Field
    name: pointBField
    returnTypes:
    - vec4
    supportedVariables:
    - stepindex
    - normstepindex
    - normoffset
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
    supportedVariables:
    - stepindex
    - normstepindex
    - normoffset
  name: lineSeriesSdf
  opType: raytk.operators.sdf.lineSeriesSdf
  parameters:
  - label: Source
    menuOptions:
    - label: Parameters
      name: params
    - label: CHOPs
      name: chops
    - label: Fields
      name: fields
    name: Source
  - label: Count
    name: Count
  - label: Thickness
    name: Thickness
  - label: Point A CHOP
    name: Pointachop
  - label: Point B CHOP
    name: Pointbchop
  - label: Point A 1
    name: Pointa1
  - label: Point B 1
    name: Pointb1
  - label: Point A 2
    name: Pointa2
  - label: Point B 2
    name: Pointb2
  - label: Point A 3
    name: Pointa3
  - label: Point B 3
    name: Pointb3
  - label: Point A 4
    name: Pointa4
  - label: Point B 4
    name: Pointb4
  - label: Point A 5
    name: Pointa5
  - label: Point B 5
    name: Pointb5
  - label: Point A 6
    name: Pointa6
  - label: Point B 6
    name: Pointb6
  - label: Point A 7
    name: Pointa7
  - label: Point B 7
    name: Pointb7
  - label: Point A 8
    name: Pointa8
  - label: Point B 8
    name: Pointb8
  status: beta
  thumb: assets/images/reference/operators/sdf/lineSeriesSdf_thumb.png
  variables:
  - label: stepindex
    name: stepindex
  - label: normstepindex
    name: normstepindex
  - label: normoffset
    name: normoffset

---
