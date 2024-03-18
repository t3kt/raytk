---
layout: operator
title: subdivisionSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/subdivisionSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.subdivisionSdf2d/
op:
  category: sdf2d
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
    - vec2
    label: Seed Field
    name: seedField
    returnTypes:
    - float
    supportedVariables:
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid
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
    - vec2
    label: Size Field
    name: sizeField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - seedField
    supportedVariables:
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid
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
    - vec2
    label: Minimum Size Field
    name: minSizeField
    returnTypes:
    - float
    supportedVariableInputs:
    - seedField
    - sizeField
    supportedVariables:
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid
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
    - vec2
    label: Pattern Shift Field
    name: patternShiftField
    returnTypes:
    - float
    supportedVariableInputs:
    - seedField
    - sizeField
    - minSizeField
    supportedVariables:
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid
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
    - vec2
    label: Shape SDF
    name: shape
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - seedField
    - sizeField
    - minSizeField
    - patternShiftField
    supportedVariables:
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
    - RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid
  name: subdivisionSdf2d
  opType: raytk.operators.sdf2d.subdivisionSdf2d
  parameters:
  - label: Iterations
    name: Iterations
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Pattern Shift
    name: Patternshift
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Minimum Size
    name: Minsize
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/sdf2d/subdivisionSdf2d_thumb.png
  variables:
  - label: RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
    name: RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellsize
  - label: RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid
    name: RTK_raytk_operators_sdf2d_subdivisionSdf2d_cellid

---
