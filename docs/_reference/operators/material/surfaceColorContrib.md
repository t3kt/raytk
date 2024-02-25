---
layout: operator
title: surfaceColorContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/surfaceColorContrib
redirect_from:
  - /reference/opType/raytk.operators.material.surfaceColorContrib/
op:
  category: material
  detail: If no color attribute has been assigned to the surface, this will use the
    `Default Color` instead.
  keywords:
  - color
  - material
  - modularmat
  - surface
  name: surfaceColorContrib
  opType: raytk.operators.material.surfaceColorContrib
  parameters:
  - label: Default Color
    name: Defaultcolor
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Color used if there is no color assigned to the surface.
  summary: A material element that produces the assigned color attribute for the surface.

---


A material element that produces the assigned color attribute for the surface.

If no color attribute has been assigned to the surface, this will use the `Default Color` instead.