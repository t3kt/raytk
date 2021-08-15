---
layout: operator
title: superQuadSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/superQuadSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.superQuadSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    label: Exponent Field
    name: exponent_definition_in
    returnTypes:
    - float
  name: superQuadSdf2d
  opType: raytk.operators.sdf2d.superQuadSdf2d
  parameters:
  - label: Radius
    name: Radius
  - label: Exponent
    name: Exponent

---
