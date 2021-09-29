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
  - name: atmosphereField
    status: beta
    summary: Field that simulates a sun and sky.
  - name: axisDistanceField
    summary: A float field that provides the distance from a specific point along
      a single axis.
  - name: bandField
    summary: Field that applies values based on a band/slice of an axis.
  - name: cellTileField
    summary: A value field that provides an approximation of repeating cellular (voronoi)
      noise.
  - name: chopField
    summary: Field that provides values from a CHOP.
  - keywords:
    - color
    - gradient
    - ramp
    name: colorRampField
    summary: A vector field that maps an input field to values from a range of colors.
  - name: colorSwitchField
    status: beta
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
  - name: domainColorField
    status: beta
  - name: hsvColorField
    status: beta
    summary: A field that uses HSV-based parameters to produce colors.
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
    summary: Vector field that produces the surface normal where it is evaluated.
  - name: pointDistanceField
    summary: A float field that provides the distance from a specific point in space.
  - name: positionField
    summary: A vector field that produces the coordinates in space where it is checked.
  - name: rayField
    summary: Field that provides the ray direction or origin.
  - name: reorderField
    status: beta
  - name: sdfField
    summary: Value field based on an SDF shape.
  - name: stepField
    status: beta
    summary: A field that switches between two values at a threshold point.
  - name: texture3dField
    status: beta
  - name: textureField
    summary: A float or vector field that looks up values from a texture.
  - name: triPlanarTextureField
    summary: Texture field that uses surface normals (or other blending techniques)
      to apply a texture facing each axis.
  - name: uvField
    summary: Field that produces surface UV coordinates, if available.
  - name: valuePointsField
    status: alpha
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
