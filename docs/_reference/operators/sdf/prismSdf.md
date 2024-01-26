---
layout: operator
title: prismSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/prismSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.prismSdf/
op:
  category: sdf
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
    - vec3
    label: Height field
    name: heightField
    returnTypes:
    - float
    summary: Float value field that controls the height of the prism.
    supportedVariables:
    - axispos
    - normangle
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
    - vec3
    label: Radius field
    name: radiusField
    returnTypes:
    - float
    summary: Float value field that controls the radius of the prism.
    supportedVariableInputs:
    - heightField
    supportedVariables:
    - axispos
    - normangle
    - normoffset
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
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - radiusField
    supportedVariables:
    - axispos
    - normangle
    - normoffset
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
    - vec3
    label: Sides Field
    name: sidesField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - radiusField
    - thicknessField
    supportedVariables:
    - axispos
    - normangle
    - normoffset
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
    - vec3
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - radiusField
    - thicknessField
    - sidesField
    supportedVariables:
    - axispos
    - normangle
    - normoffset
  keywords:
  - column
  - cylinder
  - hexagon
  - octagon
  - prism
  - square
  - triangle
  name: prismSdf
  opType: raytk.operators.sdf.prismSdf
  parameters:
  - label: Prism Type
    menuOptions:
    - label: Triangle
      name: tri
    - label: Square
      name: square
    - label: Hexagon
      name: hex
    - label: Octogon
      name: octogon
    - label: Custom
      name: custom
    name: Prismtype
    summary: The number of sides of the prism.
  - label: Translate
    name: Translate
    summary: Moves the center of the prism.
  - label: Radius
    name: Radius
    summary: The radius of the prism. If the radius field input is connected, this
      is not used.
  - label: Height
    name: Height
    summary: The height / length of the prism. If the height field input, this is
      not used.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
  - label: Sides
    name: Sides
  - label: Rounding
    name: Rounding
  - label: Infinite Height
    name: Infiniteheight
  - label: Hollow
    name: Hollow
  - label: Thickness
    name: Thickness
  - label: UV Mode
    menuOptions:
    - label: Cylindrical
      name: cylindrical
    - label: Corner-Aligned Cylindrical
      name: cornercylindrical
    - label: Faces
      name: faces
    name: Uvmode
  summary: A prism shape, like a cylinder but with flat sides, along the z axis.
  thumb: assets/images/reference/operators/sdf/prismSdf_thumb.png
  variables:
  - label: axispos
    name: axispos
  - label: normoffset
    name: normoffset
  - label: normangle
    name: normangle

---


A prism shape, like a cylinder but with flat sides, along the z axis.