---
layout: operator
title: render2D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/render2D
redirect_from:
  - /reference/opType/raytk.operators.output.render2D/
op:
  category: output
  detail: 'The input field can return either vec4 which is used as RGBA, or a float,
    which is copied to all 4 channels.

    The input field can use either 2D coordinates, or 1D, in which case it only uses
    the X axis and renders the

    same result for each vertical line of pixels.'
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    label: SDF or Field
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
  name: render2D
  opType: raytk.operators.output.render2D
  parameters:
  - label: Resolution
    name: Res
  - label: Pixel Format
    menuOptions:
    - label: Use Input
      name: useinput
    - label: 8-bit fixed (RGBA)
      name: rgba8fixed
    - label: sRGB 8-bit fixed (RGBA)
      name: srgba8fixed
    - label: 16-bit float (RGBA)
      name: rgba16float
    - label: 32-bit float (RGBA)
      name: rgba32float
    - label: _separator_
      name: _separator_
    - label: 10-bit RGB, 2-bit Alpha, fixed (RGBA)
      name: rgb10a2fixed
    - label: 16-bit fixed (RGBA)
      name: rgba16fixed
    - label: 11-bit float (RGB), Positive Values Only
      name: rgba11float
    - label: 16-bit float (RGB)
      name: rgb16float
    - label: 32-bit float (RGB)
      name: rgb32float
    - label: 8-bit fixed (Mono)
      name: mono8fixed
    - label: 16-bit fixed (Mono)
      name: mono16fixed
    - label: 16-bit float (Mono)
      name: mono16float
    - label: 32-bit float (Mono)
      name: mono32float
    - label: 8-bit fixed (RG)
      name: rg8fixed
    - label: 16-bit fixed (RG)
      name: rg16fixed
    - label: 16-bit float (RG)
      name: rg16float
    - label: 32-bit float (RG)
      name: rg32float
    - label: 8-bit fixed (A)
      name: a8fixed
    - label: 16-bit fixed (A)
      name: a16fixed
    - label: 16-bit float (A)
      name: a16float
    - label: 32-bit float (A)
      name: a32float
    - label: 8-bit fixed (Mono+Alpha)
      name: monoalpha8fixed
    - label: 16-bit fixed (Mono+Alpha)
      name: monoalpha16fixed
    - label: 16-bit float (Mono+Alpha)
      name: monoalpha16float
    - label: 32-bit float (Mono+Alpha)
      name: monoalpha32float
    name: Format
  - label: Alignment
    menuOptions:
    - description: Places 0,0 in the center of the frame.
      label: Center
      name: center
    - description: Old default behavior. Note that when used, `Scaling` is ignored.
        When in doubt, don't use this.
      label: Legacy
      name: legacy
    - description: Places 0,0 at the bottom left of the frame.
      label: Bottom Left
      name: bottomleft
    name: Alignment
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: How coordinates are positioned within the render frame.
  - label: Scaling
    menuOptions:
    - description: Stretches coordinates so both axes are -0.5 on one side and 0.5
        on the other.
      label: Fill
      name: fill
    - description: Uses the smaller of the two dimensions of the frame resolution
        to put -0.5..0.5 on that axis, and whatever the equivalent is on the other
        axis so that the scaling remains uniform.
      label: Fit Inside
      name: fitinside
    - description: Equivalent to `Fit Inside` but uses the larger of the two dimensions.
      label: Fit Outside
      name: fitoutside
    name: Scaling
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: How coordinates are scaled within the render frame.
  - label: UV Map
    name: Uvmap
    summary: UV Map that is used to pick the uV coordinates used for each pixel. If
      this is provided, the `Alignment` and `Scaling` not used.
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - label: Zoom
    name: Zoom
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Offset
    name: Offset
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Customize Shader Config
    name: Customizeshaderconfig
  - label: Enable UV Output
    name: Enableuvoutput
  - label: Enable Normal Output
    name: Enablenormaloutput
  - label: Enable Debug Output
    name: Enabledebugoutput
  - label: Enable Custom Output 1
    name: Enablecustomoutput1
  - label: Enable Custom Output 2
    name: Enablecustomoutput2
  shortcuts:
  - r2
  summary: Renders a 2D image by evaluating the input field for each pixel.
  thumb: assets/images/reference/operators/output/render2D_material_thumb.png

---


Renders a 2D image by evaluating the input field for each pixel.

The input field can return either vec4 which is used as RGBA, or a float, which is copied to all 4 channels.
The input field can use either 2D coordinates, or 1D, in which case it only uses the X axis and renders the
same result for each vertical line of pixels.