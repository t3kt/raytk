---
layout: operator
title: cellTileField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/cellTileField
redirect_from:
  - /reference/opType/raytk.operators.field.cellTileField/
op:
  category: field
  detail: 'Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).

    Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable
    by ensuring the objects wrap around the edges.

    It isn''t perfect but it is low cost.'
  name: cellTileField
  opType: raytk.operators.field.cellTileField
  parameters:
  - label: Translate
    name: Translate
  - label: Scale
    name: Scale
  - label: Cell Style
    menuOptions:
    - label: Beveled Voronoi
      name: beveledvoronoi
    - label: Cellular
      name: cellular
    - label: Raw
      name: raw
    name: Cellstyle
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 1D
      name: float
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  summary: A value field that provides an approximation of repeating cellular (voronoi)
    noise.
  thumb: assets/images/reference/operators/field/cellTileField_thumb.png

---


A value field that provides an approximation of repeating cellular (voronoi) noise.

Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).
Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable by ensuring the objects wrap around the edges.
It isn't perfect but it is low cost.