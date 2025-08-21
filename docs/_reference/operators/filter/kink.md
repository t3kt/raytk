---
layout: operator
title: kink
parent: Filter Operators
grand_parent: Operators
permalink: /reference/operators/filter/kink
redirect_from:
  - /reference/opType/raytk.operators.filter.kink/
op:
  category: filter
  detail: 'The bending that this operator applies is slightly different than the `bend`
    operator, and is asymmetrical, causing a tighter bend on one side based on the
    bend amount and direction.


    Based on [Bending an SDF](https://www.shadertoy.com/view/3llfRl) by blackle.'
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
    - amountField
    - offsetField
    - spreadField
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
    - float
    - vec2
    - vec3
    - vec4
    label: Amount Field
    name: amountField
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
    - PopContext
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: Offset Field
    name: offsetField
    returnTypes:
    - float
    supportedVariableInputs:
    - amountField
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
    - float
    - vec2
    - vec3
    - vec4
    label: Spread Field
    name: spreadField
    returnTypes:
    - float
    supportedVariableInputs:
    - amountField
    - offsetField
  name: kink
  opType: raytk.operators.filter.kink
  parameters:
  - label: Enable
    name: Enable
  - label: Direction
    menuOptions:
    - description: Bends along the X axis, in the Y direction
      label: Along X Toward Y
      name: xy
    - description: Bends along the X axis, in the Z direction
      label: Along X Toward Z
      name: xz
    - description: Bends along the Y axis, in the X direction
      label: Along Y Toward X
      name: yx
    - description: Bends along the Y axis, in the Z direction
      label: Along Y Toward Z
      name: yz
    - description: Bends along the Z axis, in the X direction
      label: Along Z Toward X
      name: zx
    - description: Bends along the Z axis, in the Y direction
      label: Along Z Toward Y
      name: zy
    name: Direction
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which axis to bend around on which plane.
  - label: Side
    menuOptions:
    - label: Negative
      name: neg
    - label: Positive
      name: pos
    name: Side
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Which side to bend towards.
  - label: Amount
    name: Amount
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Amount of bending.
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
    summary: 'Position along the '
  - label: Spread
    name: Spread
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Range over which the bending is spread. Higher values mean a more gradual
      bend.
  summary: Bends space, similar to the `bend`.
  thumb: assets/images/reference/operators/filter/kink_thumb.png

---


Bends space, similar to the `bend`.

The bending that this operator applies is slightly different than the `bend` operator, and is asymmetrical, causing a tighter bend on one side based on the bend amount and direction.

Based on [Bending an SDF](https://www.shadertoy.com/view/3llfRl) by blackle.