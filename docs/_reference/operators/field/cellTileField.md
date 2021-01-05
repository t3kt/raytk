---
layout: operator
title: cellTileField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/cellTileField
redirect_from:
  - /reference/opType/raytk.operators.field.cellTileField/
op:
  name: cellTileField
  summary: A value field that provides an approximation of repeating cellular (voronoi) noise.
  detail: |
    Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).
    Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable by ensuring the objects wrap around the edges.
    It isn't perfect but it is low cost.
  opType: raytk.operators.field.cellTileField
  category: field
  parameters:
    - name: Translate
      label: Translate
    - name: Scale
      label: Scale
    - name: Cellstyle
      label: Cell Style
      menuOptions:
        - name: beveledvoronoi
          label: Beveled Voronoi
        - name: cellular
          label: Cellular
        - name: raw
          label: Raw
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# cellTileField

Category: field



A value field that provides an approximation of repeating cellular (voronoi) noise.

Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).
Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable by ensuring the objects wrap around the edges.
It isn't perfect but it is low cost.