---
layout: operator
title: combineStairs
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineStairs
redirect_from:
  - /reference/opType/raytk.operators.combine.combineStairs/
op:
  category: combine
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: definition_in_1
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
    coordTypes:
    - vec2
    - vec3
    label: definition_in_2
    name: definition_in_2
    required: true
    returnTypes:
    - Sdf
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius of the blend region at
      different points in space, by *multiplying* the value of the `Radius` parameter.
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec2
    - vec3
    label: Offset Field
    name: offset_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the offset of the stairs at different
      points in space, by *adding* to the value of the `Offset` parameter.
  name: combineStairs
  opType: raytk.operators.combine.combineStairs
  parameters:
  - label: Enable
    name: Enable
  - label: Operation
    menuOptions:
    - description: Produces the combined area of both inputs.
      label: Union
      name: union
    - description: Produces the area where both inputs overlap.
      label: Intersect
      name: intersect
    - description: Subtracts the second input from the first.
      label: Difference
      name: diff
    name: Operation
    summary: The type of combine operation.
  - label: Swap Inputs
    name: Swapinputs
    summary: Swaps the order of the inputs. This is only used for the `diff` mode.
  - label: Number
    name: Number
    summary: The number of steps in the blending region.
  - label: Radius
    name: Radius
    summary: The size of the blending region.
  - label: Offset
    name: Offset
    summary: Shifts the steps along the blend region, with 0 being no shift, and 1
      being a full shift of the total number of steps.
  summary: Stair SDF combine, producing steps along the blend region.

---


Stair SDF combine, producing steps along the blend region.