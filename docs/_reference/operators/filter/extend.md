---
layout: operator
title: extend
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/extend
redirect_from:
  - /reference/opType/raytk.operators.filter.extend/
op:
  category: filter
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
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - sizeField
    - centerField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    - vec3
    label: Size Field
    name: sizeField
    returnTypes:
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
    - vec2
    - vec3
    label: Center Field
    name: centerField
    returnTypes:
    - vec4
    supportedVariableInputs:
    - sizeField
  keywords:
  - extend
  - stretch
  name: extend
  opType: raytk.operators.filter.extend
  parameters:
  - label: Enable
    name: Enable
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The center position around which the coordinates are clamped.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of the region outside which the coordinates are clamped. Within
      this area, the SDF will behave as it normally does.
  - label: Axes
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: XZ
      name: xz
    - label: XYZ
      name: xyz
    name: Axes
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Which axes should be extended.
  summary: Clamps coordinates around an area, which causes its edges to be extended
    infinitely along each axis.
  thumb: assets/images/reference/operators/filter/extend_thumb.png

---


Clamps coordinates around an area, which causes its edges to be extended infinitely along each axis.