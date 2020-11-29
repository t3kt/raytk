---
layout: page
title: Combine Operators
---

Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.

* [`blend`](blend.md) - 
* [`boundLimit`](boundLimit.md) - 
* [`combineChamfer`](combineChamfer.md) - Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.
* [`combineColumns`](combineColumns.md) - Columns SDF combine, producing n-1 circular columns at a 45 degree angles along the blend region.
* [`combineFields`](combineFields.md) - Combines float or vector fields using one of several mathematical operations.
* [`combineStairs`](combineStairs.md) - Stair SDF combine, producing steps along the blend region.
* [`edgeEngrave`](edgeEngrave.md) - 
* [`edgeGroove`](edgeGroove.md) - 
* [`edgePipe`](edgePipe.md) - Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.
* [`iterationSwitch`](iterationSwitch.md) - 
* [`simpleDiff`](simpleDiff.md) - Combines two SDFs using the difference operator.
Produces the area of the first shape minus any areas overlapped by the second (or vice versa).
* [`simpleIntersect`](simpleIntersect.md) - Combines SDFs using the intersect operator.
Produces the areas where all input shapes overlap.
* [`simpleUnion`](simpleUnion.md) - Combines several SDFs using the union operator.
The resulting shape is the combined areas of each of the inputs.
* [`smoothUnion`](smoothUnion.md) - Combines SDFs using a smooth union operator.
Produces the combined areas of the input shapes, blended to smooth out the intersections.
* [`switch`](switch.md) - Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.
