---
layout: operator
title: polarVectorField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/polarVectorField
redirect_from:
  - /reference/opType/raytk.operators.field.polarVectorField/
op:
  category: field
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
    label: theta_field_in
    name: thetaField
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
    - vec3
    label: phi_field_in
    name: phiField
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
    label: length_field_in
    name: lengthField
    returnTypes:
    - float
  name: polarVectorField
  opType: raytk.operators.field.polarVectorField
  parameters:
  - label: Theta Offset
    name: Thetaoffset
  - label: Phi Offset
    name: Phioffset
  - label: Length
    name: Length

---
