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
    summary: Adjust properties of color values, either directly on a field, or on
      the assigned surface color of an Sdf result.
    thumb: assets/images/reference/operators/filter/adjustColor_thumb.png
  - name: applyTransform
    status: beta
  - name: assignAttribute
    status: beta
  - keywords:
    - color
    - material
    - modularmat
    - surface
    name: assignColor
    shortcuts:
    - ac
    summary: Assigns a surface color attribute to an SDF surface.
    thumb: assets/images/reference/operators/filter/assignColor_thumb.png
  - keywords:
    - material
    - modularmat
    - surface
    - texture
    name: assignUV
    summary: Assigns UV coordinates to an SDF surface.
    thumb: assets/images/reference/operators/filter/assignUV_thumb.png
  - name: axisRotate
    summary: A simplified and optimized version of `rotate`, which only supports rotating
      around a single axis (x, y, or z).
  - name: bend
    summary: Bends space, along a main axis, towards a second axis.
    thumb: assets/images/reference/operators/filter/bend_thumb.png
  - name: cameraTransform
    status: beta
    summary: Specialized transform that can be applied to cameras.
  - name: cartesianToPolar
    summary: Convert from cartesian space to various types of polar spaces.
    thumb: assets/images/reference/operators/filter/cartesianToPolar_thumb.png
  - name: circularRepeat
    status: beta
    summary: Repeat an space to fill a 2D circular area.
  - keywords:
    - elongate
    - extend
    - stretch
    name: elongate
    summary: Stretches a shape by splitting it into pieces, moves them apart, and
      connects them.
    thumb: assets/images/reference/operators/filter/elongate_thumb.png
  - keywords:
    - extend
    - stretch
    name: extend
    summary: Clamps coordinates around an area, which causes its edges to be extended
      infinitely along each axis.
    thumb: assets/images/reference/operators/filter/extend_thumb.png
  - name: extrudeBezier
    status: beta
    summary: Extrudes 3D space along the path of a bezier curve.
    thumb: assets/images/reference/operators/filter/extrudeBezier_thumb.png
  - name: fieldExpr
    status: beta
    summary: Modifies field values using a custom expression.
  - name: fieldFunction
    summary: Modifies the values of a field using various types of math functions,
      similar to a `Function CHOP`.
  - name: flip
    summary: Flips the input across an axis, either on its own or merged with the
      original.
    thumb: assets/images/reference/operators/filter/flip_thumb.png
  - name: fold
    thumb: assets/images/reference/operators/filter/fold_thumb.png
  - name: geometricSeriesSquareTile
    status: beta
    summary: Repeats space in a square arrangement that gets smaller in the center.
    thumb: assets/images/reference/operators/filter/geometricSeriesSquareTile_thumb.png
  - name: gridClone
    summary: Repeats an SDF in a grid arrangement, combining the results.
    thumb: assets/images/reference/operators/filter/gridClone_thumb.png
  - name: hilbertCurveTransform
    status: beta
    thumb: assets/images/reference/operators/filter/hilbertCurveTransform_thumb.png
  - keywords:
    - copy
    - instance
    - iterate
    - repeat
    name: instance
    summary: Repeats its input some number of times, exposing the index as the iteration
      x value, and combines the results.
    thumb: assets/images/reference/operators/filter/instance_thumb.png
  - name: instanceField
    summary: Repeats an input field multiple times and combines the results.
  - name: invert
    summary: Invert an SDF, so that the inside is the outside.
    thumb: assets/images/reference/operators/filter/invert_thumb.png
  - name: iteratedTransform
    summary: Performs a transform multiple times, optionally reflecting across axes
      in between the steps.
    thumb: assets/images/reference/operators/filter/iteratedTransform_thumb.png
  - name: kink
    summary: Bends space, similar to the `bend`.
    thumb: assets/images/reference/operators/filter/kink_thumb.png
  - keywords:
    - crop
    - knife
    - slice
    name: knife
    summary: Cuts off an SDF along a plane.
    thumb: assets/images/reference/operators/filter/knife_thumb.png
  - name: lightTransform
    status: beta
    summary: Specialized transform that can be applied to lights, taking into account
      things like look at direction.
  - name: limitArea
    status: beta
    summary: Use an SDF to limit the area where a field produces values.
  - keywords:
    - clamp
    - limit
    - loop
    - value
    - zigzag
    name: limitField
    summary: Limits the values produced by a float or vector field.
    thumb: assets/images/reference/operators/filter/limitField_thumb.png
  - name: limitLight
    status: beta
    summary: Limits the brightness of a light using distance attenuation or a bounding
      SDF (or both).
  - name: linearClone
    summary: Repeats an SDF along a line, combining the results.
    thumb: assets/images/reference/operators/filter/linearClone_thumb.png
  - keywords:
    - log
    - modulo
    - polar
    - radial
    - repeat
    - spiral
    name: logPolarRepeat
    status: beta
    thumb: assets/images/reference/operators/filter/logPolarRepeat_thumb.png
  - name: lookAtRotate
    status: beta
    summary: Rotates space to face towards a point.
  - name: magnet
    summary: Pulls or twists space within an area.
    thumb: assets/images/reference/operators/filter/magnet_thumb.png
  - name: mirrorAxes
    summary: Mirror space across one or more axes, similar to `reflect`.
    thumb: assets/images/reference/operators/filter/mirrorAxes_thumb.png
  - name: mirrorOctant
    summary: Mirror coordinates across two axes and the diagonals.
    thumb: assets/images/reference/operators/filter/mirrorOctant_thumb.png
  - name: mirrorQuadrant
    summary: Mirror coordinates across two axes.
    thumb: assets/images/reference/operators/filter/mirrorQuadrant_thumb.png
  - name: mobiusTransform
    thumb: assets/images/reference/operators/filter/mobiusTransform_thumb.png
  - name: modifyDistance
    status: beta
  - keywords:
    - bumpmap
    - material
    - modularmat
    - normals
    - shading
    - surface
    - texture
    name: modifyNormals
    summary: Use a field to modify the normals (bump mapping) used by shading elements
      in a modular material.
  - keywords:
    - modulo
    - repeat
    name: modulo1D
    shortcuts:
    - m1
    summary: Repeats space along one axis.
    thumb: assets/images/reference/operators/filter/modulo1D_thumb.png
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo2D
    shortcuts:
    - m2
    summary: Repeats space along 2 axes.
    thumb: assets/images/reference/operators/filter/modulo2D_thumb.png
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo3D
    shortcuts:
    - m3
    summary: Repeats space along all 3 axes.
    thumb: assets/images/reference/operators/filter/modulo3D_thumb.png
  - keywords:
    - distance
    - modulo
    - polar
    - radial
    - repeat
    name: moduloDistance
  - name: moduloLine
    status: beta
    summary: Repeats space along a line, similar to `modulo1D`.
  - keywords:
    - kaleidoscope
    - modulo
    - polar
    - repeat
    name: moduloPolar
    shortcuts:
    - mp
    summary: Repeats space radially, like a kaleidoscope.
    thumb: assets/images/reference/operators/filter/moduloPolar_thumb.png
  - name: moduloSpherical
    summary: Repeats space in a spherical mesh layout with rows and columns.
    thumb: assets/images/reference/operators/filter/moduloSpherical_thumb.png
  - keywords:
    - torus
    name: moduloToroidal
    status: beta
    summary: Repeats space as rows and columns of a torus-shaped grid.
    thumb: assets/images/reference/operators/filter/moduloToroidal_thumb.png
  - keywords:
    - hollow
    - onion
    - shell
    name: onion
    summary: Converts a solid SDF to a thin shell of the surface.
    thumb: assets/images/reference/operators/filter/onion_thumb.png
  - name: polarToCartesian
    status: beta
    summary: Converts coordinates from polar to cartesian.
  - name: quadTreeRepeat
    status: beta
    summary: Repeats space in a 2d grid where some cells are subdivided into smaller
      cells recursively.
    thumb: assets/images/reference/operators/filter/quadTreeRepeat_thumb.png
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
    thumb: assets/images/reference/operators/filter/radialClone_thumb.png
  - name: radialSlice
    summary: Takes a pie-shaped slice of an SDF around an axis, either removing it
      or everything except it.
    thumb: assets/images/reference/operators/filter/radialSlice_thumb.png
  - name: rangeTransform
    summary: Applies a transform based on a range of settings, mapped with either
      the iteration value or a field input.
    thumb: assets/images/reference/operators/filter/rangeTransform_thumb.png
  - name: rectangleRepeat
    status: beta
    thumb: assets/images/reference/operators/filter/rectangleRepeat_thumb.png
  - keywords:
    - flip
    - mirror
    - reflect
    name: reflect
    shortcuts:
    - ref
    summary: Reflects space across a plane.
    thumb: assets/images/reference/operators/filter/reflect_thumb.png
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
  - name: rescaleFloatField
    summary: Simplified version of `rescaleField` that only has single settings vs
      vectors for each.
  - name: reshapeValues
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
    thumb: assets/images/reference/operators/filter/rotate4D_thumb.png
  - keywords:
    - material
    - modularmat
    - normals
    - rotate
    - spin
    - transform
    name: rotateNormals
    summary: Applies rotation to the surface normals used by material elements such
      as `specularContrib`.
  - name: round
    summary: Adds to (or subtracts from) the size of an SDF, which has the effect
      of rounding it out or shrinking it.
    thumb: assets/images/reference/operators/filter/round_thumb.png
  - keywords:
    - scale
    - transform
    name: scale
    summary: Scales space.
  - name: slice
    summary: Takes a slice of an SDF along an axis, either removing it or everything
      except it.
  - name: sphericalMobiusTransform
    status: beta
    thumb: assets/images/reference/operators/filter/sphericalMobiusTransform_thumb.png
  - keywords:
    - log
    - polar
    - spiral
    name: spiralZoom
    summary: Transforms space using a logarithmic spiral.
    thumb: assets/images/reference/operators/filter/spiralZoom_thumb.png
  - keywords:
    - separate
    - slice
    name: split
    thumb: assets/images/reference/operators/filter/split_thumb.png
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
  - keywords:
    - apply
    name: transformSequence
    status: beta
    summary: Applies one or more transform operators sequentially, to coordinates,
      field values, etc, with support for looping.
  - keywords:
    - move
    - position
    - transform
    - translate
    name: translate
    shortcuts:
    - tr
    summary: Translates coordinates of the input ROP.
  - name: twirl
    status: beta
    thumb: assets/images/reference/operators/filter/twirl_thumb.png
  - name: twist
    summary: Twists space around an axis.
    thumb: assets/images/reference/operators/filter/twist_thumb.png
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
    summary: Uses repeating waves to offset space.
    thumb: assets/images/reference/operators/filter/waveWarp_thumb.png
  - keywords:
    - volume
    - volumetric
    moduleName: raytkVolumes
    name: assignDensity
    status: beta
  - moduleName: raytkAbstractions
    name: helixWarp
    status: beta
    summary: Warps space in a helix pattern around an axis.
  - moduleName: raytkAbstractions
    name: spin
    summary: Rotation on XYZ with built-in animation.
  summary: Operators that take an input and modify it.

---

# Filter Operators

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.
