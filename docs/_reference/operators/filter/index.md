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
  - keywords:
    - adjust
    - brightness
    - color
    - contrast
    - filter
    - hue
    - saturation
    name: adjustColor
    summary: Adjust properties of color values.
  - keywords:
    - color
    - material
    - modularmat
    - surface
    name: assignColor
    shortcuts:
    - ac
    summary: Assigns a surface color attribute to an SDF surface.
  - keywords:
    - material
    - modularmat
    - surface
    - texture
    name: assignUV
    summary: Assigns UV coordinates to an SDF surface.
  - name: axisRotate
    summary: A simplified and optimized version of `rotate`, which only supports rotating
      around a single axis (x, y, or z).
  - name: bend
    summary: Bends space, along a main axis, towards a second axis.
  - name: cartesianToPolar
    summary: Convert from cartesian space to various types of polar spaces.
  - name: circularRepeat
    status: beta
    summary: Repeat an SDF to fill a 2D circular area.
  - keywords:
    - elongate
    - extend
    - stretch
    name: elongate
    summary: Stretches a shape by splitting it into pieces, moves them apart, and
      connects them.
  - keywords:
    - extend
    - stretch
    name: extend
    summary: Clamps coordinates around an SDF result, which causes their edges to
      be extended infinitely along each axis.
  - name: fieldExpr
    status: beta
  - name: fieldFunction
    status: beta
  - name: flip
    summary: Flips the input across an axis, either on its own or merged with the
      original.
  - name: fold
  - name: geometricSeriesSquareTile
    status: beta
    summary: Repeats space in a square arrangement that gets smaller in the center.
  - name: hilbertCurveTransform
    status: beta
  - keywords:
    - copy
    - instance
    - iterate
    - repeat
    name: instance
    summary: Repeats its input some number of times, exposing the index as the iteration
      x value, and combines the results.
  - name: instanceField
    status: beta
  - name: invert
    summary: Invert an SDF, so that the inside is the outside.
  - name: iteratedTransform
    summary: Performs a transform multiple times, optionally reflecting across axes
      in between the steps.
  - name: kink
  - keywords:
    - crop
    - knife
    - slice
    name: knife
    summary: Cuts off an SDF along a plane.
  - name: limitArea
    status: beta
  - keywords:
    - clamp
    - limit
    - loop
    - value
    - zigzag
    name: limitField
    summary: Limits the values produced by a float or vector field.
  - name: linearClone
  - keywords:
    - log
    - modulo
    - polar
    - radial
    - repeat
    - spiral
    name: logPolarRepeat
    status: beta
  - name: lookAtRotate
    status: beta
  - name: magnet
    summary: Pulls or twists space within an area.
  - name: mirrorAxes
  - name: mirrorOctant
    summary: Mirror coordinates across two axes and the diagonals.
  - name: mirrorQuadrant
    summary: Mirror coordinates across two axes.
  - name: mobiusTransform
  - keywords:
    - bumpmap
    - material
    - modularmat
    - normals
    - shading
    - surface
    - texture
    name: modifyNormals
    status: beta
    summary: Use a field to modify the normals (bump mapping) used by shading elements
      in a modular material.
  - keywords:
    - modulo
    - repeat
    name: modulo1D
    shortcuts:
    - m1
    summary: Repeats space along one axis.
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo2D
    shortcuts:
    - m2
    summary: Repeats space along 2 axes.
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo3D
    shortcuts:
    - m3
    summary: Repeats space along all 3 axes.
  - keywords:
    - distance
    - modulo
    - polar
    - radial
    - repeat
    name: moduloDistance
  - name: moduloLine
    status: beta
  - keywords:
    - kaleidoscope
    - modulo
    - polar
    - repeat
    name: moduloPolar
    shortcuts:
    - mp
    summary: Repeats space radially, like a kaleidoscope.
  - name: moduloSpherical
  - keywords:
    - hollow
    - onion
    - shell
    name: onion
    summary: Converts a solid SDF to a thin shell of the surface.
  - name: polarToCartesian
    status: beta
    summary: Converts coordinates from polar to cartesian.
  - name: quadTreeRepeat
    status: beta
  - name: quantizeCoords
    summary: Quantize coordinates to a 3D grid, which is sort of like "voxelizing"
      the space.
  - name: quantizeValue
  - keywords:
    - clone
    - copy
    - radial
    - repeat
    name: radialClone
    summary: Repeats an SDF radially around an axis, combining the resulting shapes.
  - name: radialSlice
  - name: rangeTransform
    summary: Applies a transform based on a range of settings, mapped with either
      the iteration value or a field input.
  - keywords:
    - flip
    - mirror
    - reflect
    name: reflect
    shortcuts:
    - ref
    summary: Reflects space across a plane.
  - name: remapCoords
    status: beta
    summary: Modifies space using a vector field.
  - name: reorderCoords
    summary: Swaps axes for the input.
  - keywords:
    - range
    - remap
    - rescale
    name: rescaleField
    shortcuts:
    - rf
    summary: Rescales the values produced by a field.
  - name: reshapeValues
    status: beta
    summary: Reshapes the values produced by a field by applying a function.
  - name: restrictStage
    summary: Restricts which render stages an operator is used in.
  - keywords:
    - rotate
    - spin
    - transform
    - twist
    name: rotate
    shortcuts:
    - rot
    summary: Transforms space with rotation.
  - name: rotate4D
    summary: Projects 3D space into 4D space, applies rotation along two axes and
      then projects back into 3D space.
  - keywords:
    - material
    - modularmat
    - normals
    - rotate
    - spin
    - transform
    name: rotateNormals
    status: beta
    summary: Applies rotation to the surface normals used by material elements such
      as `specularContrib`.
  - name: round
    summary: Adds to (or subtracts from) the size of an SDF, which has the effect
      of rounding it out or shrinking it.
  - keywords:
    - scale
    - transform
    name: scale
    summary: Scales space.
  - name: slice
    summary: Removes all of an SDF except for a slice in space.
  - name: sphericalMobiusTransform
    status: beta
  - keywords:
    - log
    - polar
    - spiral
    name: spiralZoom
    summary: Transforms space using a logarithmic spiral.
  - keywords:
    - move
    - pivot
    - position
    - rotate
    - scale
    - transform
    - translate
    name: transform
    shortcuts:
    - tfm
    summary: Transform the coordinates of the input, with rotation, scaling, and translation.
  - name: transformSequence
    status: beta
  - keywords:
    - move
    - position
    - transform
    - translate
    name: translate
    shortcuts:
    - tr
    summary: Translates coordinates of the input ROP.
  - name: twist
    summary: Twists space around an axis.
  - name: uvTransform
    status: beta
    summary: Transform the UV coordinates assigned to an SDF result.
  - keywords:
    - offset
    - shift
    - sine
    - warp
    - wave
    name: waveWarp
    status: beta
    summary: Uses repeating waves to offset space.
  summary: Operators that take an input and modify it.

---

# Filter Operators

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.
