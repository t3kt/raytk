---
layout: operatorCategory
title: Sdf2d Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/sdf2d/
cat:
  name: sdf2d
  summary: |
    Signed distances functions which define geometry in 2D space, by calculating
    the distance from the edge of the shape at any given point.
  detail: |
    These operators can be used either in 2D workflows, or can be converted to
    3D geometry such as by extrusion.
  operators:
    - op:
      name: circleSdf
    - op:
      name: crossSdf2d
      summary: 2D cross shape SDF, with 4 arms and option rounding of the intersections.
    - op:
      name: parabolaSdf2d
    - op:
      name: pieSdf2d
    - op:
      name: polygonSdf2d
    - op:
      name: rectangleSdf
    - op:
      name: rhombusSdf2d
    - op:
      name: roundedRectangleSdf2d
    - op:
      name: starSdf2d
    - op:
      name: superQuadSdf2d
    - op:
      name: triangleSdf2d
    - op:
      name: vesicaSdf2d

---

# Sdf2d Operators

Signed distances functions which define geometry in 2D space, by calculating
the distance from the edge of the shape at any given point.

These operators can be used either in 2D workflows, or can be converted to
3D geometry such as by extrusion.
