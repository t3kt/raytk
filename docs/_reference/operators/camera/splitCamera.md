---
layout: operator
title: splitCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/splitCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.splitCamera/
op:
  name: splitCamera
  summary: A camera that splits the viewport into several zones, each using a separate camera.
  detail: |
    Important note that when the horizontal and vertical layouts currently only use the first two inputs.
  opType: raytk.operators.camera.splitCamera
  category: camera
  inputs:
    - name: definition_in_1
      label: Camera Input 1
      required: true
    - name: definition_in_2
      label: Camera Input 2
      required: false
    - name: definition_in_3
      label: Camera Input 3
      required: false
      summary: |
        This is only used by the grid layout.
    - name: definition_in_4
      label: Camera Input 4
      required: false
      summary: |
        This is only used by the grid layout.
  parameters:
    - name: Enable
      label: Enable
    - name: Layout
      label: Layout
      summary: |
        How to arrange the zones.
      menuOptions:
        - name: horz
          label: Horizontal
          description: |
            Output is split into two horizontal slices. When using this layout, only the first two inputs are used.
        - name: vert
          label: Vertical
          description: |
            Output is split into two vertical slices. When using this layout, only the first two inputs are used.
        - name: grid
          label: Grid
          description: |
            Output is arranged in a 2x2 grid.
    - name: Rescale
      label: Rescale
      summary: |
        Whether to rescale each camera to fit each zone. When switched off, if using a grid, you will only see the top right corner of the first camera, the top left of the second, etc. When switched on, you see the full view that each camera would normally get.
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# splitCamera

Category: camera



A camera that splits the viewport into several zones, each using a separate camera.

Important note that when the horizontal and vertical layouts currently only use the first two inputs.