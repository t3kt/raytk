---
layout: operator
title: eggSdf2d
parent: Sdf2d Operators
grand_parent: Operators
permalink: /reference/operators/sdf2d/eggSdf2d
redirect_from:
  - /reference/opType/raytk.operators.sdf2d.eggSdf2d/
op:
  category: sdf2d
  inputs:
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Point 1 Field
    name: point1Field
    returnTypes:
    - vec4
    supportedVariableInputs:
    - radiusField
    - roundingField
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Point 2 Field
    name: point2Field
    returnTypes:
    - vec4
    supportedVariableInputs:
    - radiusField
    - roundingField
    - point1Field
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - vec2
    label: Bulge Field
    name: bulgeField
    returnTypes:
    - float
    supportedVariableInputs:
    - radiusField
    - roundingField
    - point1Field
    - point2Field
  name: eggSdf2d
  opType: raytk.operators.sdf2d.eggSdf2d
  parameters:
  - label: Shape
    menuOptions:
    - label: Egg
      name: egg
    - label: Uneven Egg
      name: unevenEgg
    name: Shape
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rounding
    name: Rounding
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 1
    name: Point1
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Point 2
    name: Point2
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Bulge
    name: Bulge
    readOnlyHandling: baked
    regularHandling: runtime
  thumb: assets/images/reference/operators/sdf2d/eggSdf2d_thumb.png

---
