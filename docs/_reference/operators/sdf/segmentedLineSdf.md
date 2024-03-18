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
    - RTK_raytk_operators_sdf_segmentedLineSdf_stepindex
    - RTK_raytk_operators_sdf_segmentedLineSdf_normstepindex
    - RTK_raytk_operators_sdf_segmentedLineSdf_stepinterp
    - RTK_raytk_operators_sdf_segmentedLineSdf_normoffset
    - RTK_raytk_operators_sdf_segmentedLineSdf_offset
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
  - label: RTK_raytk_operators_sdf_segmentedLineSdf_stepindex
    name: RTK_raytk_operators_sdf_segmentedLineSdf_stepindex
  - label: RTK_raytk_operators_sdf_segmentedLineSdf_normstepindex
    name: RTK_raytk_operators_sdf_segmentedLineSdf_normstepindex
  - label: RTK_raytk_operators_sdf_segmentedLineSdf_stepinterp
    name: RTK_raytk_operators_sdf_segmentedLineSdf_stepinterp
  - label: RTK_raytk_operators_sdf_segmentedLineSdf_normoffset
    name: RTK_raytk_operators_sdf_segmentedLineSdf_normoffset
  - label: RTK_raytk_operators_sdf_segmentedLineSdf_offset
    name: RTK_raytk_operators_sdf_segmentedLineSdf_offset

---


Multi-segment line SDF.

The line is defined my a list of points, which are either defined by parameters or by CHOP channels.