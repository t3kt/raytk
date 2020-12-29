---
layout: page
title: splitCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/splitCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.splitCamera/
---

# splitCamera

Category: camera



A camera that splits the viewport into several zones, each using a separate camera.

Important note that when the horizontal and vertical layouts currently only use the first two inputs.

## Parameters

* `Enable` *Enable*
* `Layout` *Layout*: How to arrange the zones.
  * `horz` *Horizontal*: Output is split into two horizontal slices. When using this layout, only the first two inputs are used.
  * `vert` *Vertical*: Output is split into two vertical slices. When using this layout, only the first two inputs are used.
  * `grid` *Grid*: Output is arranged in a 2x2 grid.
* `Rescale` *Rescale*: Whether to rescale each camera to fit each zone. When switched off, if using a grid, you will only see the top right corner of the first camera, the top left of the second, etc. When switched on, you see the full view that each camera would normally get.
* `Inspect`
* `Help` *Help*

## Inputs

* `definition_in_1` *Camera Input 1*:  **(Required)**
* `definition_in_2` *Camera Input 2*: 
* `definition_in_3` *Camera Input 3*:  This is only used by the grid layout.
* `definition_in_4` *Camera Input 4*:  This is only used by the grid layout.