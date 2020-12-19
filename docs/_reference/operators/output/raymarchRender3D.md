---
layout: page
title: raymarchRender3D
parent: Output Operators
grand_parent: Operators
permalink: /reference/operators/output/raymarchRender3D
redirect_from:
  - /reference/opType/raytk.operators.output.raymarchRender3D/
---

# raymarchRender3D

Category: output



Renders a scene using 3D raymarching.

## Parameters

* `Res` *Resolution*: Rendering resolution
* `Antialias` *Anti Alias*: Number of antialiasing steps. Increasing this improves render quality but can be costly.
* `Camera` *Camera*: Standard TD Camera COMP, used if the `Camera` input isn't connected. This camera is not yet fully functional.
* `Light1` *Light*: Standard TD Light COMP, used if the `Light` input isn't connected. Only point lights work, and they don't yet support distance attenuation (though the `pointLight` ROP does).
* `Userenderdepth` *Use Render Depth*: Whether to use the provided Render TOP for a base depth. Not ready for use.
* `Overlayrender` *Overlay Render*: Whether to mix the provided Render TOP with the scene using depth. Not ready for use.
* `Rendertop` *Render TOP*: Connect a Render TOP to mix with the scene based on depth. Not ready for use.
* `Inspect` *Inspect*
* `Maxsteps` *Max Steps*: Maximum number of marching steps.
* `Surfdist` *Surface Distance*: Minimum surface distance. Smaller values increase accuracy at the cost of performance.
* `Maxdist` *Max Distance*: Maximum distance. Rays that don't hit anything will stop at this distance. If this is too high, rays that don't hit anything will continue for a long time, causing a performance drain.
* `Nearhitrange` *Near Hit Range*: Advanced feature, not ready for use.
* `Timerefop` *Time Reference Operator*: COMP to use to determine the time. Only relevant if using a time field.
* `Uselimitbox` *Use Limit Box*: Whether to limit the space of the scene to a box, for performance improvements.
* `Limitboxmin` *Limit Box Minimum*: Minimum bounds of the scene limit box.
* `Limitboxmax` *Limit Box Maximum*: Maximum bounds of the scene limit box.
* `Shaderbuilderconfig` *Shader Builder Config*: Advanced configuration for the shader.
* `Enabledepthoutput` *Enable Depth Output*: Enables the depth output buffer.
* `Enablesdfoutput` *Enable SDF Output*: Enables the SDF data output buffer.
* `Enableworldposoutput` *Enable World Pos Output*: Enables the world xyz position output buffer.
* `Enablenormaloutput` *Enable Normal Output*: Enables the surface normals output buffer.
* `Enableraydiroutput` *Enable Ray Direction Output*: Enables the ray direction output buffer.
* `Enablerayoriginoutput` *Enable Ray Origin Output*: Enables the ray origin (camera position) output buffer.
* `Enableorbitoutput` *Enable Orbit Trap Output*: Enables the fractal orbit trap output buffer (only supported for certain SDFs).
* `Enablenearhitoutput` *Enable Near Hit Output*: Advance feature, not ready for use.
* `Enablestepoutput` *Enable Step Output*: Advance feature, not ready for use.
* `Enableiterationoutput` *Enable Iteration Output*: Advance feature, not ready for use.
* `Enableobjectidoutput` *Enable Object Id Output*: Advance feature, not ready for use.
* `Enabledebugoutput` *Enable Debug Output*: Advance feature, not ready for use.
* `Help` *Help*

## Inputs

* `definition_in` *SDF Scene*: SDF definition the shapes in the scene.
* `camera_definition_in` *Camera*: Camera used for render frame.
* `light_definition_in` *Light*: Light definition that can be used by supporting materials.
* `rayModifier_definition_in` *Ray Modifier*: Advanced feature, not ready for use.