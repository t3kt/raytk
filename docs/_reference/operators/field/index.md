---
layout: operatorCategory
title: Field Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/field/
cat:
  name: field
  summary: |
    Float or vector fields, which provide values for the requested coordinates.
  detail: |
    They can be used to control the behavior of other OPs, such as rotating by
    different amounts in different positions, or pulling color values from a
    texture.
  operators:
    - op:
      name: axisDistanceField
      summary: A float field that provides the distance from a specific point along a single axis.
    - op:
      name: cellTileField
      summary: A value field that provides an approximation of repeating cellular (voronoi) noise.
    - op:
      name: chopField
      status: beta
    - op:
      name: colorRampField
      summary: A vector field that maps an input field to values from a range of colors.
    - op:
      name: constantColorField
      summary: A vector field that evaluates to a constant color value.
    - op:
      name: constantField
      summary: A float or vector field that evaluates to a constant value.
    - op:
      name: contextValueField
      summary: Field that returns various fields from the context, from a downstream OP.
    - op:
      name: iterationField
      summary: Field that returns the current iteration, from a downstream OP.
    - op:
      name: metaballField
      summary: Metaball value field.
    - op:
      name: multiPointDistanceField
      summary: A vector field that provides the distance from 4 specific points in space (one for each part of the vector).
    - op:
      name: noiseField
      summary: A float or vector field that uses one of several noise functions.
    - op:
      name: pointDistanceField
      summary: A float field that provides the distance from a specific point in space.
    - op:
      name: positionField
      summary: A vector field that evaluates to the coordinates in space.
    - op:
      name: reorderField
    - op:
      name: textureField
      summary: A float or vector field that looks up values from a texture.
    - op:
      name: waveField
      summary: A field that uses a periodic wave.

---

# Field Operators

Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.
