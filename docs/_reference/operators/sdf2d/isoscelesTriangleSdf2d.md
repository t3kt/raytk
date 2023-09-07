---
layout: operator
title: isoscelesTriangleSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/isoscelesTriangleSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.isoscelesTriangleSdf2d/
op:
  category: sdf2d
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
    label: Height Field
    name: heightField
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
    label: Width Field
    name: widthField
    returnTypes:
    - float
  name: isoscelesTriangleSdf2d
  opType: raytk.operators.sdf2d.isoscelesTriangleSdf2d
  parameters:
  - label: Direction
    menuOptions:
    - label: Right (X+)
      name: xpos
    - label: Left (X-)
      name: xneg
    - label: Up (Y+)
      name: ypos
    - label: Down (Y-)
      name: yneg
    name: Direction
  - label: Position Mode
    menuOptions:
    - label: Base Centered
      name: base
    - label: Tip Centered
      name: tip
    name: Positionmode
  - label: Height
    name: Height
    summary: The distance from the base of an iscosceles triangle to the opposite
      tip.
  - label: Width
    name: Width
    summary: The width of the base of an isosceles triangle.
  thumb: assets/images/reference/operators/sdf2d/isoscelesTriangleSdf2d_thumb.png

---
