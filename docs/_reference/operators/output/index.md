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
  - name: customRender
    status: beta
  - name: fieldRender
    thumb: assets/images/reference/operators/output/fieldRender_thumb.png
  - name: functionGraphRender
    summary: Visualizes the graph of a function operator.
    thumb: assets/images/reference/operators/output/functionGraphRender_thumb.png
  - keywords:
    - point
    - render
    - volumetric
    name: pointMapRender
    shortcuts:
    - pmr
    summary: Renderer that takes in a TOP of coordinates and evaluates the scene at
      each point.
    thumb: assets/images/reference/operators/output/pointMapRender_thumb.png
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
    thumb: assets/images/reference/operators/output/render2D_material_thumb.png
  - name: renderSelect
    summary: Accesses a color output buffer from a renderer.
  - keywords:
    - volume
    moduleName: raytkVolumes
    name: texture3dRender
    status: beta
    summary: Renderer that produces 3D textures that sample SDFs, Volumes, or fields.
  - moduleName: raytkVolumes
    name: volumetricRaymarchRender3D
    status: beta
    summary: Renderer that uses raymarching with volumes instead of SDFs.
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
