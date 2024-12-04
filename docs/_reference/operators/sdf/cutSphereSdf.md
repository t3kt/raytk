---
layout: operator
title: cutSphereSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/cutSphereSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.cutSphereSdf/
op:
  category: sdf
  detail: Based on [CutSphere - distance 3D](https://www.shadertoy.com/view/stKSzc)
    by iq, and [Segment on Sphere SDF](https://www.shadertoy.com/view/lfcyDM) by SnoopethDuckDuck.
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
    - vec3
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - thicknessField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Max Angle Field
    name: maxAngleField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - thicknessField
    - offsetField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec3
    label: Rotate Field
    name: rotateField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - radiusField
    - thicknessField
    - offsetField
    - maxAngleField
  name: cutSphereSdf
  opType: raytk.operators.sdf.cutSphereSdf
  parameters:
  - label: Shape
    menuOptions:
    - label: Solid
      name: solid
    - label: Hollow
      name: hollow
    - label: Segment
      name: segment
    name: Shape
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether the sphere should be solid or a hollow shell.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Radius of the sphere.
  - label: Cut Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How far across the sphere the cut plane should be.
  - label: Thickness
    name: Thickness
    summary: Thickness of the shape if using hollow mode.
  - label: Rotate
    name: Rotate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Max Angle
    name: Maxangle
  summary: Sphere with part of it cut off, either solid or hollow.
  thumb: assets/images/reference/operators/sdf/cutSphereSdf_thumb.png

---


Sphere with part of it cut off, either solid or hollow.

Based on [CutSphere - distance 3D](https://www.shadertoy.com/view/stKSzc) by iq, and [Segment on Sphere SDF](https://www.shadertoy.com/view/lfcyDM) by SnoopethDuckDuck.