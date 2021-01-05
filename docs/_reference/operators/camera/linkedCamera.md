---
layout: operator
title: linkedCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/linkedCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.linkedCamera/
op:
  name: linkedCamera
  summary: A camera that is linked to an existing TD Camera COMP.
  detail: |
    The camera will match the view of the TD camera, including local and world transformations, FOV settings, etc.
    It can be used to combine a raymarchRender3d with a traditional TD render TOP.
  opType: raytk.operators.camera.linkedCamera
  category: camera
  parameters:
    - name: Camera
      label: Camera
      summary: |
        The camera to match. This can either be a Camera COMP, or an arcBallCamera, or the `camera` from the palette.
    - name: Createcamera
      label: Create Camera
      summary: |
        Creates and attaches an instance of the `camera` palette component.
    - name: Createbasiccamera
      label: Create Basic Camera
      summary: |
        Creates and attaches a standard Camera COMP.
    - name: Help
      label: Help

---

# linkedCamera

Category: camera



A camera that is linked to an existing TD Camera COMP.

The camera will match the view of the TD camera, including local and world transformations, FOV settings, etc.
It can be used to combine a raymarchRender3d with a traditional TD render TOP.