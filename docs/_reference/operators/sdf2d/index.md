---
layout: operatorCategory
title: Sdf2d Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/sdf2d/
cat:
  detail: 'These operators can be used either in 2D workflows, or can be converted
    to

    3D geometry such as by extrusion.'
  name: sdf2d
  operators:
  - name: arcSdf2d
  - name: arrowSdf2d
  - keywords:
    - bezier
    - curve
    - line
    name: bezierSdf2d
    status: beta
  - name: blobbyCrossSdf2d
  - name: circleSdf
    summary: 2D circle SDF.
  - name: cornerSdf2d
    summary: 2D SDF for an infinite corner, like an infinite square positioned by
      one corner.
  - name: crossSdf2d
    summary: 2D cross shape SDF, with 4 arms and option rounding of the intersections.
  - name: dogBoneSdf2d
    summary: 2D SDF for two connected circles.
  - keywords:
    - circle
    - ellipse
    - oval
    name: ellipseSdf2d
  - name: flowerSdf2d
  - name: heartSdf2d
  - name: horseshoeSdf2d
  - name: jointSdf2d
    status: beta
  - name: lineSegmentSdf2d
    summary: 2D line segment SDF.
  - name: parabolaSdf2d
  - name: parallelogramSdf2d
  - name: pieSdf2d
    summary: SDF for a 2D pie-slice shape.
  - name: planeSdf2d
  - name: polygonSdf2d
    summary: SDF for several types of 2D polygons.
  - name: quadSdf2d
    summary: SDF for a 2D quad with arbitrary corners.
  - name: rectangleSdf
    summary: SDF for a 2D rectangle.
  - name: rhombusSdf2d
    summary: SDF for a 2D rhombus (diamond), with its corners aligned to the axes.
  - name: roundedRectangleSdf2d
    summary: SDF for a 2D rectangle with optionally rounded corners.
  - name: spikeSdf2d
  - name: spiralSdf2d
    status: beta
  - name: starSdf2d
    summary: SDF for a 2D star shape.
  - name: superQuadSdf2d
  - name: trapezoidSdf2d
  - name: triangleSdf2d
    summary: SDF for a 2D triangle.
  - name: vesicaSdf2d
    summary: SDF for a 2d vesica, which is a shape based on the overlap between two
      circles.
  - name: wedgeSdf2d
    status: beta
  summary: 'Signed distances functions which define geometry in 2D space, by calculating

    the distance from the edge of the shape at any given point.'

---

# Sdf2d Operators

Signed distances functions which define geometry in 2D space, by calculating
the distance from the edge of the shape at any given point.

These operators can be used either in 2D workflows, or can be converted to
3D geometry such as by extrusion.
