---
layout: operator
title: cornerSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/cornerSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.cornerSdf2d/
op:
  category: sdf2d
  name: cornerSdf2d
  opType: raytk.operators.sdf2d.cornerSdf2d
  parameters:
  - label: Corner
    menuOptions:
    - label: Bottom Left
      name: bottomleft
    - label: Top Left
      name: topleft
    - label: Bottom Right
      name: bottomright
    - label: Top Right
      name: topright
    name: Corner
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Which corner of the infinite square to place at the origin.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the position of the corner.
  summary: 2D SDF for an infinite corner, like an infinite square positioned by one
    corner.
  thumb: assets/images/reference/operators/sdf2d/cornerSdf2d_thumb.png

---


2D SDF for an infinite corner, like an infinite square positioned by one corner.