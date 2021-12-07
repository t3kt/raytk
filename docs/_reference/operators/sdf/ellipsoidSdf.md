---
layout: operator
title: ellipsoidSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/ellipsoidSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.ellipsoidSdf/
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
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  keywords:
  - circle
  - ellipse
  - ellipsoid
  - oval
  - sphere
  name: ellipsoidSdf
  opType: raytk.operators.sdf.ellipsoidSdf
  parameters:
  - label: Scale
    name: Scale
  thumb: assets/images/reference/operators/sdf/ellipsoidSdf_thumb.png

---
