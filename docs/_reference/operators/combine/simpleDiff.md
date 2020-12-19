---
layout: page
title: simpleDiff
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/simpleDiff
---

# simpleDiff

Category: combine



Combines two SDFs using the difference operator.

Produces the area of the first shape minus any areas overlapped by the second (or vice versa).

## Parameters

* `Enable` *Enable*
* `Swaporder` *Swap Order*: Swaps the two inputs, subtracting the first from the second.
* `Inspect` *Inspect*

## Inputs

* `definition_in_1`: The first SDF, which has the second removed from it (unless `Swaporder` is used).
* `definition_in_2`: The second SDF, which is removed from the first (unless `Swaporder` is used).