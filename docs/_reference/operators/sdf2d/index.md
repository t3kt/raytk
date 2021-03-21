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
  - name: circleSdf
    summary: 2D circle SDF.
  - name: cornerSdf2d
    summary: 2D SDF for an infinite corner, like an infinite square positioned by
      one corner.
  - name: crossSdf2d
    summary: 2D cross shape SDF, with 4 arms and option rounding of the intersections.
  - name: dogBoneSdf2d
    summary: 2D SDF for two connected circles.
  - name: parabolaSdf2d
  - name: pieSdf2d
  - name: polygonSdf2d
  - name: rectangleSdf
  - name: rhombusSdf2d
  - name: roundedRectangleSdf2d
  - name: spiralSdf2d
    status: beta
  - name: starSdf2d
  - name: superQuadSdf2d
  - name: triangleSdf2d
  - name: vesicaSdf2d
  summary: 'Signed distances functions which define geometry in 2D space, by calculating

    the distance from the edge of the shape at any given point.'

---

# Sdf2d Operators

Signed distances functions which define geometry in 2D space, by calculating
the distance from the edge of the shape at any given point.

These operators can be used either in 2D workflows, or can be converted to
3D geometry such as by extrusion.
