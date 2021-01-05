---
layout: operator
title: flipFn
parent: Function Operators
grand_parent: Operators
permalink: /reference/operators/function/flipFn
redirect_from:
  - /reference/opType/raytk.operators.function.flipFn/
op:
  name: flipFn
  summary: Function that flips its input in one of several different modes.
  opType: raytk.operators.function.flipFn
  category: function
  inputs:
    - name: definition_in
      label: definition_in
      required: false
      coordTypes: [float,vec2,vec3]
      contextTypes: [none,Context,MaterialContext,CameraContext,LightContext,RayContext]
      returnTypes: [float,vec4]
  parameters:
    - name: Enable
      label: Enable
    - name: Fliptype
      label: Flip Type
      summary: |
        The type of flipping to apply.
      menuOptions:
        - name: flipdomain
          label: Flip Domain
          description: |
            Negates the coordinate passed to the input function, flipping the x axis of a function graph across the y axis.
        - name: fliprange
          label: Flip Range
          description: |
            Negates the input function's return value, flipping the y axis of a function graph across the x axis.
        - name: mirrorposdomain
          label: Mirror Positive Domain
          description: |
            Mirrors the coordinate so only the positive half is used, reflecting the positive side of a function graph across the y axis replacing the negative side.
        - name: flipnegdomain
          label: Flip Negative Domain
          description: |
            Mirrors the coordinate so only the positive half is used, but also flips the return value when on the negative side, reflecting the positive side of a function graph across the y axis but then also flipping that side upside down.
    - name: Returntype
      label: Return Type
      menuOptions:
        - name: useinput
          label: Use Input
        - name: Sdf
          label: SDF Result
        - name: float
          label: Float
        - name: vec4
          label: Vector4
        - name: Ray
          label: Ray
        - name: Light
          label: Light
    - name: Contexttype
      label: Context Type
      menuOptions:
        - name: none
          label: None
        - name: Context
          label: Context
        - name: MaterialContext
          label: Material Context
        - name: CameraContext
          label: Camera Context
        - name: LightContext
          label: Light Context
    - name: Inspect
      label: Inspect
    - name: Help
      label: Help

---

# flipFn

Category: function



Function that flips its input in one of several different modes.