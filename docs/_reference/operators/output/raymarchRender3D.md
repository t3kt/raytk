---
layout: operator
title: raymarchRender3D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/raymarchRender3D
redirect_from:
  - /reference/opType/raytk.operators.output.raymarchRender3D/
op:
  category: output
  inputs:
  - contextTypes:
    - Context
    coordTypes:
    - vec3
    label: SDF Scene
    name: definition_in
    required: true
    returnTypes:
    - Sdf
    summary: SDF definition the shapes in the scene.
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera
    name: camera_definition_in
    returnTypes:
    - Ray
    summary: Camera used for render frame.
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light_definition_in
    returnTypes:
    - Light
    summary: Light definition that can be used by supporting materials.
  - contextTypes:
    - RayContext
    coordTypes:
    - vec3
    label: Ray Modifier
    name: rayModifier_definition_in
    returnTypes:
    - Ray
    summary: Advanced feature, not ready for use.
  name: raymarchRender3D
  opType: raytk.operators.output.raymarchRender3D
  parameters:
  - label: Resolution
    name: Res
    summary: Rendering resolution
  - label: Anti Alias
    name: Antialias
    summary: Number of antialiasing steps. Increasing this improves render quality
      but can be costly.
  - label: Camera
    name: Camera
    summary: Standard TD Camera COMP, used if the `Camera` input isn't connected.
      This camera is not yet fully functional.
  - label: Light
    name: Light1
    summary: Standard TD Light COMP, used if the `Light` input isn't connected. Only
      point lights work, and they don't yet support distance attenuation (though the
      `pointLight` ROP does).
  - label: Use Render Depth
    name: Userenderdepth
    summary: Whether to use the provided Render TOP for a base depth. Not ready for
      use.
  - label: Overlay Render
    name: Overlayrender
    summary: Whether to mix the provided Render TOP with the scene using depth. Not
      ready for use.
  - label: Render TOP
    name: Rendertop
    summary: Connect a Render TOP to mix with the scene based on depth. Not ready
      for use.
  - label: Max Steps
    name: Maxsteps
    summary: Maximum number of marching steps.
  - label: Surface Distance
    name: Surfdist
    summary: Minimum surface distance. Smaller values increase accuracy at the cost
      of performance.
  - label: Max Distance
    name: Maxdist
    summary: Maximum distance. Rays that don't hit anything will stop at this distance.
      If this is too high, rays that don't hit anything will continue for a long time,
      causing a performance drain.
  - label: Near Hit Range
    name: Nearhitrange
    summary: Advanced feature, not ready for use.
  - label: Time Reference Operator
    name: Timerefop
    summary: COMP to use to determine the time. Only relevant if using a time field.
  - label: Use Limit Box
    name: Uselimitbox
    summary: Whether to limit the space of the scene to a box, for performance improvements.
  - label: Limit Box Minimum
    name: Limitboxmin
    summary: Minimum bounds of the scene limit box.
  - label: Limit Box Maximum
    name: Limitboxmax
    summary: Maximum bounds of the scene limit box.
  - label: Shader Builder Config
    name: Shaderbuilderconfig
    summary: Advanced configuration for the shader.
  - label: Enable Depth Output
    name: Enabledepthoutput
    summary: Enables the depth output buffer.
  - label: Enable SDF Output
    name: Enablesdfoutput
    summary: Enables the SDF data output buffer.
  - label: Enable World Pos Output
    name: Enableworldposoutput
    summary: Enables the world xyz position output buffer.
  - label: Enable Normal Output
    name: Enablenormaloutput
    summary: Enables the surface normals output buffer.
  - label: Enable Ray Direction Output
    name: Enableraydiroutput
    summary: Enables the ray direction output buffer.
  - label: Enable Ray Origin Output
    name: Enablerayoriginoutput
    summary: Enables the ray origin (camera position) output buffer.
  - label: Enable Orbit Trap Output
    name: Enableorbitoutput
    summary: Enables the fractal orbit trap output buffer (only supported for certain
      SDFs).
  - label: Enable Near Hit Output
    name: Enablenearhitoutput
    summary: Advance feature, not ready for use.
  - label: Enable Step Output
    name: Enablestepoutput
    summary: Advance feature, not ready for use.
  - label: Enable Iteration Output
    name: Enableiterationoutput
    summary: Advance feature, not ready for use.
  - label: Enable Object Id Output
    name: Enableobjectidoutput
    summary: Advance feature, not ready for use.
  - label: Enable Debug Output
    name: Enabledebugoutput
    summary: Advance feature, not ready for use.
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
  - label: Enable Reflection
    name: Enablereflection
  - label: Reflection Passes
    name: Reflectionpasses
  summary: Renders a scene using 3D raymarching.

---

# raymarchRender3D

Category: output



Renders a scene using 3D raymarching.