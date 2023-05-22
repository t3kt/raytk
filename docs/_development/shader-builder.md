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

## Textures

Textures from the `RopState`s of all ROPs are collected into a table, so they can be connected as inputs to the GLSL TOP.

## Macros

TODO

## Buffers

TODO

## Output Buffers

TODO

## Variables and References

TODO

## Code Processing

TODO

## Validation

TODO