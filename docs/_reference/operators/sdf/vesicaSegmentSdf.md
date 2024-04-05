---
layout: operator
title: vesicaSegmentSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/vesicaSegmentSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.vesicaSegmentSdf/
op:
  category: sdf
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
    - vec3
    label: Endpoint 1 Field
    name: endpoint1
    returnTypes:
    - vec4
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
    - vec3
    label: Endpoint 2 Field
    name: endpoint2
    returnTypes:
    - vec4
    supportedVariableInputs:
    - endpoint1
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
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - endpoint1
    - endpoint2
    supportedVariables:
    - normoffset
  name: vesicaSegmentSdf
  opType: raytk.operators.sdf.vesicaSegmentSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the capsule.
  - label: End Point 1
    name: Endpoint1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Distance of the first end from the center position.
  - label: End Point 2
    name: Endpoint2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Distance of the second end from the center position.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The thickness of the capsule.
  thumb: assets/images/reference/operators/sdf/vesicaSegmentSdf_thumb.png
  variables:
  - label: normoffset
    name: normoffset

---
