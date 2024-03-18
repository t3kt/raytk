---
layout: operator
title: truchetPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/truchetPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.truchetPattern/
op:
  category: pattern
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
    - vec2
    - vec3
    label: Coordinate Field
    name: coordField
    returnTypes:
    - vec4
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
    - vec2
    - vec3
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    supportedVariables:
    - cell
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
    - vec2
    - vec3
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - thicknessField
    supportedVariables:
    - cell
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
    - vec2
    - vec3
    label: Curve Field
    name: curveField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    supportedVariables:
    - cell
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
    - vec2
    - vec3
    label: Path Color Field / Custom Color Field
    name: pathColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - curveField
    supportedVariables:
    - cell
    - edgedist
    - contour
    - depth
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
    - vec2
    - vec3
    label: Background Color Field
    name: bgColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - curveField
    - pathColorField
    supportedVariables:
    - cell
    - edgedist
    - contour
    - depth
    - normangle
  name: truchetPattern
  opType: raytk.operators.pattern.truchetPattern
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Curve
    name: Curve
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Format
    menuOptions:
    - label: Contour
      name: contour
    - label: Edge Distance
      name: edgedist
    - label: Color & Depth
      name: colordepth
    - label: Color & Depth * Contour
      name: colordepthcontour
    - label: Custom Override Color
      name: customcolor
    name: Format
    readOnlyHandling: baked
    regularHandling: baked
  - label: Path Color
    name: Pathcolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Background Color
    name: Bgcolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta
  thumb: assets/images/reference/operators/pattern/truchetPattern_thumb.png
  variables:
  - label: RTK_raytk_operators_pattern_truchetPattern_cell
    name: RTK_raytk_operators_pattern_truchetPattern_cell
  - label: RTK_raytk_operators_pattern_truchetPattern_contour
    name: RTK_raytk_operators_pattern_truchetPattern_contour
  - label: RTK_raytk_operators_pattern_truchetPattern_normangle
    name: RTK_raytk_operators_pattern_truchetPattern_normangle
  - label: RTK_raytk_operators_pattern_truchetPattern_depth
    name: RTK_raytk_operators_pattern_truchetPattern_depth
  - label: RTK_raytk_operators_pattern_truchetPattern_edgedist
    name: RTK_raytk_operators_pattern_truchetPattern_edgedist

---
