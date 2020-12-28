---
layout: page
title: combineColumns
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineColumns
redirect_from:
  - /reference/opType/raytk.operators.combine.combineColumns/
---

# combineColumns

Category: combine



Columns SDF combine, producing n-1 circular columns/ridges at a 45 degree angles along the blend region.

## Parameters

* `Enable` *Enable*
* `Operation` *Operation*: The type of combine operation.
  * `union` *Union*: Produces the combined area of both inputs.
  * `intersect` *Intersect*: Produces the area where both inputs overlap.
  * `diff` *Difference*: Subtracts the second input from the first.
* `Swapinputs` *Swap Inputs*: Swaps the order of the inputs. This is only used for the `diff` mode.
* `Number` *Number*: The number of columns in the blending region.
* `Radius` *Radius*: The size of the blending region.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `radius_definition_in` *Radius Field*:  Value field that can be used to vary the radius of the blend region at different points in space, by *multiplying* the value of the `Radius` parameter.