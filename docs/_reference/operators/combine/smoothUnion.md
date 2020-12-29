---
layout: page
title: smoothUnion
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/smoothUnion
redirect_from:
  - /reference/opType/raytk.operators.combine.smoothUnion/
---

# smoothUnion

Category: combine



Combines SDFs using a smooth union operator.

Produces the combined areas of the input shapes, blended to smooth out the intersections.

## Parameters

* `Enable` *Enable*
* `Amount` *Amount*: Size of the blending region.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`:  **(Required)** The first SDF to combine.
* `definition_in_2`:  **(Required)** The second SDF to combine.
* `definition_in_3` *Radius Field*:  Float value field that can vary the amount of blending at different points in space.