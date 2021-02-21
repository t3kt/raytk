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
  - name: functionGraphRender
    summary: Visualizes the graph of a function operator.
  - name: pointMapRender
    status: beta
  - name: raymarchRender3D
    summary: Renders a scene using 3D raymarching.
  - name: render2D
    summary: Renders a 2D image by evaluating the input field for each pixel.
  - name: renderSelect
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
