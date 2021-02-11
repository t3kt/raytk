---
layout: operator
title: instance
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/instance
redirect_from:
  - /reference/opType/raytk.operators.filter.instance/
op:
  category: filter
  inputs:
  - contextTypes:
    - none
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - float
    - vec2
    - vec3
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: instance
  opType: raytk.operators.filter.instance
  parameters:
  - label: Enable
    name: Enable
  - label: Instance Count
    name: Instancecount
  - label: Combine
    menuOptions:
    - label: Simple Union
      name: simpleUnion
    - label: Simple Intersect
      name: simpleIntersect
    - label: Simple Difference
      name: simpleDiff
    - label: Smooth Union
      name: smoothUnion
    - label: Smooth Intersect
      name: smoothIntersect
    - label: Smooth Difference
      name: smoothDiff
    - label: Round Union
      name: roundUnion
    - label: Round Intersect
      name: roundIntersect
    - label: Round Difference
      name: roundDiff
    - label: Chamfer Union
      name: chamferUnion
    - label: Chamfer Intersect
      name: chamferIntersect
    - label: Chamfer Difference
      name: chamferDiff
    name: Combine
  - label: Radius
    name: Radius
  status: beta

---

# instance

Category: filter

