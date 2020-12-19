---
layout: page
title: layoutGrid
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/layoutGrid
---

# layoutGrid

Category: combine



Slices space into a grid, and places each input in a separate cell.

This is useful to see several different variations of a shape.
The input shapes are shifted to the center of their cell.

## Parameters

* `Enable` *Enable*
* `Layout` *Layout*: How to arrange the cells.
  * `row` *Row*: Slice space into cells horizontally. The first cell extends off infinitely to the left and the last cell extends infinitely off to the right.
  * `column` *Column*: Slice space into cells vertically.
  * `gridrow` *Grid Rows*: Slice space into 4 cells arranged in a grid.
* `Axis` *Plane*: The plane along which to arrange the cells.
  * `x` *YZ*
  * `y` *ZX*
  * `z` *XY*
* `Size` *Size*: The size of the cells
* `Prescale` *Pre Scale*: Scales the inputs within their cells.
* `Inspect` *Inspect*

## Inputs

* `definition_in_1`
* `definition_in_2`
* `definition_in_3`
* `definition_in_4`