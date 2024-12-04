---
layout: operator
title: mirrorAxes
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/mirrorAxes
redirect_from:
  - /reference/opType/raytk.operators.filter.mirrorAxes/
op:
  category: filter
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
    - float
    - vec2
    - vec3
    - vec4
    label: definition_in
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    - Volume
    - Ray
    - Light
    supportedVariableInputs:
    - offsetField
    - directionField
    - flipSideField
    - blendingField
    supportedVariables:
    - sides
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - directionField
    - flipSideField
    supportedVariables:
    - sides
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Direction Field
    name: directionField
    returnTypes:
    - float
    - vec4
    supportedVariableInputs:
    - flipSidesField
    supportedVariables:
    - sides
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Flip Sides Field
    name: flipSideField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - sides
  - contextTypes:
    - Context
    - MaterialContext
    - CameraContext
    - LightContext
    - RayContext
    - VertexContext
    - PixelContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Blending Field
    name: blendingField
    returnTypes:
    - float
    - vec4
    supportedVariables:
    - sides
  name: mirrorAxes
  opType: raytk.operators.filter.mirrorAxes
  parameters:
  - label: Enable
    name: Enable
  - label: Axes
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    - label: XY
      name: xy
    - label: YZ
      name: yz
    - label: ZX
      name: zx
    - label: XYZ
      name: xyz
    name: Axes
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which axes should be reflected.
  - label: Direction X
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Dirx
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which side of the X axis should be reflected.
  - label: Direction Y
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Diry
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which side of the Y axis should be reflected.
  - label: Direction Z
    menuOptions:
    - label: Positive
      name: pos
    - label: Negative
      name: neg
    name: Dirz
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which side of the Z axis should be reflected.
  - label: Flip X On Side
    menuOptions:
    - label: None
      name: none
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Flipsidex
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to flip one side of the X axis along either the Y or Z axes.
  - label: Flip Y On Side
    menuOptions:
    - label: None
      name: none
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Flipsidey
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to flip one side of the Y axis along either the X or Z axes.
  - label: Flip Z On Side
    menuOptions:
    - label: None
      name: none
    - label: X+
      name: xpos
    - label: X-
      name: xneg
    - label: Y+
      name: ypos
    - label: Y-
      name: yneg
    - label: Z+
      name: zpos
    - label: Z-
      name: zneg
    name: Flipsidez
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to flip one side of the Z axis along either the X or Y axes.
  - label: Center
    name: Center
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Center position for the reflection planes.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Offset applied to each side, pushing them towards / away from the reflection
      planes.
  - label: Enable Blend
    name: Enableblend
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to stretch out the area near the reflection plane to soften the
      transition between the sides.
  - label: Blending
    name: Blending
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How much area to stretch out near the reflection planes.
  - label: Apply To
    menuOptions:
    - label: Coordinates
      name: coords
    - label: SDF UV
      name: sdfuv
    - label: SDF Secondary UV
      name: sdfuv2
    - label: UV In Material
      name: matuv
    - label: Field Values
      name: value
    name: Target
    summary: What the reflection should be applied to.
  summary: Mirror space across one or more axes, similar to `reflect`.
  thumb: assets/images/reference/operators/filter/mirrorAxes_thumb.png
  variables:
  - label: Axis Sides (+/- 1)
    name: sides

---


Mirror space across one or more axes, similar to `reflect`.