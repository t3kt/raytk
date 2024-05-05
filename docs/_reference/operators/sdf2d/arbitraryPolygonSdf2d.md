---
layout: operator
title: arbitraryPolygonSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/arbitraryPolygonSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.arbitraryPolygonSdf2d/
op:
  category: sdf2d
  detail: 'Points can either be specified with parameters or by passing in a CHOP.


    If a CHOP is used, only the first N samples are used where N is the Max Points
    parameter. The first two channels of the CHOP are used for the X and Y, regardless
    of their names.'
  name: arbitraryPolygonSdf2d
  opType: raytk.operators.sdf2d.arbitraryPolygonSdf2d
  parameters:
  - label: Source
    menuOptions:
    - label: Parameters
      name: params
    - label: CHOP
      name: chop
    name: Source
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to specify points using parameters or a CHOP input.
  - label: Points
    name: Pointcount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Number of points.
  - label: Points CHOP
    name: Pointschop
    summary: CHOP used for point positions.
  - label: Max Points
    name: Maxpointcount
    summary: Maximum number of points allowed in the provided CHOP.
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
  summary: Polygonal area with arbitrarily positioned points.
  thumb: assets/images/reference/operators/sdf2d/arbitraryPolygonSdf2d_thumb.png

---


Polygonal area with arbitrarily positioned points.

Points can either be specified with parameters or by passing in a CHOP.

If a CHOP is used, only the first N samples are used where N is the Max Points parameter. The first two channels of the CHOP are used for the X and Y, regardless of their names.