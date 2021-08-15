---
layout: operator
title: combineChamfer
parent: Combine Operators
grand_parent: Operators
permalink: /reference/operators/combine/combineChamfer
redirect_from:
  - /reference/opType/raytk.operators.combine.combineChamfer/
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
    - float
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
    - float
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
    - float
    - vec2
    - vec3
    label: Radius Field
    name: radius_definition_in
    returnTypes:
    - float
    summary: Value field that can be used to vary the radius of the blend region at
      different points in space, by *multiplying* the value of the `Radius` parameter.
  name: combineChamfer
  opType: raytk.operators.combine.combineChamfer
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
  - label: Radius
    name: Radius
    summary: The size of the blending region.
  summary: Chamfer SDF combine, producing a flat surface at a 45 degree angle along
    the blend region.

---


Chamfer SDF combine, producing a flat surface at a 45 degree angle along the blend region.