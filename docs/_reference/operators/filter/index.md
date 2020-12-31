---
layout: operatorCategory
title: Filter Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/filter/
cat:
  name: filter
  summary: |
    Operators that take an input and modify it.
  detail: |
    Many of these are spatial transformations (scale, rotate, translate), which
    alter the coordinates that are used by their input operator.
    
    Many of these can be used for various types of return types (SDFs,
    float/vector fields, etc). Some only support a limited set of return types.
  operators:
    - op:
      name: bend
      summary: Bends space, along a main axis, towards a second axis.
    - op:
      name: cartesianToPolar
    - op:
      name: elongate
      summary: Splits a shape into pieces, moves them apart, and connects them.
    - op:
      name: extend
    - op:
      name: fieldExpr
    - op:
      name: flip
    - op:
      name: fold
    - op:
      name: invert
      summary: Invert an SDF, so that the inside is the outside.
    - op:
      name: iteratedTransform
      summary: Performs a transform multiple times, optionally reflecting across axes in between the steps.
    - op:
      name: knife
      summary: Cuts off an SDF along a plane.
    - op:
      name: limitField
    - op:
      name: magnet
      summary: Pulls or twists space within an area.
    - op:
      name: mirrorOctant
      summary: Mirror coordinates across two axes and the diagonals.
    - op:
      name: modulo1D
    - op:
      name: modulo2D
      summary: Repeats space along 2 axes.
    - op:
      name: modulo3D
      summary: Repeats space along all 3 axes.
    - op:
      name: moduloDistance
    - op:
      name: moduloPolar
      summary: Repeats space radially, like a kaleidoscope.
    - op:
      name: onion
    - op:
      name: quantizeCoords
      summary: Quantize coordinates to a 3D grid, which is sort of like "voxelizing" the space.
    - op:
      name: quantizeValue
    - op:
      name: radialClone
      summary: Repeats an SDF radially around an axis, combining the resulting shapes.
    - op:
      name: reflect
      summary: Reflects space across a plane.
    - op:
      name: reorderCoords
    - op:
      name: rescaleField
    - op:
      name: rotate
    - op:
      name: round
      summary: Adds to (or subtracts from) the size of an SDF, which has the effect of rounding it out or shrinking it.
    - op:
      name: scale
      summary: Scales space.
    - op:
      name: slice
    - op:
      name: transform
      summary: Transform the coordinates of the input, with rotation, scaling, and translation.
    - op:
      name: translate
      summary: Translates coordinates of the input ROP.
    - op:
      name: twist

---

# Filter Operators

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.
