---
layout: page
title: Output Buffers
nav_order: 7
---

# Output Buffers

Output buffers are TOP streams that come out of an OutputOP. They allow a single OutputOP to produce multiple types of data for each pixel. See [TouchDesigner documentation](https://docs.derivative.ca/Write_a_GLSL_TOP#Outputting_to_Multiple_Color_Buffers) for details.

Different types of renderers provide different types of output buffers. Each type of renderer has a "main" output, such as color for [raymarchRender3d]. Output ops have parameters that can enable and disable various outputs.

## Accessing Output Buffers

There are several ways to access output buffers.

First, OutputOPs have outputs for some of the buffers that they produce. [raymarchRender3d], for example, has outputs for color, normals, depth, and so on.

However not all of the possible buffers are available as outputs from the ROP itself. To access those, you can use [renderSelect]. It has a parameter that takes in a reference to an OutputOP, and a menu parameter that lets you choose from one of the possible types of outputs.

:warning: If the selected buffer produces empty output, either that buffer needs to be enabled on the OutputOP, or that type of buffer isn't offered by that OutputOP at all.

Last, certain types of buffers have specialized components that access output buffer data and provide additional associated functionality. For example, [depthMap] accesses the "depth" buffer, and has options for scaling and adjusting the resulting depth map. Similarly, [worldPosMap] accesses the "world position" buffer, and has options for adjusting the resulting position map.

## The Inspector

The [Inspector] is a great tool for exploring output buffers. It shows a list of all the available buffers for the selected ROP and shows the contents of the buffers along with tools for examining the values in them.

## Tutorial

<iframe width="560" height="315" src="https://www.youtube.com/embed/hLRIZ0yz9DI" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>


[raymarchRender3d]: /raytk/reference/operators/output/raymarchRender3d
[renderSelect]: /raytk/reference/operators/output/renderSelect
[depthMap]: /raytk/reference/operators/post/depthMap
[worldPosMap]: /raytk/reference/operators/post/worldPosMap
[Inspector]: /raytk/guide/inspector