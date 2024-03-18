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
  - keywords:
    - material
    - modularmat
    - surface
    - texture
    name: assignUV
  - name: axisRotate
  - name: bend
  - name: cameraTransform
    status: beta
  - name: cartesianToPolar
  - name: circularRepeat
    status: beta
  - keywords:
    - elongate
    - extend
    - stretch
    name: elongate
  - keywords:
    - extend
    - stretch
    name: extend
  - name: fieldExpr
    status: beta
  - name: fieldFunction
    status: beta
  - name: flip
  - name: fold
  - name: geometricSeriesSquareTile
    status: beta
  - name: gridClone
  - name: hilbertCurveTransform
    status: beta
  - keywords:
    - copy
    - instance
    - iterate
    - repeat
    name: instance
  - name: instanceField
  - name: invert
  - name: iteratedTransform
  - name: kink
  - keywords:
    - crop
    - knife
    - slice
    name: knife
  - name: limitArea
    status: beta
  - keywords:
    - clamp
    - limit
    - loop
    - value
    - zigzag
    name: limitField
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
  - name: mirrorAxes
  - name: mirrorOctant
  - name: mirrorQuadrant
  - name: mobiusTransform
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
  - keywords:
    - modulo
    - repeat
    name: modulo1D
    shortcuts:
    - m1
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo2D
    shortcuts:
    - m2
  - keywords:
    - grid
    - modulo
    - repeat
    name: modulo3D
    shortcuts:
    - m3
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
  - name: moduloSpherical
  - keywords:
    - hollow
    - onion
    - shell
    name: onion
  - name: polarToCartesian
    status: beta
  - name: quadTreeRepeat
    status: beta
  - name: quantizeCoords
  - name: quantizeValue
  - keywords:
    - clone
    - copy
    - radial
    - repeat
    name: radialClone
  - name: radialSlice
  - name: rangeTransform
  - name: rectangleRepeat
    status: beta
  - keywords:
    - flip
    - mirror
    - reflect
    name: reflect
    shortcuts:
    - ref
  - name: remapCoords
    status: beta
  - name: reorderCoords
  - keywords:
    - range
    - remap
    - rescale
    name: rescaleField
    shortcuts:
    - rf
  - name: rescaleFloatField
  - name: reshapeValues
  - name: restrictStage
  - keywords:
    - rotate
    - spin
    - transform
    - twist
    name: rotate
    shortcuts:
    - rot
  - name: rotate4D
  - keywords:
    - material
    - modularmat
    - normals
    - rotate
    - spin
    - transform
    name: rotateNormals
  - name: round
  - keywords:
    - scale
    - transform
    name: scale
  - name: slice
  - name: sphericalMobiusTransform
    status: beta
  - keywords:
    - log
    - polar
    - spiral
    name: spiralZoom
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
  - keywords:
    - apply
    name: transformSequence
    status: beta
  - keywords:
    - move
    - position
    - transform
    - translate
    name: translate
    shortcuts:
    - tr
  - name: twist
  - name: uvTransform
    status: beta
  - keywords:
    - offset
    - shift
    - sine
    - warp
    - wave
    name: waveWarp
  summary: Operators that take an input and modify it.

---

# Filter Operators

Operators that take an input and modify it.

Many of these are spatial transformations (scale, rotate, translate), which
alter the coordinates that are used by their input operator.

Many of these can be used for various types of return types (SDFs,
float/vector fields, etc). Some only support a limited set of return types.
