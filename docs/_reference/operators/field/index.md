---
layout: operatorCategory
title: Field Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/field/
cat:
  detail: 'They can be used to control the behavior of other OPs, such as rotating
    by

    different amounts in different positions, or pulling color values from a

    texture.'
  name: field
  operators:
  - name: axisDistanceField
    summary: A float field that provides the distance from a specific point along
      a single axis.
  - name: bandField
  - name: cellTileField
    summary: A value field that provides an approximation of repeating cellular (voronoi)
      noise.
  - name: chopField
    summary: Field that provides values from a CHOP.
  - name: colorRampField
    summary: A vector field that maps an input field to values from a range of colors.
  - name: constantColorField
    summary: A vector field that evaluates to a constant color value.
  - name: constantField
    summary: A float or vector field that evaluates to a constant value.
  - name: contextValueField
    status: beta
    summary: Field that returns various fields from the context, from a downstream
      OP.
  - name: curlNoiseField
    summary: Curl noise field.
  - name: hsvColorField
    status: beta
  - name: iterationField
    summary: Field that returns the current iteration, from a downstream OP.
  - name: metaballField
    summary: Metaball value field.
  - name: multiPointDistanceField
    summary: A vector field that provides the distance from 4 specific points in space
      (one for each part of the vector).
  - name: noiseField
    summary: A float or vector field that uses one of several noise functions.
  - name: normalField
    status: beta
    summary: Vector field that produces the surface normal where it is evaluated.
  - name: pointDistanceField
    summary: A float field that provides the distance from a specific point in space.
  - name: positionField
    summary: A vector field that produces the coordinates in space where it is checked.
  - name: reorderField
    status: beta
  - name: sdfField
  - name: texture3dField
    status: beta
  - name: textureField
    summary: A float or vector field that looks up values from a texture.
  - name: triPlanarTextureField
    summary: Texture field that uses surface normals (or other blending techniques)
      to apply a texture facing each axis.
  - name: waveField
    summary: A field that uses a periodic wave.
  - name: waveletNoiseField
  summary: Float or vector fields, which provide values for the requested coordinates.

---

# Field Operators

Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.
