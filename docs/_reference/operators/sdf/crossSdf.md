---
layout: operator
title: crossSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/crossSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.crossSdf/
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
    coordTypes:
    - vec3
    label: Scale Field
    name: sizeField
    returnTypes:
    - float
    - vec4
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
    label: Smooth Radius Field
    name: smoothRadiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - sizeField
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
    label: Length Field
    name: lengthField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - sizeField
    - smoothRadiusField
  name: crossSdf
  opType: raytk.operators.sdf.crossSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the center of the cross.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The width of the arms of the cross.
  - label: Smooth Radius
    name: Smoothradius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Smoothing applied to the intersections of the arms.
  - label: Axes
    menuOptions:
    - label: All Axes
      name: xyz
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    name: Axes
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Which axes to include in the cross.
  - label: Shape
    menuOptions:
    - label: Infinite
      name: infinite
    - label: Limited XYZ
      name: limitxyz
    name: Shape
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to make the cross have infinite length or limited lengths.
  - label: Length
    name: Length
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Length of the cross on each axis.
  summary: An SDF for a 3D cross along each axis, with either infinite or limited
    length.
  thumb: assets/images/reference/operators/sdf/crossSdf_thumb.png

---


An SDF for a 3D cross along each axis, with either infinite or limited length.