---
layout: operator
title: injectObjectId
parent: Utility Operators
grand_parent: Operators
permalink: /reference/operators/utility/injectObjectId
redirect_from:
  - /reference/opType/raytk.operators.utility.injectObjectId/
op:
  category: utility
  detail: 'This can be used to identify which object is shown at any given pixel in

    the output.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: ID Field
    name: idField
    returnTypes:
    - float
  name: injectObjectId
  opType: raytk.operators.utility.injectObjectId
  parameters:
  - label: Enable
    name: Enable
  - label: Object Id
    name: Objectid
    readOnlyHandling: macro
    regularHandling: runtime
  status: beta
  summary: 'Assigns an arbitrary value to the objectId field of an SDF, which can
    later

    be extracted from rendered output.'

---


Assigns an arbitrary value to the objectId field of an SDF, which can later
be extracted from rendered output.

This can be used to identify which object is shown at any given pixel in
the output.