---
layout: operator
title: moduloPolyhedral
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/moduloPolyhedral
redirect_from:
  - /reference/opType/raytk.operators.filter.moduloPolyhedral/
op:
  category: filter
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
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec3
    label: UVW Field
    name: uvwField
    returnTypes:
    - vec4
    sourceParamLabel: UVW Field
    sourceParamName: Uvwfield
    supportedVariableInputs:
    - radiusField
  name: moduloPolyhedral
  opType: raytk.operators.filter.moduloPolyhedral
  parameters:
  - label: Enable
    name: Enable
  - label: Type
    name: Type
    readOnlyHandling: baked
    regularHandling: runtime
  - label: U
    name: U
    readOnlyHandling: baked
    regularHandling: runtime
  - label: V
    name: V
    readOnlyHandling: baked
    regularHandling: runtime
  - label: W
    name: W
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: UVW Field
    name: Uvwfield
  status: beta
  thumb: assets/images/reference/operators/filter/moduloPolyhedral_thumb.png

---
