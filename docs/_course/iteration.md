> Kind of like instancing!

# Iteration concepts

Earlier we discussed filters that use spatial reflect, repetition, and other techniques to create the effect of having multiple "copies" of a shape.

Some operators will actually run their input multiple times and combine the results, like `radialClone` and `flip` (when using the blend mode).

Others did things like tiling space, causing a shape to appear in multiple positions, without having to run their input multiple times, like `modulo1D`, `moduloPolar`, and `reflect`.

Some of those operators, like `modulo1d` and `moduloPolar`, provide some basic options to mirror every other "copy". But they are still effectively just placing the same shape in various positions and sometimes flipping them.

The repetition operators like `modulo1D` are kind of like instancing with a `Geometry COMP`. If you have a cube inside a `Geometry COMP` that's using instancing, you can place the instances in different positions, and you can rotate and scale them differently. But you can't (without clever trickery or geometry shaders) have some of those instances be spheres and some be cubes.

Fortunately, RayTK provides you with a way to do just that!

It's called "iteration".

Note that there's also `iteratedTransform` which isn't actually related to this. It's just an unfortunate collision of two uses of the same word.

# How iteration flows through the network

When `modulo1D` is asked the question for some point `p`, it'll adjust that point so it repeats before it forwards the question on to whatever is connected to its input. By switching on the "Iteration" setting, when it asks its input for a result, it'll include some information about which "cell" in space the original point was in.

Without iteration, if it's repeating with a spacing of size 1, and it gets asked about point `3.2, 0, 0`, it'll still ask its input:

What's the result at `0.2, 0, 0`?

With iteration, it'll include a hint like:

What's the result at `0.2, 0, 0`? (by the way, this is for cell 2)

*It's 2 instead of 3 since the cells are numbered starting at 0 rather than 1.*

That extra hint at the end will get passed to the input's inputs, and their inputs, and so on.

<< diagram: iteration-1-flow >>

The only time that hint gets replaceed is if something further up the stream wants to add its own hint instead, but just for **its** inputs.

<< diagram: iteration-2-overriding >>

Iteration is similar the "stamping" mechanism in the `Copy SOP`, where you use expressions in the `Copy SOP` to set "variables" that can be different for each copy. SOPs that are upstream from the Copy SOP can access those using `me.fetchStamp('copyNum', 0)`, and use that to change their settings.

# Sources of iteration values

This hint is known as the "iteration value".

The iteration value is a `vec4` (a 4-part vector). Not all operators fill all 4 parts though. Since `modulo1D` only has one axis of repetition, it'll just fill in the first part and set the others to zero.

The `modulo2D` operator has a few options for types of iteration values to provide, most of which fill both X and Y.

The `reflect` operator also supports iteration, though it just produces 0 for one side and 1 for the other.

The operators that ask their input for results multiple times and combine them can also provide iteration values. For example, the `radialClone` and `flip` operators have options to provide the index of the current request each time they ask their input.

The `instance` operator is specifically designed to be used with iteration. In fact, that's really the only way you can use it at all. It's similar to `radialClone`, where it will ask its input multiple times and combine the results. But instead of arranging those requests around an axis, it just always asks with the same coordinates. The only difference between each time it asks its input is the iteration value.

# Using iteration values

Once you have an operator that's providing an iteration value to its inputs, there are a few operators that can use those values.

The `iterationField` makes them available as a float or vector field. When asked for a value for any point in space, it will just respond with the current iteration value.

You can use that to control anything that has a field input, like `rotate`. Remember though that `rotate` is expecting angles in degrees, so the small numbers that you'll often get from `iterationField` need to be scaled up using `rescaleField`.

The `iterationSwitch` can be used to alternate between different input sources based on the current iteration value.

Remember earlier when we mentioned being able to swap in a different shape for each "instance"? This is how you do that!

The `rangeTransform` is designed to work with `instance`, but it can be used with anything that provides iteration values. It has ranges of translate and rotate settings, and it picks settings within those ranges based on the iteration.

If you have an `instance` with 3 copies, and a `rangeTransform` with a translate range of `0,0,0` to `6,0,0`, it will translate the first copy by `0,0,0`, the second by `3,0,0`, and the third by `6,0,0`. You can use it to arrange instances in a line, or you can use the rotation settings to reproduce the same behavior as `radialClone`.
