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
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Point 1 Field
    name: point1
    returnTypes:
    - vec4
    summary: If connected, this field will be used to pick both points. The first
      point comes from the X and Y components of the vector that comes out of the
      field, and the second point will use the Z and W components.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Point 2 Field
    name: point2
    returnTypes:
    - vec4
    supportedVariableInputs:
    - point1Field
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - point1Field
    - point2Field
    supportedVariables:
    - normoffset
  name: lineSegmentSdf2d
  opType: raytk.operators.sdf2d.lineSegmentSdf2d
  parameters:
  - label: Point 1
    name: Pointa
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Pointb
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  summary: 2D line segment SDF.
  thumb: assets/images/reference/operators/sdf2d/lineSegmentSdf2d_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf2d_lineSegmentSdf2d_normoffset
    name: RTK_raytk_operators_sdf2d_lineSegmentSdf2d_normoffset

---


2D line segment SDF.

The line segment is defined by two points.
By default those come from the "Point A" and "Point B" parameters.
But if the "Points Field" input is connected, it will use that to get the points instead.