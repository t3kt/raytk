---
layout: operator
title: boxSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/boxSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.boxSdf/
op:
  category: sdf
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scale_definition_in
    returnTypes:
    - float
    - vec4
  name: boxSdf
  opType: raytk.operators.sdf.boxSdf
  parameters:
  - label: Box Type
    menuOptions:
    - description: A bit more efficient but slightly less accurate.
      label: Box Cheap
      name: boxcheap
    - description: More accurate but slightly less efficient.
      label: Box
      name: box
    name: Boxtype
    summary: The type of box function.
  - label: Infinite Axis
    menuOptions:
    - description: Regular box.
      label: None
      name: none
    - description: Box is infinite along the x axis.
      label: X
      name: x
    - description: Box is infinite along the y axis.
      label: Y
      name: y
    - description: Box is infinite along the z axis.
      label: Z
      name: z
    name: Infiniteaxis
    summary: Axis along which the box should stretch infinitely.
  - label: Translate
    name: Translate
    summary: Move the center of the box.
  - label: Scale
    name: Scale
    summary: The size of the box in each dimension.
  - label: Uniform Scale
    name: Uniformscale
    summary: Scaling applied to all dimensions of the `Scale`.
  - label: Context Type
    menuOptions:
    - label: Auto
      name: auto
    - label: Context
      name: Context
    - label: MaterialContext
      name: MaterialContext
    - label: CameraContext
      name: CameraContext
    - label: LightContext
      name: LightContext
    - label: RayContext
      name: RayContext
    name: Contexttype
  summary: SDF for a box, optionally infinite one one axis.

---


SDF for a box, optionally infinite one one axis.