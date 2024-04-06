---
layout: operator
title: sphereGridSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/sphereGridSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.sphereGridSdf/
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  name: sphereGridSdf
  opType: raytk.operators.sdf.sphereGridSdf
  parameters:
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Parts
    menuOptions:
    - label: Both Latitudes & Longitudes
      name: latlon
    - label: Latitudes Only
      name: lat
    - label: Longitudes Only
      name: lon
    name: Parts
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Rows
    name: Rows
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Columns
    name: Cols
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: the thickness of the bars.
  status: beta
  thumb: assets/images/reference/operators/sdf/sphereGridSdf_thumb.png

---
