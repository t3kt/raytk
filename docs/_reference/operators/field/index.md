---
layout: page
title: Field Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/field/
---

# Field Operators

Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.

* [`axisDistanceField`](axisDistanceField/) - A float field that provides the distance from a specific point along a single axis.
* [`cellTileField`](cellTileField/) - A value field that provides an approximation of repeating cellular (voronoi) noise.
* [`chopField`](chopField/) -  *beta*{: .label .status-beta }
* [`colorRampField`](colorRampField/) - A vector field that maps an input field to values from a range of colors.
* [`constantColorField`](constantColorField/) - A vector field that evaluates to a constant color value.
* [`constantField`](constantField/) - A float or vector field that evaluates to a constant value.
* [`contextValueField`](contextValueField/) - Field that returns various fields from the context, from a downstream OP.
* [`iterationField`](iterationField/) - Field that returns the current iteration, from a downstream OP.
* [`multiPointDistanceField`](multiPointDistanceField/) - A vector field that provides the distance from 4 specific points in space (one for each part of the vector).
* [`noiseField`](noiseField/) - A float or vector field that uses one of several noise functions.
* [`pointDistanceField`](pointDistanceField/) - A float field that provides the distance from a specific point in space.
* [`positionField`](positionField/) - A vector field that evaluates to the coordinates in space.
* [`reorderField`](reorderField/) - 
* [`textureField`](textureField/) - A float or vector field that looks up values from a texture.
* [`timeField`](timeField/) - 
* [`waveField`](waveField/) - A field that uses a periodic wave.
