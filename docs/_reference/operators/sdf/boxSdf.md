---
layout: page
title: boxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/boxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.boxSdf/
---

# boxSdf

Category: sdf



SDF for a box, optionally infinite one one axis.

## Parameters

* `Boxtype` *Box Type*: The type of box function.
  * `boxcheap` *Box Cheap*: A bit more efficient but slightly less accurate.
  * `box` *Box*: More accurate but slightly less efficient.
* `Infiniteaxis` *Infinite Axis*: Axis along which the box should stretch infinitely.
  * `none` *None*: Regular box.
  * `x` *X*: Box is infinite along the x axis.
  * `y` *Y*: Box is infinite along the y axis.
  * `z` *Z*: Box is infinite along the z axis.
* `Translate` *Translate*: Move the center of the box.
* `Scale` *Scale*: The size of the box in each dimension.
* `Uniformscale` *Uniform Scale*: Scaling applied to all dimensions of the `Scale`.
* `Inspect` *Inspect*
* `Help` *Help*