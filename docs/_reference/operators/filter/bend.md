---
layout: page
title: bend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/bend
redirect_from:
  - /reference/opType/raytk.operators.filter.bend/
---

# bend

Category: filter



Bends space, along a main axis, towards a second axis.

For example, bends sideways (towards X) depending on the vertical position (along Y).

## Parameters

* `Enable` *Enable*
* `Direction` *Direction*: Chooses the axis to bend along and the axis to bend towards.
  * `xyz` *Along X Toward Y*
  * `xzy` *Along X Toward Z*
  * `yxz` *Along Y Toward X*
  * `yzx` *Along Y Toward Z*
  * `zxy` *Along Z Toward X*
  * `zyx` *Along Z Toward Y*
* `Amount` *Amount*: Amount of bending.
* `Shift` *Shift*: Shifts the axis to bend along and the axis to bend towards.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`:  **(Required)**
* `definition_in_2` *Bend Field*:  Value field that determines how much to bend. If this accepts 1D coords, it is passed the position along the bend axis. For 2D coords, both the bend axis and the bend direction are passed. For 3D coords, the relative XYZ position is passed.