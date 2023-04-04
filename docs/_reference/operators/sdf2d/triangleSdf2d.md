---
layout: operator
title: triangleSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/triangleSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.triangleSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    coordTypes:
    - vec2
    label: Height/Width Field
    name: sizeField
    returnTypes:
    - float
  name: triangleSdf2d
  opType: raytk.operators.sdf2d.triangleSdf2d
  parameters:
  - label: Shape
    menuOptions:
    - description: An equilateral triangle (all sides are the same). This is defined
        based on `Radius`. The triangle is centered around the origin.
      label: Equilateral Triangle
      name: equilateral
    - description: An iscosceles triangle (2 sides are the same). This is defined
        based on `Width` and `Height`. The tip of the triangle is placed at the origin.
      label: Isosceles Triangle
      name: isosceles
    - label: Inverted Isosceles Triangle
      name: invertisosceles
    - description: An arbitrary triangle based on 3 points.
      label: Abritrary Triangle
      name: arbitrary
    name: Shape
    summary: Which type of triangle to produce. The types are defined by different
      sets of parameters.
  - label: Radius
    name: Radius
    summary: The distance from the center to each corner of the triangle. Used for
      equilateral triangles.
  - label: Height
    name: Height
    summary: The distance from the base of an iscosceles triangle to the opposite
      tip.
  - label: Width
    name: Width
    summary: The width of the base of an isosceles triangle.
  - label: Point 1
    name: Point1
    summary: The first corner position, for an arbitrary triangle.
  - label: Point 2
    name: Point2
    summary: The second corner position, for an arbitrary triangle.
  - label: Point 3
    name: Point3
    summary: The third corner position, for an arbitrary triangle.
  - label: Direction
    menuOptions:
    - label: Right (X+)
      name: xpos
    - label: Left (X-)
      name: xneg
    - label: Up (Y+)
      name: ypos
    - label: Down (Y-)
      name: yneg
    name: Direction
  summary: SDF for a 2D triangle.
  thumb: assets/images/reference/operators/sdf2d/triangleSdf2d_thumb.png

---


SDF for a 2D triangle.