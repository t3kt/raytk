---
layout: operator
title: raymarchRender3D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/raymarchRender3D
redirect_from:
  - /reference/opType/raytk.operators.output.raymarchRender3D/
op:
  name: raymarchRender3D
  summary: Renders a scene using 3D raymarching.
  opType: raytk.operators.output.raymarchRender3D
  category: output
  inputs:
    - name: definition_in
      label: SDF Scene
      required: true
      coordTypes: [vec3]
      contextTypes: [Context]
      returnTypes: [Sdf]
      summary: |
        SDF definition the shapes in the scene.
    - name: camera_definition_in
      label: Camera
      required: false
      coordTypes: [vec2]
      contextTypes: [CameraContext]
      returnTypes: [Ray]
      summary: |
        Camera used for render frame.
    - name: light_definition_in
      label: Light
      required: false
      coordTypes: [vec3]
      contextTypes: [LightContext]
      returnTypes: [Light]
      summary: |
        Light definition that can be used by supporting materials.
    - name: rayModifier_definition_in
      label: Ray Modifier
      required: false
      coordTypes: [vec3]
      contextTypes: [RayContext]
      returnTypes: [Ray]
      summary: |
        Advanced feature, not ready for use.
  parameters:
    - name: Res
      label: Resolution
      summary: |
        Rendering resolution
    - name: Antialias
      label: Anti Alias
      summary: |
        Number of antialiasing steps. Increasing this improves render quality but can be costly.
    - name: Camera
      label: Camera
      summary: |
        Standard TD Camera COMP, used if the `Camera` input isn't connected. This camera is not yet fully functional.
    - name: Light1
      label: Light
      summary: |
        Standard TD Light COMP, used if the `Light` input isn't connected. Only point lights work, and they don't yet support distance attenuation (though the `pointLight` ROP does).
    - name: Userenderdepth
      label: Use Render Depth
      summary: |
        Whether to use the provided Render TOP for a base depth. Not ready for use.
    - name: Overlayrender
      label: Overlay Render
      summary: |
        Whether to mix the provided Render TOP with the scene using depth. Not ready for use.
    - name: Rendertop
      label: Render TOP
      summary: |
        Connect a Render TOP to mix with the scene based on depth. Not ready for use.
    - name: Inspect
      label: Inspect
    - name: Maxsteps
      label: Max Steps
      summary: |
        Maximum number of marching steps.
    - name: Surfdist
      label: Surface Distance
      summary: |
        Minimum surface distance. Smaller values increase accuracy at the cost of performance.
    - name: Maxdist
      label: Max Distance
      summary: |
        Maximum distance. Rays that don't hit anything will stop at this distance. If this is too high, rays that don't hit anything will continue for a long time, causing a performance drain.
    - name: Nearhitrange
      label: Near Hit Range
      summary: |
        Advanced feature, not ready for use.
    - name: Timerefop
      label: Time Reference Operator
      summary: |
        COMP to use to determine the time. Only relevant if using a time field.
    - name: Uselimitbox
      label: Use Limit Box
      summary: |
        Whether to limit the space of the scene to a box, for performance improvements.
    - name: Limitboxmin
      label: Limit Box Minimum
      summary: |
        Minimum bounds of the scene limit box.
    - name: Limitboxmax
      label: Limit Box Maximum
      summary: |
        Maximum bounds of the scene limit box.
    - name: Shaderbuilderconfig
      label: Shader Builder Config
      summary: |
        Advanced configuration for the shader.
    - name: Enabledepthoutput
      label: Enable Depth Output
      summary: |
        Enables the depth output buffer.
    - name: Enablesdfoutput
      label: Enable SDF Output
      summary: |
        Enables the SDF data output buffer.
    - name: Enableworldposoutput
      label: Enable World Pos Output
      summary: |
        Enables the world xyz position output buffer.
    - name: Enablenormaloutput
      label: Enable Normal Output
      summary: |
        Enables the surface normals output buffer.
    - name: Enableraydiroutput
      label: Enable Ray Direction Output
      summary: |
        Enables the ray direction output buffer.
    - name: Enablerayoriginoutput
      label: Enable Ray Origin Output
      summary: |
        Enables the ray origin (camera position) output buffer.
    - name: Enableorbitoutput
      label: Enable Orbit Trap Output
      summary: |
        Enables the fractal orbit trap output buffer (only supported for certain SDFs).
    - name: Enablenearhitoutput
      label: Enable Near Hit Output
      summary: |
        Advance feature, not ready for use.
    - name: Enablestepoutput
      label: Enable Step Output
      summary: |
        Advance feature, not ready for use.
    - name: Enableiterationoutput
      label: Enable Iteration Output
      summary: |
        Advance feature, not ready for use.
    - name: Enableobjectidoutput
      label: Enable Object Id Output
      summary: |
        Advance feature, not ready for use.
    - name: Enabledebugoutput
      label: Enable Debug Output
      summary: |
        Advance feature, not ready for use.
    - name: Help
      label: Help

---

# raymarchRender3D

Category: output



Renders a scene using 3D raymarching.