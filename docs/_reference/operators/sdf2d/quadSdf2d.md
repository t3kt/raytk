---
layout: operator
title: quadSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/quadSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.quadSdf2d/
op:
  category: sdf2d
  detail: Based on [Sierpinski Fractal Cubes by Shane](https://www.shadertoy.com/view/tldfzX).
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
    label: Point 1-2 Coords Field
    name: points12
    returnTypes:
    - vec4
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Point 3-4 Coords Field
    name: points34
    returnTypes:
    - vec4
  name: quadSdf2d
  opType: raytk.operators.sdf2d.quadSdf2d
  parameters:
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
  - label: Point 3
    name: Point3
  - label: Point 4
    name: Point4
  summary: SDF for a 2D quad with arbitrary corners.
  thumb: assets/images/reference/operators/sdf2d/quadSdf2d_thumb.png

---


SDF for a 2D quad with arbitrary corners.

Based on [Sierpinski Fractal Cubes by Shane](https://www.shadertoy.com/view/tldfzX).