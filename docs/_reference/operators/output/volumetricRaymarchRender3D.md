---
layout: operator
title: volumetricRaymarchRender3D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/volumetricRaymarchRender3D
redirect_from:
  - /reference/opType/raytkVolumes.operators.output.volumetricRaymarchRender3D/
op:
  category: output
  detail: 'Note that this renderer is actively being developed, so it may have some
    bugs or limitations.


    This renderer uses steps that have a constant size, rather than stepping different
    distances based on how far an SDF says they are from the surface. This makes it
    more suitable for volumes that are based on fields of density rather than SDFs.


    There are two main modes: Solid and Cloud.


    Solid mode behaves similarly to regular raymarching, where the rays stop once
    they hit an area with a density of 1 or more. Then it uses shading similar to
    a regular `raymarchRender3D`. This mode works best with volumes that are based
    on SDFs.


    Cloud mode sends rays through the volume, and at each step, it checks the density
    of the volume. Rays don''t stop marching until they go through the bounding area.
    The density and color accumulate as the rays go through the volume to produce
    the final results.'
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: Volume
    name: volume
    required: true
    returnTypes:
    - Volume
    summary: Volume that the rays will march through. This must be a Volume and not
      an SDF.
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera
    name: camera
    returnTypes:
    - Ray
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light
    returnTypes:
    - Light
  moduleName: raytkVolumes
  name: volumetricRaymarchRender3D
  opType: raytkVolumes.operators.output.volumetricRaymarchRender3D
  parameters:
  - label: March Mode
    menuOptions:
    - label: Solid Surface
      name: solid
    - label: Cloud
      name: cloud
    name: Marchmode
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Raymarching approach to use.
  - label: Step Size
    name: Stepsize
    readOnlyHandling: baked
    regularHandling: runtime
    summary: The size of each marching step. Smaller steps will produce more accurate
      results but will be slower.
  - label: Area Mode
    menuOptions:
    - description: Uses a box defined by `Areacenter` and `Areasize`.
      label: Bounding Box
      name: box
    - description: Uses a range of distances defined by `Distrange`, so that each
        ray has the same length, regardless of the direction.
      label: Distance Range
      name: range
    name: Areamode
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: How to define the area that the rays will march through.
  - label: Area Center
    name: Areacenter
    summary: Center of the scene bounding box.
  - label: Area Size
    name: Areasize
    summary: Size of the scene bounding box.
  - label: Dist Range
    name: Distrange
    summary: Minimum and maximum distances where the rays start and end.
  - label: Max Distance
    name: Maxdist
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Maximum distance. Rays that don't hit anything will stop at this distance.
      This is applied on top of the bounding area, so it can generally be fairly high.
  - label: Resolution
    name: Res
    summary: Rendering resolution
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
  - label: Enable Debug Output
    name: Enabledebugoutput
  - label: Enable Custom Output 1
    name: Enablecustomoutput1
  - label: Enable Custom Output 2
    name: Enablecustomoutput2
  - label: Enable Depth Output
    name: Enabledepthoutput
    summary: Enables the depth output buffer.
  - label: Enable World Pos Output
    name: Enableworldposoutput
    summary: Enables the world xyz position output buffer.
  - label: Enable Ray Origin Output
    name: Enablerayoriginoutput
    summary: Enables the ray origin (camera position) output buffer.
  - label: Enable Ray Direction Output
    name: Enableraydiroutput
    summary: Enables the ray direction output buffer.
  - label: Ray Marching
    name: Headerraymarching
  - label: Max Steps
    name: Maxsteps
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Maximum number of marching steps. If this is too low, the rays may stop
      before they finish going through the scene area.
  - label: Refinement Steps
    name: Refinementsteps
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Number of steps to take to refine the final position of the ray. This
      can help reduce artifacts for solid mode.
  - label: Enable Normal Smoothing
    name: Enablenormalsmoothing
    readOnlyHandling: baked
    regularHandling: baked
    summary: Enable normal smoothing. This will average the normals of nearby points
      to produce a smoother result.
  - label: Normal Smoothing
    name: Normalsmoothing
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Distance to use for normal smoothing.
  - label: Time Reference Operator
    name: Timerefop
  - label: Shader Builder Config
    name: Shaderbuilderconfig
  - label: Customize Shader Config
    name: Customizeshaderconfig
  status: beta
  summary: Renderer that uses raymarching with volumes instead of SDFs.

---


Renderer that uses raymarching with volumes instead of SDFs.

Note that this renderer is actively being developed, so it may have some bugs or limitations.

This renderer uses steps that have a constant size, rather than stepping different distances based on how far an SDF says they are from the surface. This makes it more suitable for volumes that are based on fields of density rather than SDFs.

There are two main modes: Solid and Cloud.

Solid mode behaves similarly to regular raymarching, where the rays stop once they hit an area with a density of 1 or more. Then it uses shading similar to a regular `raymarchRender3D`. This mode works best with volumes that are based on SDFs.

Cloud mode sends rays through the volume, and at each step, it checks the density of the volume. Rays don't stop marching until they go through the bounding area. The density and color accumulate as the rays go through the volume to produce the final results.