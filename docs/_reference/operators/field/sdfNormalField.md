---
layout: operator
title: sdfNormalField
parent: Field Operators
grand_parent: Operators
permalink: /reference/operators/field/sdfNormalField
redirect_from:
  - /reference/opType/raytk.operators.field.sdfNormalField/
op:
  category: field
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  name: sdfNormalField
  opType: raytk.operators.field.sdfNormalField
  parameters:
  - label: Enable Normal Smoothing
    name: Enablenormalsmoothing
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Normal Smoothing
    name: Normalsmoothing
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/field/sdfNormalField_thumb.png

---
