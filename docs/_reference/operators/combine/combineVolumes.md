---
layout: operator
title: combineVolumes
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineVolumes
redirect_from:
  - /reference/opType/raytkVolumes.operators.combine.combineVolumes/
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
    - vec3
    label: Volume 1
    name: definition_in_1
    returnTypes:
    - Volume
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
    label: Volume 2
    name: definition_in_2
    returnTypes:
    - Volume
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
    label: Volume 2
    name: definition_in_3
    returnTypes:
    - Volume
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
    label: Volume 2
    name: definition_in_4
    returnTypes:
    - Volume
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
    label: Volume 1
    name: definition_in_5
    returnTypes:
    - Volume
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
    label: Volume 2
    name: definition_in_6
    returnTypes:
    - Volume
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
    label: Volume 2
    name: definition_in_7
    returnTypes:
    - Volume
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
    label: Volume 2
    name: definition_in_8
    returnTypes:
    - Volume
  moduleName: raytkVolumes
  name: combineVolumes
  opType: raytkVolumes.operators.combine.combineVolumes
  parameters:
  - label: Enable
    name: Enable
  - label: Density Mode
    menuOptions:
    - label: Add
      name: add
    - label: Subtract
      name: sub
    - label: Multiply
      name: mul
    - label: Divide
      name: div
    - label: Average
      name: avg
    - label: Minimum
      name: min
    - label: Maximum
      name: max
    name: Densitymode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Color Mode
    menuOptions:
    - label: Add
      name: add
    - label: Subtract
      name: sub
    - label: Multiply
      name: mul
    - label: Divide
      name: div
    - label: Average
      name: avg
    - label: Input 1
      name: input1
    - label: Input 2
      name: input2
    name: Colormode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  status: beta

---
