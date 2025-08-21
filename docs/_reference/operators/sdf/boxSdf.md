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
    - VertexContext
    - PixelContext
    - PopContext
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
  - menuOptions:
    - description: A bit more efficient but slightly less accurate.
      name: boxcheap
    - description: More accurate but slightly less efficient.
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
    readOnlyHandling: runtime
    regularHandling: runtime
    summary: Axis along which the box should stretch infinitely.
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Move the center of the box.
  - label: Scale
    name: Scale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the box in each dimension.
  - label: Uniform Scale
    name: Uniformscale
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scaling applied to all dimensions of the `Scale`.
  - label: UV Mode
    menuOptions:
    - label: None
      name: none
    - label: Bounds XYZ
      name: bounds
    - label: Faces
      name: faces
    name: Uvmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Optimize
    name: Optimize
  shortcuts:
  - box
  summary: SDF for a box, optionally infinite one one axis.
  thumb: assets/images/reference/operators/sdf/boxSdf_thumb.png

---


SDF for a box, optionally infinite one one axis.