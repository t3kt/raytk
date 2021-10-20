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
    status: beta
    summary: Adjust properties of color values.
  - keywords:
    - color
    - material
    - modularmat
    - surface
    name: assignColor
    summary: Assigns a surface color attribute to an SDF surface.
  - keywords:
    - material
    - modularmat
    - surface
    - texture
    name: assignUV
    summary: Assigns UV coordinates to an SDF surface.
  - name: bend
    summary: Bends space, along a main axis, towards a second axis.
  - name: cartesianToPolar
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
  - keywords:
    - copy
    - instance
    - iterate
    - repeat
    name: instance
    summary: Repeats its input some number of times, exposing the index as the iteration
      x value, and combines the results.
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
  - keywords:
    - clamp
    - limit
    - loop
    - value
    - zigzag
    name: limitField
    summary: Limits the values produced by a float or vector field.
  - name: linkedTransform
    status: alpha
  - name: magnet
    summary: Pulls or twists space within an area.
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
    summary: Repeats space along one axis.
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo2D
    summary: Repeats space along 2 axes.
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo3D
    summary: Repeats space along all 3 axes.
  - keywords:
    - distance
    - modulo
    - polar
    - radial
    - repeat
    name: moduloDistance
  - keywords:
    - kaleidoscope
    - modulo
    - polar
    - repeat
    name: moduloPolar
    summary: Repeats space radially, like a kaleidoscope.
  - keywords:
    - hollow
    - onion
    - shell
    name: onion
    summary: Converts a solid SDF to a thin shell of the surface.
  - name: polarToCartesian
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
  - name: rangeTransform
    status: beta
    summary: Applies a transform based on a range of settings, mapped with either
      the iteration value or a field input.
  - keywords:
    - flip
    - mirror
    - reflect
    name: reflect
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
    summary: Rescales the values produced by a field.
  - name: reshapeValues
    status: beta
    summary: Reshapes the values produced by a field by applying a function.
  - name: restrictStage
    status: beta
    summary: Restricts which render stages an operator is used in.
  - keywords:
    - rotate
    - spin
    - transform
    - twist
    name: rotate
    summary: Transforms space with rotation.
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
    - rotate
    - spin
    name: spin
    status: beta
  - name: spiralZoom
    summary: Transforms space using a logarithmic spiral.
  - name: spread
    status: alpha
  - keywords:
    - move
    - pivot
    - position
    - rotate
    - scale
    - transform
    - translate
    name: transform
    summary: Transform the coordinates of the input, with rotation, scaling, and translation.
  - keywords:
    - move
    - position
    - transform
    - translate
    name: translate
    summary: Translates coordinates of the input ROP.
  - name: truchetTile
    status: alpha
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
