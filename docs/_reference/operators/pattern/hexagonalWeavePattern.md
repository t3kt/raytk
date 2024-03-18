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
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    supportedVariables:
    - RTK_raytk_operators_pattern_hexagonalWeavePattern_axialdist
    - RTK_raytk_operators_pattern_hexagonalWeavePattern_mask
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
    supportedVariableInputs:
    - coordField
    - thicknessField
    - blendingField
    - color1Field
    supportedVariables:
    - RTK_raytk_operators_pattern_hexagonalWeavePattern_axialdist
    - RTK_raytk_operators_pattern_hexagonalWeavePattern_mask
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
    - color1Field
    - color2Field
    supportedVariables:
    - RTK_raytk_operators_pattern_hexagonalWeavePattern_axialdist
    - RTK_raytk_operators_pattern_hexagonalWeavePattern_mask
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
  - label: Size
    name: Size
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
  - label: Randomize
    name: Randomize
    readOnlyHandling: baked
    regularHandling: baked
  - label: Seed
    name: Seed
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Format
    menuOptions:
    - label: Color
      name: color
    - label: Custom Override Color
      name: customcolor
    name: Format
    readOnlyHandling: baked
    regularHandling: baked
  - label: Color 1
    name: Color1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Color 2
    name: Color2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Background Color
    name: Bgcolor
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/pattern/hexagonalWeavePattern_thumb.png
  variables:
  - label: RTK_raytk_operators_pattern_hexagonalWeavePattern_axialdist
    name: RTK_raytk_operators_pattern_hexagonalWeavePattern_axialdist
  - label: RTK_raytk_operators_pattern_hexagonalWeavePattern_mask
    name: RTK_raytk_operators_pattern_hexagonalWeavePattern_mask

---
