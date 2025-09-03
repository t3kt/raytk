---
layout: operator
title: tilingPattern
parent: Pattern Operators
grand_parent: Operators
permalink: /reference/operators/pattern/tilingPattern
redirect_from:
  - /reference/opType/raytk.operators.pattern.tilingPattern/
op:
  category: pattern
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Vertex Radius Field
    name: vertexRadiusField
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
    - VertexContext
    - PixelContext
    - PopContext
    coordTypes:
    - vec2
    - vec3
    label: Outline Thickness Field
    name: outlineThicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - coordField
    - vertexRadiusField
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
    - vec3
    label: Poly Color 1 Field
    name: polyColor1Field
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - vertexRadiusField
    - outlineThicknessField
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
    - vec3
    label: Poly Color 2 Field
    name: polyColor2Field
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - vertexRadiusField
    - outlineThicknessField
    - polyColor1Field
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
    - vec3
    label: Poly Color 3 Field
    name: polyColor3Field
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - vertexRadiusField
    - outlineThicknessField
    - polyColor1Field
    - polyColor2Field
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
    - vec3
    label: Outline Color Field
    name: outlineColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - vertexRadiusField
    - outlineThicknessField
    - polyColor1Field
    - polyColor2Field
    - polyColor3Field
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
    - vec3
    label: Dual Outline Color Field
    name: dualOutlineColorField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - coordField
    - vertexRadiusField
    - outlineThicknessField
    - polyColor1Field
    - polyColor2Field
    - polyColor3Field
    - outlineColorField
  name: tilingPattern
  opType: raytk.operators.pattern.tilingPattern
  parameters:
  - label: Pattern
    menuOptions:
    - label: Rhombitrihexagonal
      name: rhombitrihexagonal
    - label: Truncated Square
      name: truncatedsquare
    - label: Hexagonal
      name: hexagonal
    - label: Trihexagonal
      name: trihexagonal
    - label: Truncated Hexagonal
      name: truncatedhexagonal
    - label: Triangular
      name: triangular
    - label: Square
      name: square
    - label: Truncated Trihexagonal
      name: truncatedtrihexagonal
    - label: Snub Trihexagonal
      name: snubtrihexagonal
    - label: Snub Square
      name: snubsquare
    name: Pattern
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Format
    menuOptions:
    - label: Poly Color
      name: polycolor
    - label: Dual Tiling Poly Color
      name: dualpolycolor
    - label: Poly Number, Refl Side, Outline
      name: polyreflline
    name: Format
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
  - label: Vertex Radius
    name: Vertexradius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Outline Thickness
    name: Outlinethickness
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Outline Blending
    name: Outlineblending
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 1
    name: Polycolor1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 2
    name: Polycolor2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Poly Color 3
    name: Polycolor3
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Outline Color
    name: Outlinecolor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Dual Outline Color
    name: Dualoutlinecolor
    readOnlyHandling: baked
    regularHandling: runtime
  status: beta

---
