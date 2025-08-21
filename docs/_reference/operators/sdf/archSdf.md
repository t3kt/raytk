---
layout: operator
title: archSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/archSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.archSdf/
op:
  category: sdf
  detail: 'This SDF combines a few parts, which can be toggled on/off.


    The panel is the flat inner surface that fills the center of the arch.

    The frame is the outer border of the arch.'
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
    - vec3
    label: Height Field
    name: heightField
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
    - vec3
    label: Width Field
    name: widthField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
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
    - vec3
    label: Rounding Field
    name: roundingField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - widthField
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
    - vec3
    label: Frame Thickness Field
    name: frameThicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - widthField
    - roundingField
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
    - vec3
    label: Frame Depth Field
    name: frameDepthField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - widthField
    - roundingField
    - frameThicknessField
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
    - vec3
    label: Panel Depth Field
    name: panelDepthField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - widthField
    - roundingField
    - frameThicknessField
    - frameDepthField
  name: archSdf
  opType: raytk.operators.sdf.archSdf
  parameters:
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Width
    name: Width
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Rounding
    name: Rounding
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Size of the curves on the top corners. Smaller values produce more of
      a rectangle and larger values produce a curved peak.
  - label: Enable Panel
    name: Enablepanel
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to show the flat shape filling the center of the arch.
  - label: Panel Depth
    name: Paneldepth
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the center part.
  - label: Enable Frame
    name: Enableframe
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to show the outer part of the arch.
  - label: Frame Thickness
    name: Framethickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the frame (width/height).
  - label: Frame Depth
    name: Framedepth
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Depth of the frame.
  - label: Hide Frame Bottom
    name: Hideframebottom
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Whether to include a bottom section to the frame or leave it empty.
  summary: Arch / doorway.
  thumb: assets/images/reference/operators/sdf/archSdf_thumb.png

---


Arch / doorway.

This SDF combines a few parts, which can be toggled on/off.

The panel is the flat inner surface that fills the center of the arch.
The frame is the outer border of the arch.