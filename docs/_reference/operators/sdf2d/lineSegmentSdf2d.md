---
layout: operator
title: lineSegmentSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/lineSegmentSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.lineSegmentSdf2d/
op:
  category: sdf2d
  detail: 'The line segment is defined by two points.

    By default those come from the "Point A" and "Point B" parameters.

    But if the "Points Field" input is connected, it will use that to get the points
    instead.'
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
    label: Point Coords Field
    name: points
    returnTypes:
    - vec4
    summary: If connected, this field will be used to pick both points. The first
      point comes from the X and Y components of the vector that comes out of the
      field, and the second point will use the Z and W components.
  name: lineSegmentSdf2d
  opType: raytk.operators.sdf2d.lineSegmentSdf2d
  parameters:
  - label: Point A
    name: Pointa
  - label: Point B
    name: Pointb
  summary: 2D line segment SDF.

---


2D line segment SDF.

The line segment is defined by two points.
By default those come from the "Point A" and "Point B" parameters.
But if the "Points Field" input is connected, it will use that to get the points instead.