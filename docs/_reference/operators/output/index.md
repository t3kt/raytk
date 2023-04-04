---
layout: operatorCategory
title: Output Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/output/
cat:
  detail: 'The most common one is `raymarchRender3d`, which takes in a chain of OPs

    that produces an SDF in 3D space, and applies raymarching to render an

    image.'
  name: output
  operators:
  - name: fieldRender
    status: beta
  - name: functionGraphRender
    summary: Visualizes the graph of a function operator.
  - keywords:
    - point
    - render
    - volumetric
    name: pointMapRender
    shortcuts:
    - pmr
    summary: Renderer that takes in a TOP of coordinates and evaluates the scene at
      each point.
  - keywords:
    - inspect
    - preview
    - raymarch
    - render
    name: raymarchPreviewPanel
    status: beta
  - name: raymarchRender3D
    shortcuts:
    - rr3
    summary: Renders a scene using 3D raymarching.
  - name: render2D
    shortcuts:
    - r2
    summary: Renders a 2D image by evaluating the input field for each pixel.
  - name: renderSelect
    summary: Accesses a color output buffer from a renderer.
  summary: 'Outputs are a special category of operator that takes in one or more

    chains of OPs, generate a shader, and run it to produce some sort of

    output.'

---

# Output Operators

Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.

The most common one is `raymarchRender3d`, which takes in a chain of OPs
that produces an SDF in 3D space, and applies raymarching to render an
image.
