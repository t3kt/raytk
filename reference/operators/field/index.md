---
layout: page
title: Field Operators
---

Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.

* [`axisDistanceField`](axisDistanceField.md) - A float field that provides the distance from a specific point along a single axis.

* [`cellTileField`](cellTileField.md) - A value field that provides an approximation of repeating cellular (voronoi) noise.
* [`chopField`](chopField.md) - 
* [`colorRampField`](colorRampField.md) - A vector field that maps an input field to values from a range of colors.
* [`constantColorField`](constantColorField.md) - A vector field that evaluates to a constant color value.
* [`constantField`](constantField.md) - A float or vector field that evaluates to a constant value.
* [`contextValueField`](contextValueField.md) - Field that returns various fields from the context, from a downstream OP.
* [`iterationField`](iterationField.md) - Field that returns the current iteration, from a downstream OP.
* [`multiPointDistanceField`](multiPointDistanceField.md) - A vector field that provides the distance from 4 specific points in space (one for each part of the vector).

* [`noiseField`](noiseField.md) - A float or vector field that uses one of several noise functions.
* [`pointDistanceField`](pointDistanceField.md) - A float field that provides the distance from a specific point in space.

* [`positionField`](positionField.md) - A vector field that evaluates to the coordinates in space.
* [`reorderField`](reorderField.md) - 
* [`textureField`](textureField.md) - A float or vector field that looks up values from a texture.
* [`timeField`](timeField.md) - 
* [`waveField`](waveField.md) - A field that uses a periodic wave.
