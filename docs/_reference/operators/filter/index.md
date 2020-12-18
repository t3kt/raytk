---
layout: page
title: Filter Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/filter/
---

# Filter Operators

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.

* [`bend`](bend/) - Bends space, along a main axis, towards a second axis.
* [`cartesianToPolar`](cartesianToPolar/) - 
* [`elongate`](elongate/) - Splits a shape into pieces, moves them apart, and connects them.
* [`extend`](extend/) - 
* [`fieldExpr`](fieldExpr/) - 
* [`flip`](flip/) - 
* [`fold`](fold/) - 
* [`invert`](invert/) - Invert an SDF, so that the inside is the outside.
* [`iteratedTransform`](iteratedTransform/) - Performs a transform multiple times, optionally reflecting across axes in between the steps.
* [`knife`](knife/) - Cuts off an SDF along a plane.
* [`limitField`](limitField/) - 
* [`magnet`](magnet/) - 
* [`mirrorOctant`](mirrorOctant/) - Mirror coordinates across two axes and the diagonals.
* [`modulo1D`](modulo1D/) - 
* [`modulo2D`](modulo2D/) - Repeats space along 2 axes.
* [`modulo3D`](modulo3D/) - Repeats space along all 3 axes.
* [`moduloDistance`](moduloDistance/) - 
* [`moduloPolar`](moduloPolar/) - Repeats space radially, like a kaleidoscope.
* [`onion`](onion/) - 
* [`quantizeCoords`](quantizeCoords/) - Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.
* [`quantizeValue`](quantizeValue/) - 
* [`radialClone`](radialClone/) - Repeats an SDF radially around an axis, combining the resulting shapes.
* [`reflect`](reflect/) - Reflects space across a plane.
* [`reorderCoords`](reorderCoords/) - 
* [`rescaleField`](rescaleField/) - 
* [`rotate`](rotate/) - 
* [`round`](round/) - Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.
* [`scale`](scale/) - 
* [`slice`](slice/) - 
* [`transform`](transform/) - Transform the coordinates of the input, with rotation, scaling, and translation.
* [`translate`](translate/) - Translates coordinates of the input ROP.
* [`twist`](twist/) - 
