---
layout: operator
title: hexagonalWeavePattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/hexagonalWeavePattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.hexagonalWeavePattern/
op:
  category: pattern
  detail: This pattern always produces colors (vectors), but the Format parameter
    controls how those colors are produced.
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
    summary: Field that produces vectors that the pattern uses as coordinates instead
      of regular spatial position. Only the X and Y parts are used.
    supportedVariableInputs:
    - thicknessField
    - blendingField
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
    summary: Field that controls the thickness of the edges between layers.
    supportedVariableInputs:
    - coordField
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
    summary: Field that controls the amount of blending between layers and edges.
    supportedVariableInputs:
    - coordField
    - thicknessField
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
    label: Color 1 Field / Replacement Color
    name: color1Field
    returnTypes:
    - float
    - vec4
    summary: Field providing either the color for layer 1 or the custom color for
      everywhere, depending on the selected Format.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    supportedVariables:
    - axialdist
    - mask
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
    label: Color 2 Field
    name: color2Field
    returnTypes:
    - float
    - vec4
    summary: Field providing the color for layer 2.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - color1Field
    supportedVariables:
    - axialdist
    - mask
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
    summary: Field providing the color for the background.
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - color1Field
    - color2Field
    supportedVariables:
    - axialdist
    - mask
  name: hexagonalWeavePattern
  opType: raytk.operators.pattern.hexagonalWeavePattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Two Layer
      name: twolayer
    name: Pattern
    readOnlyHandling: baked
    regularHandling: baked
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Moves the entire pattern.
  - label: Size
    name: Size
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Scales the pattern.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of each layer, where larger values produce smaller gaps.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of blending between layers and edges.
  - label: Randomize
    name: Randomize
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to weave the two layers together in a random arrangement, or
      always put one layer in front of the other.
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Seed number used to control randomization.
  - label: Format
    menuOptions:
    - description: Uses the color parameters to color layer 1, layer 2, and background.
      label: Color
      name: color
    - description: Uses the Color 1 field input for everything, relying on that field
        to use variables to differentiate between the different parts of the pattern.
      label: Custom Override Color
      name: customcolor
    name: Format
    readOnlyHandling: baked
    regularHandling: baked
    summary: What type of values are produced.
  - label: Color 1
    name: Color1
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The color to use for layer 1.
  - label: Color 2
    name: Color2
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The color to use for layer 2.
  - label: Background Color
    name: Bgcolor
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The color to use for the background behind both layers.
  summary: Pattern with two layers with gaps in a hexagonal layout.
  thumb: assets/images/reference/operators/pattern/hexagonalWeavePattern_thumb.png
  variables:
  - label: Axial Distances
    name: axialdist
  - label: Masks
    name: mask

---


Pattern with two layers with gaps in a hexagonal layout.

This pattern always produces colors (vectors), but the Format parameter controls how those colors are produced.