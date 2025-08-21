---
layout: operator
title: edgeCombine
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/edgeCombine
redirect_from:
  - /reference/opType/raytk.operators.combine.edgeCombine/
op:
  category: combine
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 1
    name: definition_in_1
    required: true
    returnTypes:
    - Sdf
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
    - float
    - vec2
    - vec3
    - vec4
    label: SDF 2
    name: definition_in_2
    required: true
    returnTypes:
    - Sdf
    supportedVariableInputs:
    - inputOp1
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
    - float
    - vec2
    - vec3
    - vec4
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp[1-2]
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
    - float
    - vec2
    - vec3
    - vec4
    label: Depth Field
    name: depthField
    returnTypes:
    - float
    supportedVariableInputs:
    - inputOp[1-2]
    - radiusField
  name: edgeCombine
  opType: raytk.operators.combine.edgeCombine
  parameters:
  - label: Enable
    name: Enable
  - label: Combine
    menuOptions:
    - label: Engrave
      name: engrave
    - label: Groove
      name: groove
    - label: Tongue
      name: tongue
    - label: Pipe
      name: pipe
    name: Combine
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Swap Inputs
    name: Swapinputs
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Width of the edge overlap area.
  - label: Depth
    name: Depth
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Depth of the groove / tongue.
  summary: Combines two SDFs in ways that use the intersection areas.
  thumb: assets/images/reference/operators/combine/edgeCombine_thumb.png

---


Combines two SDFs in ways that use the intersection areas.