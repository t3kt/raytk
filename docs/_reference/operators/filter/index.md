---
layout: operatorCategory
title: Filter Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/filter/
cat:
  detail: 'Many of these are spatial transformations (scale, rotate, translate), which

    alter the coordinates that are used by their input operator.


    Many of these can be used for various types of return types (SDFs,

    float/vector fields, etc). Some only support a limited set of return types.'
  name: filter
  operators:
  - name: bend
    summary: Bends space, along a main axis, towards a second axis.
  - name: cartesianToPolar
  - name: elongate
    summary: Splits a shape into pieces, moves them apart, and connects them.
  - name: extend
  - name: fieldExpr
    status: beta
  - name: flip
    summary: Flips the input across an axis, either on its own or merged with the
      original.
  - name: fold
  - name: instance
    summary: Repeats its input some number of times, exposing the index as the iteration
      x value, and combines the results.
  - name: invert
    summary: Invert an SDF, so that the inside is the outside.
  - name: iteratedTransform
    summary: Performs a transform multiple times, optionally reflecting across axes
      in between the steps.
  - name: knife
    summary: Cuts off an SDF along a plane.
  - name: limitField
  - name: magnet
    summary: Pulls or twists space within an area.
  - name: mirrorOctant
    summary: Mirror coordinates across two axes and the diagonals.
  - name: mobiusTransform
  - name: modulo1D
    summary: Repeats space along one axis.
  - name: modulo2D
    summary: Repeats space along 2 axes.
  - name: modulo3D
    summary: Repeats space along all 3 axes.
  - name: moduloDistance
  - name: moduloPolar
    summary: Repeats space radially, like a kaleidoscope.
  - name: onion
    summary: Converts a solid SDF to a thin shell of the surface.
  - name: quantizeCoords
    summary: Quantize coordinates to a 3D grid, which is sort of like "voxelizing"
      the space.
  - name: quantizeValue
    status: beta
  - name: radialClone
    summary: Repeats an SDF radially around an axis, combining the resulting shapes.
  - name: rangeTransform
    status: beta
    summary: Applies a transform based on a range of settings, mapped with either
      the iteration value or a field input.
  - name: reflect
    summary: Reflects space across a plane.
  - name: remapCoords
    status: beta
  - name: reorderCoords
    summary: Swaps axes for the input.
  - name: rescaleField
  - name: reshapeValues
    status: beta
    summary: Reshapes the values produced by a field by applying a function.
  - name: rotate
  - name: rotateNormals
    status: beta
    summary: Applies rotation to the surface normals used by material elements such
      as `specularContrib`.
  - name: round
    summary: Adds to (or subtracts from) the size of an SDF, which has the effect
      of rounding it out or shrinking it.
  - name: scale
    summary: Scales space.
  - name: slice
    summary: Removes all of an SDF except for a slice in space.
  - name: sphericalMobiusTransform
    status: beta
  - name: spiralZoom
    summary: Transforms space using a logarithmic spiral.
  - name: transform
    summary: Transform the coordinates of the input, with rotation, scaling, and translation.
  - name: translate
    summary: Translates coordinates of the input ROP.
  - name: twist
    summary: Twists space around an axis.
  summary: Operators that take an input and modify it.

---

# Filter Operators

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.
