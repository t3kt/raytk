---
layout: page
title: scale
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/scale
redirect_from:
  - /reference/opType/raytk.operators.filter.scale/
---

# scale

Category: filter



Scales space.

Scaling works for either 3D or 2D inputs.

## Parameters

* `Enable` *Enable*
* `Scale` *Scale*: Scale to apply to each axis. If input is 2D only X and Y are used.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`: 
* `scale_field_definition_in` *Scale Field*:  If provided, this field is used to modify the scaling at different points in space. If the field returns float values, the value of all the `Scale` parameters are multiplied by that value. If it returns vec4 values, each part of the `Scale` parameter is multiplied by the corresponding value in the vec4.