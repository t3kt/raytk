---
layout: operator
title: sdfField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/sdfField
redirect_from:
  - /reference/opType/raytk.operators.field.sdfField/
op:
  category: field
  detail: This can be used to apply effects only within certain shaped areas of space.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - float
    - Sdf
  name: sdfField
  opType: raytk.operators.field.sdfField
  parameters:
  - label: Field Type
    menuOptions:
    - label: Distance
      name: dist
    - label: Inside
      name: inside
    - label: Outside
      name: outside
    - label: Surface
      name: surface
    - label: Surface Inside
      name: surfaceinside
    - label: Surface Outside
      name: surfaceoutside
    - label: Surface Primary UV
      name: uv
    - label: Surface Secondary UV
      name: uv2
    name: Fieldtype
  - label: Offset
    name: Offset
    summary: Offsets the surface of the shape. Positive values expand the shape and
      negative values contract it. This is equivalent to the `round` operator.
  - label: Thickness
    name: Thickness
    summary: For surface-based fields, this is the thickness of the area where the
      value is 1.
  - label: Blending
    name: Blending
    summary: The distance over which the 1 area transitions to the 0 area.
  summary: Value field based on an SDF shape.
  thumb: assets/images/reference/operators/field/sdfField_thumb.png

---


Value field based on an SDF shape.

This can be used to apply effects only within certain shaped areas of space.