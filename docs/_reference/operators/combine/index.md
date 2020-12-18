---
layout: page
title: Combine Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/combine/
---

# Combine Operators

Operators that take two or more inputs and combine them into a single
output.

This includes operations that merge SDFs (union, diff, intersect), as
well as more generic things like switches and cross-fade blending.

* [`blend`](blend/) - 
* [`combine`](combine/) - 
* [`combineChamfer`](combineChamfer/) - Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.
* [`combineColumns`](combineColumns/) - Columns SDF combine, producing n-1 circular columns at a 45 degree angles along the blend region.
* [`combineFields`](combineFields/) - Combines float or vector fields using one of several mathematical operations.
* [`combineStairs`](combineStairs/) - Stair SDF combine, producing steps along the blend region.
* [`edgeEngrave`](edgeEngrave/) - 
* [`edgeGroove`](edgeGroove/) - 
* [`edgePipe`](edgePipe/) - Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.
* [`iterationSwitch`](iterationSwitch/) - 
* [`layoutGrid`](layoutGrid/) - 
* [`simpleDiff`](simpleDiff/) - Combines two SDFs using the difference operator.
Produces the area of the first shape minus any areas overlapped by the second (or vice versa).
* [`simpleIntersect`](simpleIntersect/) - Combines SDFs using the intersect operator.
Produces the areas where all input shapes overlap.
* [`simpleUnion`](simpleUnion/) - Combines several SDFs using the union operator.
The resulting shape is the combined areas of each of the inputs.
* [`smoothUnion`](smoothUnion/) - Combines SDFs using a smooth union operator.
Produces the combined areas of the input shapes, blended to smooth out the intersections.
* [`switch`](switch/) - Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.
