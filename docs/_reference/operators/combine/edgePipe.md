---
layout: page
title: edgePipe
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgePipe
redirect_from:
  - /reference/opType/raytk.operators.combine.edgePipe/
---

# edgePipe

Category: combine



Produces a cylindrical pipe along the blend region, replacing the input shapes entirely.

Creates an entirely new SDF result, removing any materials and other settings from the inputs.

## Parameters

* `Enable` *Enable*
* `Radius` *Radius*: The width of the pipe.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`: 
* `definition_in_2`: 
* `radius_definition_in` *Radius Field*:  Value field that can be used to vary the radius of the blend region at different points in space, by *multiplying* the value of the `Radius` parameter.