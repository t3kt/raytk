---
layout: operator
title: capsuleSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/capsuleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.capsuleSdf/
op:
  category: sdf
  detail: With a small `Radius`, this can be used to create a line segment.
  keywords:
  - capsule
  - line
  - points
  - segment
  name: capsuleSdf
  opType: raytk.operators.sdf.capsuleSdf
  parameters:
  - label: Translate
    name: Translate
    summary: Moves the center of the capsule.
  - label: End Point 1
    name: Endpoint1
    summary: Distance of the first end from the center position.
  - label: End Point 2
    name: Endpoint2
    summary: Distance of the second end from the center position.
  - label: Radius
    name: Radius
    summary: The thickness of the capsule.
  summary: A cylinder with rounded ends, between two points.

---


A cylinder with rounded ends, between two points.

With a small `Radius`, this can be used to create a line segment.