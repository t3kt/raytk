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
  - name: axisDistanceField
  - name: bandField
  - name: blackbodyColorField
  - keywords:
    - cellular
    - voronoi
    name: cellTileField
  - name: chopField
  - keywords:
    - color
    - gradient
    - ramp
    name: colorRampField
  - name: colorSwitchField
  - name: constantColorField
  - name: constantField
  - name: constantSwitchField
  - name: curlNoiseField
  - name: dataTextureField
  - name: domainColorField
    status: beta
  - name: hashField
    status: beta
  - name: hsvColorField
  - name: iterationField
  - name: magnetField
    status: beta
  - name: metaballField
  - name: multiPointDistanceField
  - name: nearestRingPointField
  - name: noiseField
  - name: normalField
    status: deprecated
  - name: pointDistanceField
  - name: polarCoordField
  - name: polarVectorField
  - name: positionField
    shortcuts:
    - pos
  - name: rampField
    status: beta
  - name: rayField
  - name: reorderField
  - name: sdfField
  - name: sdfNormalField
    status: beta
  - name: spectralColorField
  - name: stepField
  - keywords:
    - fbm
    - landscape
    name: terrainNoiseField
    status: beta
  - name: texture1dField
    status: beta
  - name: texture3dField
  - name: textureField
  - name: triPlanarTextureField
  - name: uvField
  - name: waveField
  - name: waveVectorField
    status: beta
  - name: waveletNoiseField
  - name: worleyNoiseField
  summary: Float or vector fields, which provide values for the requested coordinates.

---

# Field Operators

Float or vector fields, which provide values for the requested coordinates.

They can be used to control the behavior of other OPs, such as rotating by
different amounts in different positions, or pulling color values from a
texture.
