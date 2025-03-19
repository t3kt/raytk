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
    returnTypes:
    - float
    - vec4
    - Sdf
    summary: SDF definition the shapes in the scene.
    supportedVariableInputs:
    - camera
  - contextTypes:
    - CameraContext
    coordTypes:
    - vec2
    label: Camera
    name: camera
    returnTypes:
    - Ray
    summary: Camera used for render frame.
  - contextTypes:
    - LightContext
    coordTypes:
    - vec3
    label: Light
    name: light
    returnTypes:
    - Light
    summary: Light definition that can be used by supporting materials.
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: shadow
    name: shadow
    returnTypes:
    - float
    sourceParamLabel: Shadow
    sourceParamName: Shadow
  - contextTypes:
    - RayContext
    coordTypes:
    - vec3
    label: Background Field
    name: backgroundField
    returnTypes:
    - float
    - vec4
    sourceParamLabel: Background Field
    sourceParamName: Backgroundfield
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Secondary Ray Cast
    name: secondaryRayCast
    returnTypes:
    - float
    - vec4
    sourceParamLabel: Secondary Ray Cast
    sourceParamName: Secondaryraycast
  - contextTypes:
    - MaterialContext
    coordTypes:
    - vec3
    label: Refraction Ray Cast
    name: refractionRayCast
    returnTypes:
    - float
    - vec4
    sourceParamLabel: Refraction Ray Cast
    sourceParamName: Refractionraycast
  name: raymarchRender3D
  opType: raytk.operators.output.raymarchRender3D
  parameters:
  - label: Resolution
    name: Res
    summary: Rendering resolution
  - label: Anti Alias
    name: Antialias
    readOnlyHandling: baked
    regularHandling: baked
    summary: Number of antialiasing steps. Increasing this improves render quality
      but can be costly.
  - label: Use Render Depth
    name: Userenderdepth
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Whether to use the provided Render TOP for a base depth.
  - label: Overlay Render
    name: Overlayrender
    summary: Whether to mix the provided Render TOP with the scene using depth.
  - label: Render TOP
    name: Rendertop
    summary: Connect a Render TOP to mix with the scene based on depth.
  - label: Max Steps
    name: Maxsteps
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Maximum number of marching steps.
  - label: Surface Distance
    name: Surfdist
    readOnlyHandling: semibaked
    regularHandling: semibaked
    summary: Minimum surface distance. Smaller values increase accuracy at the cost
      of performance.
  - label: Max Distance
    name: Maxdist
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Maximum distance. Rays that don't hit anything will stop at this distance.
      If this is too high, rays that don't hit anything will continue for a long time,
      causing a performance drain.
  - label: Near Hit Range
    name: Nearhitrange
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Advanced feature, not ready for use.
  - label: Time Reference Operator
    name: Timerefop
    summary: COMP to use to determine the time. Only relevant if using a time field.
  - label: Use Limit Box
    name: Uselimitbox
    summary: Whether to limit the space of the scene to a box, for performance improvements.
  - label: Limit Box Minimum
    name: Limitboxmin
    readOnlyHandling: baked
    regularHandling: runtime
    summary: Minimum bounds of the scene limit box.
  - label: Limit Box Maximum
    name: Limitboxmax
    readOnlyHandling: baked
    regularHandling: runtime
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
    summary: Enables near hit output which shows where rays got close to hitting surfaces.
  - label: Enable Step Output
    name: Enablestepoutput
    summary: Enables step count output which shows how many steps each ray took while
      marching through the scene.
  - label: Enable Iteration Output
    name: Enableiterationoutput
    summary: Advance feature, not ready for use.
  - label: Enable Object Id Output
    name: Enableobjectidoutput
    summary: Enables object id output which shows id values assigned using `injectObjectId`.
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
    readOnlyHandling: baked
    regularHandling: baked
  - label: Reflection Passes
    name: Reflectionpasses
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Enable Shadow
    name: Enableshadow
    readOnlyHandling: baked
    regularHandling: baked
  - label: Enable Near Hit Minimum Dist
    name: Enablenearhitmindist
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Near Hit Minimum Distance
    name: Nearhitmindist
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Near Hit Fade
    name: Nearhitfade
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Enable Color Output
    name: Enablecoloroutput
  - label: Format
    name: Headerformat
  - label: Compositing
    name: Headercompositing
  - label: Reflection
    name: Headerreflection
  - label: Refraction
    name: Headerrefraction
  - label: Enable Refraction
    name: Enablerefraction
    readOnlyHandling: baked
    regularHandling: baked
  - label: Refraction Passes
    name: Refractionpasses
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Refraction Ray Cast
    name: Refractionraycast
  - label: Background
    name: Headerbackground
  - label: Background Field
    name: Backgroundfield
  - label: Use Background Field Alpha
    name: Usebackgroundfieldalpha
    readOnlyHandling: semibaked
    regularHandling: semibaked
  - label: Show Background
    name: Showbackground
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Shadow
    name: Headershadow
  - label: Shadow
    name: Shadow
  - label: Ray Marching
    name: Headerraymarching
  - label: Distance Correction Factor
    name: Distfactor
    readOnlyHandling: baked
    regularHandling: runtime
  - label: Limits
    name: Headerlimits
  - label: Near Hit
    name: Headernearhit
  - label: Normals
    name: Headernormals
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
  - label: Volumetrics
    name: Headervolumetrics
  - label: Enable Secondary Ray Cast
    name: Enablesecondaryraycast
  - label: Secondary Ray Cast
    name: Secondaryraycast
  - label: Customize Shader Config
    name: Customizeshaderconfig
  - label: Enable UV Output
    name: Enableuvoutput
  - label: Enable Custom Output 1
    name: Enablecustomoutput1
  - label: Enable Custom Output 2
    name: Enablecustomoutput2
  - label: Enable Dithering
    name: Enabledithering
    readOnlyHandling: baked
    regularHandling: runtime
  shortcuts:
  - rr3
  summary: Renders a scene using 3D raymarching.

---


Renders a scene using 3D raymarching.