---
layout: operatorCategory
title: Output Operators
parent: Operators
has_children: true
has_toc: false
permalink: /reference/operators/output/
cat:
  name: output
  summary: |
    Outputs are a special category of operator that takes in one or more
    chains of OPs, generate a shader, and run it to produce some sort of
    output.
  detail: |
    The most common one is `raymarchRender3d`, which takes in a chain of OPs
    that produces an SDF in 3D space, and applies raymarching to render an
    image.
  operators:
    - op:
      name: functionGraphRender
      summary: Visualizes the graph of a function operator.
    - op:
      name: pointMapRender
      status: beta
    - op:
      name: raymarchRender3D
      summary: Renders a scene using 3D raymarching.
    - op:
      name: render2D
    - op:
      name: renderSelect

---

# Output Operators

Outputs are a special category of operator that takes in one or more
chains of OPs, generate a shader, and run it to produce some sort of
output.

The most common one is `raymarchRender3d`, which takes in a chain of OPs
that produces an SDF in 3D space, and applies raymarching to render an
image.
