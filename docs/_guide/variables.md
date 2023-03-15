---
layout: page
title: Variables
nav_order: 7.1
---

# Variables

Variables are a way for operators to provide additional information to other operators in the scene.

For example, the [`modulo1D`](/raytk/reference/operators/filter/modulo1D) operator repeats slices of space along an axis. It offers a variable indicating which slice is being rendered, so that its input can vary settings per-slice.

Another example is the [`assignColor`](/raytk/reference/operators/filter/assignColor) operator, which adds a color setting to an SDF result. It offers a variable to access the SDF result produced by its first input, so that the "Color Field" input can base the color on something like the SDF's UV coordinates.

Variables can be created in one of two ways:

1. Selecting the operator providing the variable, and using the [editor tools](/raytk/guide/tools/) menu (`alt+shift+r`), with the "Reference Variable" sub-menu.
2. Clicking one of the buttons on the providing operator's "Variables" parameter page.

Doing this will create a [`variableReference`](/raytk/reference/operators/utility/variableReference) operator, which access the value of the selected variable from the selected operator. This operator produces whatever type of value that variable uses, either in its entirety or just a single field within that value. For example, a vector variable can be accessed to produce either the whole vector, or just the Y part of the vector, depending on the settings on the `variableReference`.

## Tutorial Video

<iframe width="560" height="315" src="https://www.youtube.com/embed/eqqOlSEk0YA" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
