---
layout: operator
title: flowerSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/flowerSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.flowerSdf2d/
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
    label: Radius Field
    name: radiusField
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
    label: Amplitude Field
    name: amplitudeField
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
    label: Petals Field
    name: petalsField
    returnTypes:
    - float
  name: flowerSdf2d
  opType: raytk.operators.sdf2d.flowerSdf2d
  parameters:
  - label: Radius
    name: Radius
  - label: Amplitude
    name: Amplitude
  - label: Petals
    name: Petals
  - label: Normalized Angle (0..1)
    name: Createrefnormangle
    summary: 'Create reference to variable: Normalized Angle (0..1)'
  thumb: assets/images/reference/operators/sdf2d/flowerSdf2d_thumb.png

---
