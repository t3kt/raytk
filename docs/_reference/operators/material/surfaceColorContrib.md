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
  name: surfaceColorContrib
  opType: raytk.operators.material.surfaceColorContrib
  parameters:
  - label: Default Color
    name: Defaultcolor
    summary: Color used if there is no color assigned to the surface.
  status: beta
  summary: A material element that produces the assigned color attribute for the surface.

---


A material element that produces the assigned color attribute for the surface.

If no color attribute has been assigned to the surface, this will use the `Default Color` instead.