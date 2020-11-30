---
layout: page
title: Output Buffers
nav_order: 5
---

# Output Buffers

Output buffers are TOP streams that come out of an OutputOP. They allow a single OutputOP to produce multiple types of data for each pixel. See [TouchDesigner documentation](https://docs.derivative.ca/Write_a_GLSL_TOP#Outputting_to_Multiple_Color_Buffers) for details.

Different types of renderers provide different types of output buffers. Each type of renderer has a "main" output, such as color for [raymarchRender3d]. Output ops have parameters that can enable and disable various outputs.  


[raymarchRender3d]: /raytk/reference/operators/output/raymarchRender3d