---
layout: operator
title: assignDensity
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/assignDensity
redirect_from:
  - /reference/opType/raytkVolumes.operators.filter.assignDensity/
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
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF or Volume
    name: sdf
    required: true
    returnTypes:
    - Sdf
    - Volume
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Density Field
    name: density
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp1
    supportedVariables:
    - sdf
  keywords:
  - volume
  - volumetric
  moduleName: raytkVolumes
  name: assignDensity
  opType: raytkVolumes.operators.filter.assignDensity
  parameters:
  - label: Enable
    name: Enable
  - label: Density
    name: Density
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Fill Mode
    menuOptions:
    - label: Inside
      name: inside
    - label: Outside
      name: outside
    - label: Everywhere
      name: everywhere
    - label: Surface
      name: surface
    - label: Surface Interior Blend Only
      name: surfaceinside
    - label: Surface Exterior Blend Only
      name: surfaceoutside
    name: Fillmode
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
  - label: Thickness
    name: Thickness
  - label: Blending
    name: Blending
  status: beta
  variables:
  - label: SDF Surface
    name: sdf

---
