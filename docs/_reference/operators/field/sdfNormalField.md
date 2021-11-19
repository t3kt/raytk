---
layout: operator
title: sdfNormalField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/sdfNormalField
redirect_from:
  - /reference/opType/raytk.operators.field.sdfNormalField/
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
    - vec3
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: sdfNormalField
  opType: raytk.operators.field.sdfNormalField
  parameters:
  - label: Enable Normal Smoothing
    name: Enablenormalsmoothing
  - label: Normal Smoothing
    name: Normalsmoothing
  status: beta

---
