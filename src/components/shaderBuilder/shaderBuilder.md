# shaderBuilder

Builds a shader for a renderer based on a scene definition.

Each renderer contains an instance of this component.
It takes in the scene definition table, extracts information from the operators
in the scene, and generates shader text along with some tables that the renderer
uses to configure the `GLSL Multi TOP` which executes the shader.

The builder produces:
* Variable declarations
* Uniform variable declarations
* Uniform texture declarations
* CHOP-based buffer sampler declarations
* Preprocessor macros
* Combined code blocks from all operators
* Switch blocks for things like material lookups
* Initialization code blocks

The builder also aggregates validation results from all operators in the scene.