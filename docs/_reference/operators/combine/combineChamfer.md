---
layout: page
title: combineChamfer
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineChamfer
redirect_from:
  - /reference/opType/raytk.operators.combine.combineChamfer/
---

# combineChamfer

Category: combine



Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.

## Parameters

* `Enable` *Enable*
* `Operation` *Operation*: The type of combine operation.
  * `union` *Union*: Produces the combined area of both inputs.
  * `intersect` *Intersect*: Produces the area where both inputs overlap.
  * `diff` *Difference*: Subtracts the second input from the first.
* `Swapinputs` *Swap Inputs*: Swaps the order of the inputs. This is only used for the `diff` mode.
* `Radius` *Radius*: The size of the blending region.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`:  **(Required)**
* `definition_in_2`:  **(Required)**
* `radius_definition_in` *Radius Field*:  Value field that can be used to vary the radius of the blend region at different points in space, by *multiplying* the value of the `Radius` parameter.