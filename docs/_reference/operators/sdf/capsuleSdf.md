---
layout: operator
title: capsuleSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/capsuleSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.capsuleSdf/
op:
  category: sdf
  detail: With a small `Radius`, this can be used to create a line segment.
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
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
  keywords:
  - capsule
  - line
  - points
  - segment
  name: capsuleSdf
  opType: raytk.operators.sdf.capsuleSdf
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
  summary: A line or cylinder with rounded ends, between two points.
  thumb: assets/images/reference/operators/sdf/capsuleSdf_thumb.png
  variables:
  - label: Normalized Offset (0..1)
    name: normoffset

---


A line or cylinder with rounded ends, between two points.

With a small `Radius`, this can be used to create a line segment.