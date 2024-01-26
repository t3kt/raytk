---
layout: operator
title: segmentedLineSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/segmentedLineSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.segmentedLineSdf/
op:
  category: sdf
  detail: The line is defined my a list of points, which are either defined by parameters
    or by CHOP channels.
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
    - float
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariables:
    - stepindex
    - normstepindex
    - stepinterp
    - normoffset
    - offset
  keywords:
  - line
  - path
  - points
  - segments
  name: segmentedLineSdf
  opType: raytk.operators.sdf.segmentedLineSdf
  parameters:
  - label: Source
    menuOptions:
    - description: Points are based on the `Point 1, etc parameters.
      label: Parameters
      name: params
    - description: The points are based on the `Points CHOP`.
      label: CHOP
      name: chop
    name: Source
    summary: Where to get the point positions.
  - label: Radius
    name: Radius
    summary: The thickness of the line segments.
  - label: Segments
    name: Segments
    summary: The number of line segments. This controls how many parameters or CHOP
      samples are used.
  - label: Close Path
    name: Closepath
    summary: Whether to add a line segment connecting the first and last points.
  - label: Points
    name: Points
    summary: CHOP used for point positions, using the `tx`, `ty`, and `tz` channels
  - label: Point 1
    name: Point1
  - label: Point 2
    name: Point2
  - label: Point 3
    name: Point3
  - label: Point 4
    name: Point4
  - label: Point 5
    name: Point5
  - label: Point 6
    name: Point6
  - label: Point 7
    name: Point7
  - label: Point 8
    name: Point8
  summary: Multi-segment line SDF.
  thumb: assets/images/reference/operators/sdf/segmentedLineSdf_thumb.png
  variables:
  - label: stepindex
    name: stepindex
  - label: normstepindex
    name: normstepindex
  - label: stepinterp
    name: stepinterp
  - label: normoffset
    name: normoffset
  - label: offset
    name: offset

---


Multi-segment line SDF.

The line is defined my a list of points, which are either defined by parameters or by CHOP channels.