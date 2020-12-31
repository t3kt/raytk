---
layout: operator
title: capsuleSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/capsuleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.capsuleSdf/
op:
  name: capsuleSdf
  summary: A cylinder with rounded ends, between two points.
  detail: |
    With a small `Radius`, this can be used to create a line segment.
  opType: raytk.operators.sdf.capsuleSdf
  category: sdf
  parameters:
    - name: Translate
      label: Translate
      summary: |
        Moves the center of the capsule.
    - name: Endpoint1
      label: End Point 1
      summary: |
        Distance of the first end from the center position.
    - name: Endpoint2
      label: End Point 2
      summary: |
        Distance of the second end from the center position.
    - name: Radius
      label: Radius
      summary: |
        The thickness of the capsule.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# capsuleSdf

Category: sdf



A cylinder with rounded ends, between two points.

With a small `Radius`, this can be used to create a line segment.