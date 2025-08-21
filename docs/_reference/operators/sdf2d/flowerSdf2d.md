---
layout: operator
title: flowerSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/flowerSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.flowerSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariables:
    - normangle
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
    - vec2
    label: Amplitude Field
    name: amplitudeField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    supportedVariables:
    - normangle
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
    - vec2
    label: Petals Field
    name: petalsField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - amplitudeField
    supportedVariables:
    - normangle
  name: flowerSdf2d
  opType: raytk.operators.sdf2d.flowerSdf2d
  parameters:
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Amplitude
    name: Amplitude
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Petals
    name: Petals
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/flowerSdf2d_thumb.png
  variables:
  - label: Normalized Angle (0..1)
    name: normangle

---
