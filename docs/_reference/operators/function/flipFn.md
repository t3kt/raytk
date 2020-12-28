---
layout: page
title: flipFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/flipFn
redirect_from:
  - /reference/opType/raytk.operators.function.flipFn/
---

# flipFn

Category: function



Function that flips its input in one of several different modes.

## Parameters

* `Enable` *Enable*
* `Fliptype` *Flip Type*: The type of flipping to apply.
  * `flipdomain` *Flip Domain*: Negates the coordinate passed to the input function, flipping the x axis of a function graph across the y axis.
  * `fliprange` *Flip Range*: Negates the input function's return value, flipping the y axis of a function graph across the x axis.
  * `mirrorposdomain` *Mirror Positive Domain*: Mirrors the coordinate so only the positive half is used, reflecting the positive side of a function graph across the y axis replacing the negative side.
  * `flipnegdomain` *Flip Negative Domain*: Mirrors the coordinate so only the positive half is used, but also flips the return value when on the negative side, reflecting the positive side of a function graph across the y axis but then also flipping that side upside down.
* `Returntype` *Return Type*
  * `useinput` *Use Input*
  * `Sdf` *SDF Result*
  * `float` *Float*
  * `vec4` *Vector4*
  * `Ray` *Ray*
  * `Light` *Light*
* `Contexttype` *Context Type*
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in`: 