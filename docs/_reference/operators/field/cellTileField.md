---
layout: page
title: cellTileField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/cellTileField
---

# cellTileField

Category: field



A value field that provides an approximation of repeating cellular (voronoi) noise.

Based on Biomine by Shane (https://www.shadertoy.com/view/4lyGzR).
Uses a minimum blend at various 3D locations on a cubic tile. Make the tile wrappable by ensuring the objects wrap around the edges.
It isn't perfect but it is low cost.

## Parameters

* `Translate` *Translate*
* `Scale` *Scale*
* `Cellstyle` *Cell Style*
  * `beveledvoronoi` *Beveled Voronoi*
  * `cellular` *Cellular*
  * `raw` *Raw*
* `Contexttype` *Context Type*
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
* `Inspect` *Inspect*