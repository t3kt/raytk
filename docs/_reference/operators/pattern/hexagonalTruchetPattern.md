---
layout: operator
title: hexagonalTruchetPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalTruchetPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalTruchetPattern/
op:
  category: pattern
  detail: 'This operator produces different types of values from the grid depending
    on the selected Pattern.


    Truchet patterns involve a curving path through a grid (in this case hexagonal),
    where the path is always uninterrupted, but may sometimes form closed loops.


    Based on [hexagonal truchet by FabriceNeyret2](https://www.shadertoy.com/view/Xdt3D8).


    See details about [Truchet tiles](https://en.wikipedia.org/wiki/Truchet_tiles).'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
  name: hexagonalTruchetPattern
  opType: raytk.operators.pattern.hexagonalTruchetPattern
  parameters:
  - label: Pattern
    menuOptions:
    - description: Produces float values with 1 for the path and 0 for the space around
        the path.
      label: Default (FabriceNeyret2)
      name: default
    - description: Produces float values with multiple stripes going through the path.
      label: Variant 1 (Shane)
      name: variant1
    - description: Produces vectors with colors using stripes along the path. Currently
        these colors are fixed and unchangeable.
      label: Variant 2 (Shane)
      name: variant2
    name: Pattern
    readOnlyHandling: baked
    regularHandling: baked
    summary: What type of values to produce from the grid.
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Seed number used to control the randomization of the path.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the pattern.
  summary: Pattern using truchet tiling in a hexagonal arrangement.
  thumb: assets/images/reference/operators/pattern/hexagonalTruchetPattern_thumb.png

---


Pattern using truchet tiling in a hexagonal arrangement.

This operator produces different types of values from the grid depending on the selected Pattern.

Truchet patterns involve a curving path through a grid (in this case hexagonal), where the path is always uninterrupted, but may sometimes form closed loops.

Based on [hexagonal truchet by FabriceNeyret2](https://www.shadertoy.com/view/Xdt3D8).

See details about [Truchet tiles](https://en.wikipedia.org/wiki/Truchet_tiles).