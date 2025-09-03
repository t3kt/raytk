---
layout: operator
title: sweep
parent: Convert Operators
grand_parent: Operators
permalink: /reference/operators/convert/sweep
redirect_from:
  - /reference/opType/raytk.operators.convert.sweep/
op:
  category: convert
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    label: Cross-Section SDF
    name: crossSection
    required: true
    returnTypes:
    - float
    - vec4
    - Sdf
    summary: The SDF that sweeps around the path SDF.
    supportedVariableInputs:
    - cross_section_definition_in
    - path_definition_in
    supportedVariables:
    - pathsdf
    - pathpos
    - pos3d
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    label: Path SDF
    name: path
    required: true
    returnTypes:
    - float
    - Sdf
    summary: The SDF around which the cross-section SDF sweeps.
  name: sweep
  opType: raytk.operators.convert.sweep
  parameters:
  - label: Plane
    menuOptions:
    - label: XY
      name: xy
    - label: YX
      name: yx
    - label: YZ
      name: yz
    - label: ZY
      name: zy
    - label: XZ
      name: xz
    - label: ZX
      name: zx
    name: Plane
    readOnlyHandling: semibaked
    regularHandling: runtime
  summary: Creates a 3D SDF by sweeping a 2D SDF along the surface of another 2D SDF.
  thumb: assets/images/reference/operators/convert/sweep_thumb.png
  variables:
  - label: Path SDF
    name: pathsdf
  - label: Path Position
    name: pathpos
  - label: 3D Position
    name: pos3d

---


Creates a 3D SDF by sweeping a 2D SDF along the surface of another 2D SDF.