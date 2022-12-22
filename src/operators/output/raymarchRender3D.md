Renders a scene using 3D raymarching.

## Parameters

* `Res`: Rendering resolution
* `Antialias`: Number of antialiasing steps. Increasing this improves render quality but can be costly.
* `Userenderdepth`: Whether to use the provided Render TOP for a base depth.
* `Overlayrender`: Whether to mix the provided Render TOP with the scene using depth.
* `Rendertop`: Connect a Render TOP to mix with the scene based on depth.
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
* `Enablenearhitoutput`: Enables near hit output which shows where rays got close to hitting surfaces.
* `Enablestepoutput`: Enables step count output which shows how many steps each ray took while marching through the scene.
* `Enableiterationoutput`: Advance feature, not ready for use.
* `Enableobjectidoutput`: Enables object id output which shows id values assigned using `injectObjectId`.
* `Enabledebugoutput`: Advance feature, not ready for use.
* `Format`
  * `useinput`
  * `rgba8fixed`
  * `srgba8fixed`
  * `rgba16float`
  * `rgba32float`
  * `_separator_`
  * `rgb10a2fixed`
  * `rgba16fixed`
  * `rgba11float`
  * `rgb16float`
  * `rgb32float`
  * `mono8fixed`
  * `mono16fixed`
  * `mono16float`
  * `mono32float`
  * `rg8fixed`
  * `rg16fixed`
  * `rg16float`
  * `rg32float`
  * `a8fixed`
  * `a16fixed`
  * `a16float`
  * `a32float`
  * `monoalpha8fixed`
  * `monoalpha16fixed`
  * `monoalpha16float`
  * `monoalpha32float`
* `Enablereflection`
* `Reflectionpasses`
* `Enableshadow`
* `Enablenearhitmindist`
* `Nearhitmindist`
* `Nearhitfade`
* `Enablecoloroutput`

## Inputs

* `definition_in`:  SDF definition the shapes in the scene.
* `camera_definition_in`:  Camera used for render frame.
* `light_definition_in`:  Light definition that can be used by supporting materials.
* `shadow_definition_in`: 