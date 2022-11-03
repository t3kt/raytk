---
layout: operator
title: hilbertCurveTransform
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/hilbertCurveTransform
redirect_from:
  - /reference/opType/raytk.operators.filter.hilbertCurveTransform/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Ray
    - Light
    - Particle
  name: hilbertCurveTransform
  opType: raytk.operators.filter.hilbertCurveTransform
  parameters:
  - label: Enable
    name: Enable
  - label: Steps
    name: Steps
  - label: Offset
    name: Offset
  status: beta
  thumb: assets/images/reference/operators/filter/hilbertCurveTransform_thumb.png
  variables:
  - label: localuv
    name: localuv
  - label: cell
    name: cell
  - label: localcell
    name: localcell

---
