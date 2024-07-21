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
    summary: Field that simulates a sun and sky.
    thumb: assets/images/reference/operators/field/atmosphereField_thumb.png
  - name: axisDistanceField
    summary: A float field that provides the distance from a specific point along
      a single axis.
    thumb: assets/images/reference/operators/field/axisDistanceField_thumb.png
  - name: bandField
    summary: Field that applies values based on a band/slice of an axis.
    thumb: assets/images/reference/operators/field/bandField_thumb.png
  - name: blackbodyColorField
    summary: Field that produces colors using a model of blackbody radiation from
      physics.
    thumb: assets/images/reference/operators/field/blackbodyColorField_thumb.png
  - keywords:
    - cellular
    - voronoi
    name: cellTileField
    summary: A value field that provides an approximation of repeating cellular (voronoi)
      noise.
    thumb: assets/images/reference/operators/field/cellTileField_thumb.png
  - name: chopField
    summary: Field that provides values from a CHOP.
  - keywords:
    - color
    - gradient
    - ramp
    name: colorRampField
    summary: A vector field that maps an input field to values from a range of colors.
    thumb: assets/images/reference/operators/field/colorRampField_thumb.png
  - name: colorSwitchField
    summary: Switches or fades between a list of colors based on an index field.
  - name: constantColorField
    summary: A vector field that evaluates to a constant color value.
    thumb: assets/images/reference/operators/field/constantColorField_thumb.png
  - name: constantField
    summary: A float or vector field that evaluates to a constant value.
    thumb: assets/images/reference/operators/field/constantField_thumb.png
  - name: constantSwitchField
    summary: Switches or blends between constant values based on an index field.
  - name: curlNoiseField
    summary: Curl noise field.
    thumb: assets/images/reference/operators/field/curlNoiseField_thumb.png
  - name: dataTextureField
    summary: Accesses data from a texture with the same layout as the renderer.
  - name: domainColorField
    status: beta
    thumb: assets/images/reference/operators/field/domainColorField_thumb.png
  - name: hashField
    status: beta
    summary: Advanced field that produces randomized values.
  - name: hsvColorField
    summary: A field that uses HSV-based parameters to produce colors.
    thumb: assets/images/reference/operators/field/hsvColorField_thumb.png
  - name: iterationField
    summary: Field that returns the current iteration, from a downstream OP.
  - name: magnetField
    thumb: assets/images/reference/operators/field/magnetField_thumb.png
  - name: metaballField
    summary: Metaball value field.
    thumb: assets/images/reference/operators/field/metaballField_thumb.png
  - name: multiPointDistanceField
    summary: A vector field that provides the distance from 4 specific points in space
      (one for each part of the vector).
    thumb: assets/images/reference/operators/field/multiPointDistanceField_thumb.png
  - name: nearestRingPointField
    thumb: assets/images/reference/operators/field/nearestRingPointField_thumb.png
  - name: noiseField
    summary: A float or vector field that uses one of several noise functions.
    thumb: assets/images/reference/operators/field/noiseField_thumb.png
  - name: normalField
    status: deprecated
    summary: Vector field that produces the surface normal where it is evaluated.
    thumb: assets/images/reference/operators/field/normalField_thumb.png
  - name: pointDistanceField
    summary: A float field that provides the distance from a specific point in space
      from either the current position or from another point.
    thumb: assets/images/reference/operators/field/pointDistanceField_thumb.png
  - name: polarCoordField
    summary: A field that produces various types of polar coordinates.
    thumb: assets/images/reference/operators/field/polarCoordField_thumb.png
  - name: polarVectorField
    thumb: assets/images/reference/operators/field/polarVectorField_thumb.png
  - name: positionField
    shortcuts:
    - pos
    summary: A vector field that produces the coordinates in space where it is checked.
    thumb: assets/images/reference/operators/field/positionField_thumb.png
  - name: rampField
    summary: Field that produces values that fade from one value to another along
      an axis or line.
    thumb: assets/images/reference/operators/field/rampField_thumb.png
  - name: rayField
    summary: Field that provides the ray direction or origin.
    thumb: assets/images/reference/operators/field/rayField_thumb.png
  - name: reorderField
  - name: sdfField
    summary: Value field based on an SDF shape.
    thumb: assets/images/reference/operators/field/sdfField_thumb.png
  - name: sdfNormalField
    status: beta
    thumb: assets/images/reference/operators/field/sdfNormalField_thumb.png
  - name: spectralColorField
    summary: Produces colors using rainbow spectrum patterns.
    thumb: assets/images/reference/operators/field/spectralColorField_thumb.png
  - name: stepField
    summary: A field that switches between two values at a threshold point.
    thumb: assets/images/reference/operators/field/stepField_thumb.png
  - keywords:
    - fbm
    - landscape
    name: terrainNoiseField
    summary: Noise that uses fBm (fractal brownian motion), which can work well for
      surface offsetting for terrain.
    thumb: assets/images/reference/operators/field/terrainNoiseField_thumb.png
  - name: texture1dField
  - name: texture3dField
    thumb: assets/images/reference/operators/field/texture3dField_thumb.png
  - name: textureField
    summary: A float or vector field that looks up values from a texture.
    thumb: assets/images/reference/operators/field/textureField_thumb.png
  - name: triPlanarTextureField
    summary: Texture field that uses surface normals (or other blending techniques)
      to apply a texture facing each axis.
    thumb: assets/images/reference/operators/field/triPlanarTextureField_thumb.png
  - name: uvField
    summary: Field that produces surface UV coordinates, if available.
    thumb: assets/images/reference/operators/field/uvField_thumb.png
  - name: waveField
    summary: A field that uses a periodic wave.
    thumb: assets/images/reference/operators/field/waveField_thumb.png
  - name: waveVectorField
    status: beta
    thumb: assets/images/reference/operators/field/waveVectorField_thumb.png
  - name: waveletNoiseField
    thumb: assets/images/reference/operators/field/waveletNoiseField_thumb.png
  - name: worleyNoiseField
    thumb: assets/images/reference/operators/field/worleyNoiseField_thumb.png
  - moduleName: raytkAbstractions
    name: enhancedWaveField
    status: beta
  summary: Float or vector fields, which provide values for the requested coordinates.

---

# Field Operators

Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.
