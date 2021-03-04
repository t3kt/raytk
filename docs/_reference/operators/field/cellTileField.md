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
  - label: Context Type
    menuOptions:
    - label: None
      name: none
    - label: Context
      name: Context
    - label: Material Context
      name: MaterialContext
    - label: Camera Context
      name: CameraContext
    - label: Light Context
      name: LightContext
    name: Contexttype
  summary: A value field that provides an approximation of repeating cellular (voronoi)
    noise.

---


A value field that provides an approximation of repeating cellular (voronoi) noise.

Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).
Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable by ensuring the objects wrap around the edges.
It isn't perfect but it is low cost.