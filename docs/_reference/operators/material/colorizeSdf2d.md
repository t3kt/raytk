---
layout: operator
title: colorizeSdf2d
parent: Material Operators
grand_parent: Operators
permalink: /reference/operators/material/colorizeSdf2d
redirect_from:
  - /reference/opType/raytk.operators.material.colorizeSdf2d/
op:
  category: material
  detail: 'This pattern is useful for debugging purposes.

    While this is not a regular "material", it is used to convert an SDF to a color
    output.'
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - ParticleContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF
    name: definition_in
    required: true
    returnTypes:
    - float
    - Sdf
  name: colorizeSdf2d
  opType: raytk.operators.material.colorizeSdf2d
  parameters:
  - label: Enable
    name: Enable
  - label: Enable Edge
    name: Enableedge
    summary: Whether to show a border at the suface of the shape.
  - label: Edge Thickness
    name: Edgethickness
    summary: Thickness of the shape border.
  - label: Edge Blending
    name: Edgeblending
    summary: Amount of blending applied to each side of the shape border.
  - label: Edge Color
    name: Edgecolor
    summary: The color for the shape border.
  - label: Inside Period
    name: Insideperiod
    summary: The tightness of the stripes inside the shape.
  - label: Inside Color 1
    name: Insidecolor1
    summary: The first stripe color inside the shape.
  - label: Inside Color 2
    name: Insidecolor2
    summary: The second stripe color inside the shape.
  - label: Outside Period
    name: Outsideperiod
    summary: The tightness fo the stripes outside the shape.
  - label: Outside Color 1
    name: Outsidecolor1
    summary: The first stripe color outside the shape.
  - label: Outside Color 2
    name: Outsidecolor2
    summary: The second stripe color outside the shape.
  - label: Inside Phase
    name: Insidephase
  - label: Outside Phase
    name: Outsidephase
  summary: Converts a 2D SDF to a striped distance pattern.

---


Converts a 2D SDF to a striped distance pattern.

This pattern is useful for debugging purposes.
While this is not a regular "material", it is used to convert an SDF to a color output.