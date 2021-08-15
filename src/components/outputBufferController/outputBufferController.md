# outputBufferController

Manages the output buffers that are produced by a renderer.

The renderer defines a table of available output buffers, along
with settings and indicators of which are currently enabled.
This component uses that to generate tables used by the renderer
and the shaderBuilder within it.
