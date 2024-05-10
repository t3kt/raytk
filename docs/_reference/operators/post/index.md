---
layout: operatorCategory
title: Post Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/post/
cat:
  detail: Most or all of these are not standard RayTK operators that get connected
    into a renderer and add to the generated shader.
  name: post
  operators:
  - name: depthMap
    thumb: assets/images/reference/operators/post/depthMap_thumb.png
  - name: nearHitMap
    status: beta
    thumb: assets/images/reference/operators/post/nearHitMap_thumb.png
  - name: objectIdMask
  - name: stepMap
  - name: worldPosMap
    summary: Access the world position values from a raymarchRender3D, scaled to a
      normalized range.
  summary: Post processing operators are components that take information from a renderer
    and process it to produce images that can be used for post-processing.

---

# Post Operators

Post processing operators are components that take information from a renderer and process it to produce images that can be used for post-processing.

Most or all of these are not standard RayTK operators that get connected into a renderer and add to the generated shader.
