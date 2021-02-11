---
layout: operator
title: linkedCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/linkedCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.linkedCamera/
op:
  category: camera
  detail: 'The camera will match the view of the TD camera, including local and world
    transformations, FOV settings, etc.

    It can be used to combine a raymarchRender3d with a traditional TD render TOP.'
  name: linkedCamera
  opType: raytk.operators.camera.linkedCamera
  parameters:
  - label: Camera
    name: Camera
    summary: The camera to match. This can either be a Camera COMP, or an arcBallCamera,
      or the `camera` from the palette.
  - label: Create Camera
    name: Createcamera
    summary: Creates and attaches an instance of the `camera` palette component.
  - label: Create Basic Camera
    name: Createbasiccamera
    summary: Creates and attaches a standard Camera COMP.
  summary: A camera that is linked to an existing TD Camera COMP.

---

# linkedCamera

Category: camera



A camera that is linked to an existing TD Camera COMP.

The camera will match the view of the TD camera, including local and world transformations, FOV settings, etc.
It can be used to combine a raymarchRender3d with a traditional TD render TOP.