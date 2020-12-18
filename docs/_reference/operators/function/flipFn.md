---
layout: page
title: flipFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/flipFn
---

# flipFn

Category: function
OP Type: raytk.operators.function.flipFn



Function that flips its input in one of several different modes.

## Parameters

* `Enable`
* `Fliptype`: The type of flipping to apply.
  * `flipdomain`: Negates the coordinate passed to the input function, flipping the x axis of a function graph across the y axis.
  * `fliprange`: Negates the input function's return value, flipping the y axis of a function graph across the x axis.
  * `mirrorposdomain`: Mirrors the coordinate so only the positive half is used, reflecting the positive side of a function graph across the y axis replacing the negative side.
  * `flipnegdomain`: Mirrors the coordinate so only the positive half is used, but also flips the return value when on the negative side, reflecting the positive side of a function graph across the y axis but then also flipping that side upside down.
* `Returntype`
* `Contexttype`
* `Inspect`