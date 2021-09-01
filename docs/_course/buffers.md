> Dig deeper! There's even more data in there!

# Output buffer concepts

- So far, the images that we've seen coming out of the `raymarchRender3D` have just been the regular colorized rendering.
- But there are other types of outputs that you can pull out of the renderer.
- Each type of output supported by a renderer is called an "output buffer".
- Different types of renderers provide different kinds of output buffers.
- All of the buffers discussed in this section can be produced by the `raymarchRender3D`, though there are other ones supported by other types of renderers which we'll discuss later.
- Many output buffers aren't enabled by default. The "Outputs" parameter page of `raymarchRender3D` contains toggles for the various types that it supports.

# Depth

- The "Depth" output buffer contains the distance from the camera of whatever is shown in each pixel, either a point on a surface, or nothing if the ray didn't hit anything before it gave up.
- It's equivalent to what comes out of the `Depth TOP` for a regular `Render TOP`.
- The alpha channel will be 1 for surface hits, and 0 when the ray didn't hit anything.
- Like the `Depth TOP`, the values that come out of it are often outside the 0...1 range that you normally work with in TOPs. So you may need to rescale the values using a `Math TOP`.
- There are a few ways to access the depth output buffer.
    - The simplest option is to use the second outlet on the `raymarchRender3D`.
    - There's also the `outputSelect` component has a menu that you can use to select either depth or various other types of outputs. It's equivalent to the `Render Select TOP` (in fact it contains one of those).
    - Or if you want special depth-specific functionality like rescaling, you can use the toolkit's `depthMap` component, which behaves like the `Depth TOP` in that you point it at a renderer and it pulls out the depth data.

# Normals

- In the "Normal" output buffer, for any pixel that represents a hit on a surface, it gives you the surface normal for that point on the surface (the direction which the surface is facing at that point).
- The values coming out of it are normalized vectors, meaning that each R, G, and B (a.k.a. X, Y, and Z) can be anywhere between -1 and 1, and the vector as a whole will have a length of 1. The alpha channel will be 1 for pixels that hit a surface, and 0 for those that do not.
- Unlike depth, the `raymarchRender3D` doesn't produce the normals buffer by default. So you need to make sure to switch that on in the `raymarchRender3D`'s "Outputs" parameters.

# Step count

- The "Step Count" output buffer gives you the number of times the ray stopped to check the scene as it marched along.
- Because of how the marching works, this ends up being a larger number for rays that come close to hitting a surface before they either hit something else, or don't hit anything.
- The result is that the step count provides a sort of "glow" around shapes in the scene.
- However it's important to note that since this is a count of steps, it's always in whole numbers. You can't take 1.5 steps. This means that the contents of the buffer will contain hard transitions from one value to another. It looks similar to a "posterize" effect, or using the "Step" settings in a `Level TOP`.

# Near hit

- The "Near Hit" buffer is similar to step count, but it smoothes out those hard transitions.
- It represents how much the ray was close to things as it moved along.
- In the `raymarchRender3D`, there are settings that control how close a ray has to come to hitting a surface for it to be considered "near". It also lets you specify a fade range, so that rays that come closer to a surface count more than rays that are further away but still within the maximum allowed range.
- It also takes into account the amount of distance traveled, to make sure that a ray spending a lot of its "time" near a shape in a single step vs only stopping by it "briefly".
- Even with these features, you can still sometimes end up with some amount of hard edges particularly over large open areas. But you have more control over that behavior than with step count.
