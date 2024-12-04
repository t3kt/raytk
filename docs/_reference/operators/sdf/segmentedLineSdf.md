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
    readOnlyHandling: baked
    regularHandling: baked
    summary: Where to get the point positions.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The thickness of the line segments.
  - label: Segments
    name: Segments
    readOnlyHandling: baked
    regularHandling: baked
    summary: The number of line segments. This controls how many parameters or CHOP
      samples are used.
  - label: Close Path
    name: Closepath
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to add a line segment connecting the first and last points.
  - label: Points
    name: Points
    summary: CHOP used for point positions, using the `tx`, `ty`, and `tz` channels
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 3
    name: Point3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 4
    name: Point4
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 5
    name: Point5
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 6
    name: Point6
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 7
    name: Point7
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 8
    name: Point8
    readOnlyHandling: baked
    regularHandling: runtime
  summary: Multi-segment line SDF.
  thumb: assets/images/reference/operators/sdf/segmentedLineSdf_thumb.png
  variables:
  - label: Segment Index
    name: stepindex
  - label: Normalized Segment Index
    name: normstepindex
  - label: Interpolated Segment Index
    name: stepinterp
  - label: Normalized Distance Offset
    name: normoffset
  - label: Distance Offset
    name: offset

---


Multi-segment line SDF.

The line is defined my a list of points, which are either defined by parameters or by CHOP channels.