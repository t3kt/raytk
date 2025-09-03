---
layout: operator
title: cylinderSdf
parent: Sdf Operators
grand_parent: Operators
permalink: /reference/operators/sdf/cylinderSdf
redirect_from:
  - /reference/opType/raytk.operators.sdf.cylinderSdf/
op:
  category: sdf
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
    summary: Optional field used to control the radius of the cylinder. If it uses
      1D coordinates, it is given the position along the axis. For 3D coordinates,
      it is given the raw position.
    supportedVariables:
    - axispos
    - normangle
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
    label: Radius Field
    name: radiusField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    supportedVariables:
    - axispos
    - normangle
    - normoffset
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
    label: Thickness Field
    name: thicknessField
    returnTypes:
    - float
    supportedVariableInputs:
    - heightField
    - radiusField
    supportedVariables:
    - axispos
    - normangle
    - normoffset
  keywords:
  - column
  - cylinder
  - pipe
  name: cylinderSdf
  opType: raytk.operators.sdf.cylinderSdf
  parameters:
  - label: Translate
    name: Translate
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Shifts the center of the cylinder.
  - label: Radius
    name: Radius
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The radius of the cylinder.
  - label: Height
    name: Height
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The height of the cylinder, along the selected axis.
  - label: Axis
    menuOptions:
    - label: X
      name: x
    - label: Y
      name: y
    - label: Z
      name: z
    name: Axis
    readOnlyHandling: semibaked
    regularHandling: runtime
  - label: Infinite Height
    name: Infiniteheight
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to extend infinitely along the chosen axis or have a limited
      height.
  - label: Hollow
    name: Hollow
    readOnlyHandling: semibaked
    regularHandling: runtime
    summary: Whether to make the cylinder a hollow tube instead of a solid cylinder.
  - label: Thickness
    name: Thickness
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Thickness of the walls of the tube when using hollow mode.
  summary: Cylinder, either solid or a hollow tube.
  thumb: assets/images/reference/operators/sdf/cylinderSdf_thumb.png
  variables:
  - label: Position Along Axis
    name: axispos
  - label: Normalized Axis Position (0..1)
    name: normoffset
  - label: Normalized Angle (0..1)
    name: normangle

---


Cylinder, either solid or a hollow tube.