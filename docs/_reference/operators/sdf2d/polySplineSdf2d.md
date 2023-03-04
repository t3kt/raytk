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
    summary: Where to get the point positions.
  - label: Radius
    name: Radius
    summary: The thickness of the line segments.
  - label: Segments
    name: Segments
    summary: The number of line segments. This controls how many parameters or CHOP
      samples are used.
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
  status: beta
  thumb: assets/images/reference/operators/sdf2d/polySplineSdf2d_thumb.png

---
