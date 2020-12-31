---
layout: operator
title: mengerSpongeSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/mengerSpongeSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.mengerSpongeSdf/
op:
  name: mengerSpongeSdf
  summary: Menger sponge fractal, made of boxes with holes cut through each axis.
  opType: raytk.operators.sdf.mengerSpongeSdf
  category: sdf
  parameters:
    - name: Translate
      label: Translate
      summary: |
        Moves the center of the shape.
    - name: Steps
      label: Steps
      summary: |
        Number of levels of detail.
    - name: Scale
      label: Scale
    - name: Boxscale
      label: Box Scale
      summary: |
        The scale of the boxes used at each step.
    - name: Crossscale
      label: Cross Scale
      summary: |
        The size of the holes cut through the boxes at each step.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# mengerSpongeSdf

Category: sdf



Menger sponge fractal, made of boxes with holes cut through each axis.