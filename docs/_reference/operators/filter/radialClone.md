---
layout: page
title: radialClone
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/radialClone
redirect_from:
  - /reference/opType/raytk.operators.filter.radialClone/
---

# radialClone

Category: filter



Repeats an SDF radially around an axis, combining the resulting shapes.

Note that this runs its input multiple times, which can lead to performance issues.

## Parameters

* `Enable` *Enable*
* `Axis` *Axis*
  * `x` *X*
  * `y` *Y*
  * `z` *Z*
* `Count` *Count*
* `Anglerange` *Angle Range*
* `Angleoffset` *Angle Offset*
* `Radiusoffset` *Radius Offset*
* `Mergetype` *Merge Type*
  * `union` *Union*
  * `smoothunion` *Smooth Union*
* `Mergeradius` *Merge Radius*
* `Iterationtype` *Iteration Type*
  * `none` *None*
  * `index` *Clone Index*
  * `scaled` *Scaled Clone Index*
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`