---
layout: page
title: linkedCamera
parent: Camera Operators
grand_parent: Operators
permalink: /reference/operators/camera/linkedCamera
redirect_from:
  - /reference/opType/raytk.operators.camera.linkedCamera/
---

# linkedCamera

Category: camera



A camera that is linked to an existing TD Camera COMP.

The camera will match the view of the TD camera, including local and world transformations, FOV settings, etc.
It can be used to combine a raymarchRender3d with a traditional TD render TOP.

## Parameters

* `Camera` *Camera*: The camera to match. This can either be a Camera COMP, or an arcBallCamera, or the `camera` from the palette.
* `Help` *Help*