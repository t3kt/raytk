---
layout: operator
title: pointMapRender
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/pointMapRender
redirect_from:
  - /reference/opType/raytk.operators.output.pointMapRender/
op:
  category: output
  detail: 'The primary use for this is with TOP-based instancing for a Geometry COMP:


    * Create a TOP with a coordinate value in each pixel. For example, this could
    be point cloud data, or converted points from a SOP/CHOP.

    * Create your RayTK scene network, with an SDF or value/vector field.

    * (Optionally) add a `sampledPointMat` to the scene to control how colors are
    applied to shapes.

    * Create a `pointMapRender`, and connect the scene to the first input and the
    coordinate TOP to the TOP input.

    * The TOP that comes out of the "Color" output will be a TOP with the same dimensions
    as the coordinate TOP, with a color value for each pixel, based on the scene.

    * On a Geometry COMP, with instancing on, use the coordinate TOP for the instance
    positions, and use the colors TOP from the `pointMapRender` for the instance colors.


    Other uses include:

    * LED pixel mapping, where you use the physical location of each LED for the coordinates,
    and apply the resulting colors to each LED.

    * GPU particles, where the simulation GLSL TOP produces coordinates from one buffer,
    which are run through the `pointMapRender`, and then feed the resulting values
    back into the simulation to control particle forces for each particle/pixel.


    The "SDF or Value" output, when using an SDF scene, will output values where the
    RGB channels contain the distance to the surface. The alpha channel will be one
    for points that existed in the input map and zero for ones that did not. In other
    words the alpha channel will be the same as the alpha channel in the input point
    map.'
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - float
    - vec2
    - vec3
    - vec4
    label: SDF or Field
    name: definition_in
    returnTypes:
    - float
    - vec4
    - Sdf
    supportedVariables:
    - datapos
    - datauv
    - datares
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera
    name: camera
    returnTypes:
    - Ray
    supportedVariables:
    - datapos
    - datauv
    - datares
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light
    returnTypes:
    - Light
    supportedVariables:
    - datapos
    - datauv
    - datares
  keywords:
  - point
  - render
  - volumetric
  name: pointMapRender
  opType: raytk.operators.output.pointMapRender
  parameters:
  - label: Pixel Format
    menuOptions:
    - label: Use Input
      name: useinput
    - label: 8-bit fixed (RGBA)
      name: rgba8fixed
    - label: 16-bit float (RGBA)
      name: rgba16float
    - label: 32-bit float (RGBA)
      name: rgba32float
    - label: 10-bit RGB, 2-bit Alpha, fixed (RGBA)
      name: rgb10a2fixed
    - label: 16-bit fixed (RGBA)
      name: rgba16fixed
    - label: 11-bit float (RGB), Positive Values Only
      name: rgba11float
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
  - label: Enable Normal Output
    name: Enablenormaloutput
    summary: Enable producing normal vectors. For each point, this will produce a
      vector pointing in the direction that the nearest surface point is facing. These
      values can be accessed using a `renderSelect` operator.
  - label: Enable Object Id Output
    name: Enableobjectidoutput
    summary: Enable object ID output, which produces a TOP with values assigned with
      the `injectObjectId` operator for whichever shape each point is inside.
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - label: Coord Type
    menuOptions:
    - label: Auto
      name: auto
    - label: 2D
      name: vec2
    - label: 3D
      name: vec3
    name: Coordtype
  - label: Output Type
    menuOptions:
    - label: 2D Texture
      name: texture2d
    - label: 2D Texture Array
      name: texture2darray
    - label: 3D Texture
      name: texture3d
    name: Outputtype
  - label: Enable Density Output
    name: Enabledensityoutput
  - label: Enable Debug Output
    name: Enabledebugoutput
  - label: Enable Custom Output 1
    name: Enablecustomoutput1
  - label: Enable Custom Output 2
    name: Enablecustomoutput2
  - label: Enable Normal Smoothing
    name: Enablenormalsmoothing
    readOnlyHandling: baked
    regularHandling: baked
    summary: Whether to smooth out surface normals by sampling at larger distances.
  - label: Normal Smoothing
    name: Normalsmoothing
    readOnlyHandling: baked
    regularHandling: runtime
    summary: How far apart to sample to calculate surface normals.
  - label: Material Mode
    menuOptions:
    - label: Only Inside SDF
      name: inside
    - label: Only SDF Surface
      name: surface
    - label: Fill Everwhere
      name: everywhere
    name: Materialmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Enable Blending
    name: Enableblending
  - label: Blending
    name: Blending
  - label: Thickness
    name: Thickness
  - label: Customize Shader Config
    name: Customizeshaderconfig
  - label: Compile Behavior
    menuOptions:
    - label: Stall Until Done
      name: stalluntildone
    - label: Threaded, Show Checkerboard Until Done
      name: threadedcheckerboard
    - label: Threaded, Show Black Until Done
      name: threadedblack
    - label: Threaded, Show Previous Shader Until Done
      name: threadedprevious
    name: Compilebehavior
  shortcuts:
  - pmr
  summary: Renderer that takes in a TOP of coordinates and evaluates the scene at
    each point.
  thumb: assets/images/reference/operators/output/pointMapRender_thumb.png
  variables:
  - label: Data Coord (Pixels)
    name: datapos
  - label: Data Coord (0..1)
    name: datauv
  - label: Data Resolution (Pixels)
    name: datares

---


Renderer that takes in a TOP of coordinates and evaluates the scene at each point.

The primary use for this is with TOP-based instancing for a Geometry COMP:

* Create a TOP with a coordinate value in each pixel. For example, this could be point cloud data, or converted points from a SOP/CHOP.
* Create your RayTK scene network, with an SDF or value/vector field.
* (Optionally) add a `sampledPointMat` to the scene to control how colors are applied to shapes.
* Create a `pointMapRender`, and connect the scene to the first input and the coordinate TOP to the TOP input.
* The TOP that comes out of the "Color" output will be a TOP with the same dimensions as the coordinate TOP, with a color value for each pixel, based on the scene.
* On a Geometry COMP, with instancing on, use the coordinate TOP for the instance positions, and use the colors TOP from the `pointMapRender` for the instance colors.

Other uses include:
* LED pixel mapping, where you use the physical location of each LED for the coordinates, and apply the resulting colors to each LED.
* GPU particles, where the simulation GLSL TOP produces coordinates from one buffer, which are run through the `pointMapRender`, and then feed the resulting values back into the simulation to control particle forces for each particle/pixel.

The "SDF or Value" output, when using an SDF scene, will output values where the RGB channels contain the distance to the surface. The alpha channel will be one for points that existed in the input map and zero for ones that did not. In other words the alpha channel will be the same as the alpha channel in the input point map.