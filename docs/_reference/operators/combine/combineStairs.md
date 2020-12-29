---
layout: page
title: combineStairs
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineStairs
redirect_from:
  - /reference/opType/raytk.operators.combine.combineStairs/
---

# combineStairs

Category: combine



Stair SDF combine, producing steps along the blend region.

## Parameters

* `Enable` *Enable*
* `Operation` *Operation*: The type of combine operation.
  * `union` *Union*: Produces the combined area of both inputs.
  * `intersect` *Intersect*: Produces the area where both inputs overlap.
  * `diff` *Difference*: Subtracts the second input from the first.
* `Swapinputs` *Swap Inputs*: Swaps the order of the inputs. This is only used for the `diff` mode.
* `Number` *Number*: The number of steps in the blending region.
* `Radius` *Radius*: The size of the blending region.
* `Offset` *Offset*: Shifts the steps along the blend region, with 0 being no shift, and 1 being a full shift of the total number of steps.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`:  **(Required)**
* `definition_in_2`:  **(Required)**
* `radius_definition_in` *Radius Field*:  Value field that can be used to vary the radius of the blend region at different points in space, by *multiplying* the value of the `Radius` parameter.
* `offset_definition_in` *Offset Field*:  Value field that can be used to vary the offset of the stairs at different points in space, by *adding* to the value of the `Offset` parameter.