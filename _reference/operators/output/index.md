---
layout: page
title: Output Operators
parent: Operators
has_children: true
has_toc: false
---

Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.

The most common one is `raymarchRender3d`, which takes in a chain of OPs
that produces an SDF in 3D space, and applies raymarching to render an
image.

* [`customRender`](customRender/) - 
* [`functionGraphRender`](functionGraphRender/) - 
* [`pointMapRender`](pointMapRender/) - 
* [`raymarchRender3D`](raymarchRender3D/) - 
* [`render2D`](render2D/) - 
* [`renderSelect`](renderSelect/) -
