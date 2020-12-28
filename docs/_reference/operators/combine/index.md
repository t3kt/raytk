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

* [`blend`](blend/) - Smoothly blends/morphs between up to 4 SDFs.
* [`combine`](combine/) - Combines SDFs in various ways.
* [`combineChamfer`](combineChamfer/) - Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.
* [`combineColumns`](combineColumns/) - Columns SDF combine, producing n-1 circular columns/ridges at a 45 degree angles along the blend region.
* [`combineFields`](combineFields/) - Combines float or vector fields using one of several mathematical operations.
* [`combineStairs`](combineStairs/) - Stair SDF combine, producing steps along the blend region.
* [`edgeEngrave`](edgeEngrave/) - Carves a v-shaped groove where the second input intersects with the first.
* [`edgeGroove`](edgeGroove/) - Creates a raised bar or indented groove where the second input intersects with the first.
* [`edgePipe`](edgePipe/) - Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.
* [`iterationSwitch`](iterationSwitch/) - 
* [`layoutGrid`](layoutGrid/) - Slices space into a grid, and places each input in a separate cell.
* [`simpleDiff`](simpleDiff/) - Combines two SDFs using the difference operator.
* [`simpleIntersect`](simpleIntersect/) - Combines SDFs using the intersect operator.
* [`simpleUnion`](simpleUnion/) - Combines several SDFs using the union operator.
* [`smoothUnion`](smoothUnion/) - Combines SDFs using a smooth union operator.
* [`switch`](switch/) - Switches between several inputs, without the need to rebuild the shader, allowing for fast switching.
