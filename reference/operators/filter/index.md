---
layout: page
title: Filter Operators
---

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.

* [`bend`](bend.md) - Bends space, along a main axis, towards a second axis.
* [`elongate`](elongate.md) - Splits a shape into pieces, moves them apart, and connects them.
* [`fieldExpr`](fieldExpr.md) - 
* [`flip`](flip.md) - 
* [`fold`](fold.md) - 
* [`invert`](invert.md) - Invert an SDF, so that the inside is the outside.
* [`iteratedTransform`](iteratedTransform.md) - Performs a transform multiple times, optionally reflecting across axes in between the steps.
* [`knife`](knife.md) - Cuts off an SDF along a plane.
* [`limitField`](limitField.md) - 
* [`magnet`](magnet.md) - 
* [`mirrorOctant`](mirrorOctant.md) - Mirror coordinates across two axes and the diagonals.
* [`modulo1D`](modulo1D.md) - 
* [`modulo2D`](modulo2D.md) - Repeats space along 2 axes.
* [`modulo3D`](modulo3D.md) - Repeats space along all 3 axes.
* [`moduloPolar`](moduloPolar.md) - Repeats space radially, like a kaleidoscope.
* [`onion`](onion.md) - 
* [`quantizeCoords`](quantizeCoords.md) - Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.
* [`quantizeValue`](quantizeValue.md) - 
* [`radialClone`](radialClone.md) - Repeats an SDF radially around an axis, combining the resulting shapes.
* [`reflect`](reflect.md) - Reflects space across a plane.
* [`reorderCoords`](reorderCoords.md) - 
* [`rescaleField`](rescaleField.md) - 
* [`rotate`](rotate.md) - 
* [`round`](round.md) - Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.
* [`scale`](scale.md) - 
* [`slice`](slice.md) - 
* [`transform`](transform.md) - Transform the coordinates of the input, with rotation, scaling, and translation.
* [`translate`](translate.md) - Translates coordinates of the input ROP.
* [`twist`](twist.md) -
