---
layout: operator
title: combineColumns
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineColumns
redirect_from:
  - /reference/opType/raytk.operators.combine.combineColumns/
op:
  category: combine
  inputs:
  - contextTypes:
    - none
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
    - float
    - Sdf
  - contextTypes:
    - none
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
    - float
    - Sdf
  - contextTypes:
    - none
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
  name: combineColumns
  opType: raytk.operators.combine.combineColumns
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
    summary: The number of columns in the blending region.
  - label: Radius
    name: Radius
    summary: The size of the blending region.
  - label: Inspect
    name: Inspect
  - label: Help
    name: Help
  summary: Columns SDF combine, producing n-1 circular columns/ridges at a 45 degree
    angles along the blend region.

---

# combineColumns

Category: combine



Columns SDF combine, producing n-1 circular columns/ridges at a 45 degree angles along the blend region.