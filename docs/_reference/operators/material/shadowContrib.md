---
layout: operator
title: shadowContrib
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/shadowContrib
redirect_from:
  - /reference/opType/raytk.operators.material.shadowContrib/
op:
  category: material
  detail: The shading level will be 1 in areas without a shadow, and 0 in areas that
    are fully in shadow.
  keywords:
  - lighting
  - material
  - modularmat
  - shading
  - shadow
  name: shadowContrib
  opType: raytk.operators.material.shadowContrib
  parameters:
  - label: Use Color
    name: Usecolor
    summary: Whether to multiply the shading level by a color, producing a vector
      field instead of just the shading level.
  - label: Color
    name: Color
  - label: Invert
    name: Invert
    summary: Inverts the shading level, so that 1 is for full shadow and 0 is for
      no shadow.
  status: beta
  summary: A material element that produces the shading level for the surface.

---


A material element that produces the shading level for the surface.

The shading level will be 1 in areas without a shadow, and 0 in areas that are fully in shadow.