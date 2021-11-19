---
layout: operator
title: bezierSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/bezierSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.bezierSdf/
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
    - float
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  name: bezierSdf
  opType: raytk.operators.sdf.bezierSdf
  parameters:
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
  - label: Point 3
    name: Point3
  - label: Radius Start
    name: Radiusstart
  - label: Radius End
    name: Radiusend
  status: beta

---
