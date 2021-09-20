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
    - ParticleContext
    coordTypes:
    - vec3
    label: Scale Field
    name: scaleField
    returnTypes:
    - float
    - vec4
  keywords:
  - box
  - cube
  - rectangle
  - square
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
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds XYZ
      name: bounds
    name: Uvmode
  summary: SDF for a box, optionally infinite one one axis.

---


SDF for a box, optionally infinite one one axis.