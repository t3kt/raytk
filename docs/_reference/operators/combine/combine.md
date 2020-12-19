---
layout: page
title: combine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combine
redirect_from:
  - /reference/opType/raytk.operators.combine.combine/
---

# combine

Category: combine



Combines SDFs in various ways.

Depending on which `Combine` option is selected, different parameters will be enabled.
This operator only supports two input SDFs (along with a value field to control blending).
To combine more than two SDFs, use one of the specialized operators like `simpleUnion`.

## Parameters

* `Enable` *Enable*
* `Combine` *Combine*: The type of combination operation to perform.
  * `simpleUnion` *Simple Union*: The combined areas of each of the inputs.
  * `simpleIntersect` *Simple Intersect*: The overlapping areas of each of the inputs.
  * `simpleDiff` *Simple Difference*: The first input with the second input removed from it.
  * `smoothUnion` *Smooth Union*: Like `simpleUnion` but with the intersecting edges rounded out.
  * `smoothIntersect` *Smooth Intersect*: Like `simpleIntersect` but with the intersecting edges rounded out.
  * `smoothDiff` *Smooth Difference*: Like `simpleDiff` but with the intersecting edges rounded out.
  * `roundUnion` *Round Union*: Uses a quarter circle blending area along the edges.
  * `roundIntersect` *Round Intersect*
  * `roundDiff` *Round Difference*
  * `chamferUnion` *Chamfer Union*: Uses a 45 degree flat slope to blend along the edges.
  * `chamferIntersect` *Chamfer Intersect*
  * `chamferDiff` *Chamfer Difference*
  * `stairUnion` *Stair Union*: Uses vertical and horizontal stairs to blend along the edges.
  * `stairIntersect` *Stair Intersect*
  * `stairDiff` *Stair Difference*
  * `columnUnion` *Column Union*: Uses multiple circular tubes to blend along the edges.
  * `columnIntersect` *Column Intersect*
  * `columnDiff` *Column Difference*
* `Swapinputs` *Swap Inputs*: Swaps the order of the inputs. This is only relevant for "diff" modes.
* `Radius` *Radius*: The size of the blending region.
* `Number` *Number*: For stair and column modes, this controls how many steps are used in the blending regions.
* `Inspect` *Inspect*
* `Help` *Help*

## Inputs

* `definition_in_1`
* `definition_in_2`
* `radius_field_definition_in`