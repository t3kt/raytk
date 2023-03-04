---
layout: operator
title: coneSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/coneSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.coneSdf/
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
    coordTypes:
    - vec3
    label: Height Field
    name: heightField
    returnTypes:
    - float
    summary: Value field that can be used to vary the height of the cone.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius (both base and top) of
      the cone.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec3
    label: Base Position Field
    name: baseField
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
    - vec3
    label: Top Position Field
    name: topField
    returnTypes:
    - vec4
  name: coneSdf
  opType: raytk.operators.sdf.coneSdf
  parameters:
  - name: Enable
  - label: Shape
    menuOptions:
    - label: Cone
      name: cone
    - label: Capped Cone
      name: cappedcone
    name: Shape
    summary: Choose between a regular cone and a capped cone without a tip.
  - label: Base Position
    name: Translate
    summary: Move the center of the shape.
  - label: Height
    name: Height
    summary: The height of the cone.
  - label: Radius
    name: Radius
    summary: The radius of the base of the cone.
  - label: Top Radius
    name: Radius2
    summary: The radius of the top of the cone, if using a capped cone.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Mode
    menuOptions:
    - label: Axis and Height
      name: axis
    - label: Base and Top Points
      name: points
    name: Mode
  - label: Top Position
    name: Top
  summary: Defines a cone or capped cone shape.
  thumb: assets/images/reference/operators/sdf/coneSdf_thumb.png

---


Defines a cone or capped cone shape.