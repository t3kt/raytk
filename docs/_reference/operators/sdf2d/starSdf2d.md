---
layout: operator
title: starSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/starSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.starSdf2d/
op:
  category: sdf2d
  name: starSdf2d
  opType: raytk.operators.sdf2d.starSdf2d
  parameters:
  - label: Radius
    name: Radius
    summary: The distance from the center to each outer point on the star.
  - label: Points
    name: Points
    summary: The number of points for the star. When this is a non-integer value there
      will be one point that is partially cut off at the bottom.
  - label: Tightness
    name: Tightness
    summary: How much the inner points of the start are pulled towards the center.
      At zero this will produce a polygon with two sides for each point. At one it
      will produce thin lines radiating from the center.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Cartesian
      name: cartesian
    - label: Polar
      name: polar
    name: Uvmode
  summary: SDF for a 2D star shape.

---


SDF for a 2D star shape.