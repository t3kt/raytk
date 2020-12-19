Renders a scene using 3D raymarching.



## Parameters

* `Res`: Rendering resolution
* `Antialias`: Number of antialiasing steps. Increasing this improves render quality but can be costly.
* `Camera`: Standard TD Camera COMP, used if the `Camera` input isn't connected. This camera is not yet fully functional.
* `Light1`: Standard TD Light COMP, used if the `Light` input isn't connected. Only point lights work, and they don't yet support distance attenuation (though the `pointLight` ROP does).
* `Userenderdepth`: Whether to use the provided Render TOP for a base depth. Not ready for use.
* `Overlayrender`: Whether to mix the provided Render TOP with the scene using depth. Not ready for use.
* `Rendertop`: Connect a Render TOP to mix with the scene based on depth. Not ready for use.
* `Inspect`
* `Maxsteps`: Maximum number of marching steps.
* `Surfdist`: Minimum surface distance. Smaller values increase accuracy at the cost of performance.
* `Maxdist`: Maximum distance. Rays that don't hit anything will stop at this distance. If this is too high, rays that don't hit anything will continue for a long time, causing a performance drain.
* `Nearhitrange`: Advanced feature, not ready for use.
* `Timerefop`: COMP to use to determine the time. Only relevant if using a time field.
* `Uselimitbox`: Whether to limit the space of the scene to a box, for performance improvements.
* `Limitboxmin`: Minimum bounds of the scene limit box.
* `Limitboxmax`: Maximum bounds of the scene limit box.
* `Shaderbuilderconfig`: Advanced configuration for the shader.
* `Enabledepthoutput`: Enables the depth output buffer.
* `Enablesdfoutput`: Enables the SDF data output buffer.
* `Enableworldposoutput`: Enables the world xyz position output buffer.
* `Enablenormaloutput`: Enables the surface normals output buffer.
* `Enableraydiroutput`: Enables the ray direction output buffer.
* `Enablerayoriginoutput`: Enables the ray origin (camera position) output buffer.
* `Enableorbitoutput`: Enables the fractal orbit trap output buffer (only supported for certain SDFs).
* `Enablenearhitoutput`: Advance feature, not ready for use.
* `Enablestepoutput`: Advance feature, not ready for use.
* `Enableiterationoutput`: Advance feature, not ready for use.
* `Enableobjectidoutput`: Advance feature, not ready for use.
* `Enabledebugoutput`: Advance feature, not ready for use.

## Inputs

* `definition_in` *SDF Scene*: SDF definition the shapes in the scene.
* `camera_definition_in` *Camera*: Camera used for render frame.
* `light_definition_in` *Light*: Light definition that can be used by supporting materials.
* `rayModifier_definition_in` *Ray Modifier*: Advanced feature, not ready for use.