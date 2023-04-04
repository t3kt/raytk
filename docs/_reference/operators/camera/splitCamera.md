---
layout: operator
title: splitCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/splitCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.splitCamera/
op:
  category: camera
  detail: Important note that when the horizontal and vertical layouts currently only
    use the first two inputs.
  inputs:
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera Input 1
    name: definition_in_1
    required: true
    returnTypes:
    - Ray
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera Input 2
    name: definition_in_2
    returnTypes:
    - Ray
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera Input 3
    name: definition_in_3
    returnTypes:
    - Ray
    summary: This is only used by the grid layout.
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera Input 4
    name: definition_in_4
    returnTypes:
    - Ray
    summary: This is only used by the grid layout.
  name: splitCamera
  opType: raytk.operators.camera.splitCamera
  parameters:
  - label: Enable
    name: Enable
  - label: Layout
    menuOptions:
    - description: Output is split into two horizontal slices. When using this layout,
        only the first two inputs are used.
      label: Horizontal
      name: horz
    - description: Output is split into two vertical slices. When using this layout,
        only the first two inputs are used.
      label: Vertical
      name: vert
    - description: Output is arranged in a 2x2 grid.
      label: Grid
      name: grid
    name: Layout
    summary: How to arrange the zones.
  - label: Rescale
    name: Rescale
    summary: Whether to rescale each camera to fit each zone. When switched off, if
      using a grid, you will only see the top right corner of the first camera, the
      top left of the second, etc. When switched on, you see the full view that each
      camera would normally get.
  - label: Camera Map
    name: Cameramap
    summary: Texture that switches between cameras on a per-pixel basis. Values are
      scaled from 0..1 to 0..(N-1), where N is the number of connected inputs. So
      if there are 4 connected inputs, 0..0.249999.. is input 1, 0.25..0.49999.. is
      input 2, etc.
  summary: A camera that splits the viewport into several zones, each using a separate
    camera.
  thumb: assets/images/reference/operators/camera/splitCamera_thumb.png
  variables:
  - label: index
    name: index

---


A camera that splits the viewport into several zones, each using a separate camera.

Important note that when the horizontal and vertical layouts currently only use the first two inputs.