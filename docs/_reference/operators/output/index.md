---
layout: page
title: Output Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/output/
---

# Output Operators

Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.

The most common one is `raymarchRender3d`, which takes in a chain of OPs
that produces an SDF in 3D space, and applies raymarching to render an
image.

* [`functionGraphRender`](functionGraphRender/) - Visualizes the graph of a function operator.
* [`pointMapRender`](pointMapRender/) - 
* [`raymarchRender3D`](raymarchRender3D/) - Renders a scene using 3D raymarching.
* [`render2D`](render2D/) - 
* [`renderSelect`](renderSelect/) - 
