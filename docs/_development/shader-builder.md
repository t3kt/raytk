---
layout: page
title: Shader Builder
nav_order: 8
---

# Shader Builder

The `shaderBuilder` component is included in every output / renderer operator.

It is responsible for producing all the things that the render ROP needs to execute the shader in a GLSL TOP.

* Collect information about all the ROPs in a scene.
* Generate the complete shader.
* Collect the parameters, texture sources, specialization constants, etc. that the shader relies on.

## Shader Config

TODO

## Definition Processing

Definition processing is applied to the incoming table of ROP definitions.

* Gather fields from each ROP's full definition table and add them to the inline columns.
* Resolve coord / context / return types. See (Type Handling)[/raytk/development/type-handling/].
* Reverse rows so that every ROP's dependencies come after it in the table.
* Apply name simplification (depend on the render config).

## Runtime Parameters

The runtime parameters from all ROPs are collected, then arranged into 4-part tuples.

For parameters that are already tuples, they're just used as they are (with spacers if needed to fill them to 4 parts).

For parameters that are single values, they're combined into tuples when possible.

The resulting CHOP is then passed to the GLSL TOP as a uniform array of vec4.

## Constant Parameters

The parameters configured as specialization constants from all ROPs are collected into a single CHOP.

Then each one is added to the GLSL TOP as a separate specialization constant.

## Parameter Aliases

For each parameter, a macro is generated that refers to its position in the params array and the relevant vector field (XYZW).

For each tuplet, a macro is generated that refers to either the vector in the params array, with a type wrapper to reduce it to the relevant number of parts (e.g. vec2).

## Macros

TODO

## Buffers

TODO

## Textures

Textures from the `RopState`s of all ROPs are collected into a table, so they can be connected as inputs to the GLSL TOP.

## Output Buffers

Each enabled output buffer on the ROP is identified and a declaration for it is injected into the shader. The number of each buffer is passed to the parent renderer, so it can enable that many outputs for the GLSL TOP.

## Variables and References

TODO

## Library Includes

There is a set of commonly used shared libraries that ROPs can indicate that they use. For each of these that is used by at least one ROP in the scene, either an `#include` directive is injected into the code referring to its DAT, or the contents of that DAT is directly injected into the shader (depending on the shader configuration). 

For less commonly used libraries, ROPs may include a copy within themselves and include its path so the `shaderBuilder` can include it. These are deduplicated based on their text content to avoid declaration conflicts and redundant code.

## Code Processing

The generated shader is organized into a number of sections. Depending on the contents of the scene, some of these sections might not be present (e.g. if no textures are used).

* Global declarations provided by the renderer. These can provide items accessible from other ROPs.
* OP data type aliases/macros. For each ROP, macros are added that refer to the coord / context / return types (for use in declarations), as well as macros indicating which types are used (for preprocessor usage).
* Macros from OPs and/or the renderer
* Library includes (or the full contents of libraries depening on shader config)
* Predeclarations provided by the renderer
* Parameter alias macros
* Texture declarations / alias macros
* Buffer declarations
* Material ID declarations
* Output buffer declarations
* Variable declarations
* Output buffer initialization function: zero out output buffers in case they are left unassigned.
* Global declarations from each ROP
* Initialization function with init block from each ROP
* ROP Functions
* Renderer body code

## Validation

TODO