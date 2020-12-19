---
layout: page
title: noiseField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/noiseField
---

# noiseField

Category: field



A float or vector field that uses one of several noise functions.

## Parameters

* `Noisetype` *Noise Type*
  * `TDSimplexNoise2d` *Simplex 2D*
  * `TDSimplexNoise3d` *Simplex 3D*
  * `TDSimplexNoise4d` *Simplex 4D*
  * `TDPerlinNoise2d` *Perlin 2D*
  * `TDPerlinNoise3d` *Perlin 3D*
  * `TDPerlinNoise4d` *Perlin 4D*
* `Coordtype` *Coord Type*
  * `vec2` *2D*
  * `vec3` *3D*
* `Contexttype` *Context Type*
  * `none` *None*
  * `Context` *Context*
  * `MaterialContext` *Material Context*
  * `CameraContext` *Camera Context*
  * `LightContext` *Light Context*
* `Axis` *Axis*
  * `x` *X*
  * `y` *Y*
  * `z` *Z*
* `Translate` *Translate*
* `Scale` *Scale*
* `Inspect` *Inspect*