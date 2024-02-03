---
layout: operator
title: polySplineSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/polySplineSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.polySplineSdf2d/
op:
  category: sdf2d
  name: polySplineSdf2d
  opType: raytk.operators.sdf2d.polySplineSdf2d
  parameters:
  - label: Source
    menuOptions:
    - label: Parameters
      name: params
    - label: CHOP
      name: chop
    name: Source
    readOnlyHandling: macro
    regularHandling: macro
    summary: Where to get the point positions.
  - label: Radius
    name: Radius
    readOnlyHandling: macro
    regularHandling: runtime
    summary: The thickness of the line segments.
  - label: Segments
    name: Segments
    readOnlyHandling: macro
    regularHandling: macro
    summary: The number of line segments. This controls how many parameters or CHOP
      samples are used.
  - label: Points
    name: Points
    summary: CHOP used for point positions, using the `tx`, `ty`, and `tz` channels
  - label: Point 1
    name: Point1
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 3
    name: Point3
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 4
    name: Point4
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 5
    name: Point5
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 6
    name: Point6
    readOnlyHandling: macro
    regularHandling: runtime
  - label: Point 7
    name: Point7
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/sdf2d/polySplineSdf2d_thumb.png

---
