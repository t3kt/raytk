> When is a point not a point?

So far when we've been working with fields and coordinates, the coordinates that we've been using have been the same kind of spatial coordinates that are used by the `raymarchRender3D` or `render2D`.

That generally makes sense, but there are times when it can be useful to interpret the meaning of "coordinates" in other ways.

# Coordinates for `mobiusRingSdf`

For example, let's say you have a `mobiusRingSdf` and you want to use a field to vary the thickness at different points around the ring with a sine wave pattern. You could use a `waveField`, but it only has options for using the X, Y, or Z axis, or distance from the origin. Those options can't wrap the wave in a ring matching the SDF.

Fortunately, `mobiusRingSdf` provides some alternative ways to use coordinates in the fields that it takes in. When you connect a field that expects 1D coordinates, the `mobiusRingSdf` will ask the field for a value based on how far around the ring the point is.

In other words, when the renderer asks `mobiusRingSdf` about the nearest surface to point `0.5, 0.5, 0.0`, the `mobiusRingSdf` will need to choose a thickness setting. To do that, it will figure out how far around the ring that point is (`0.125` in this case, since it's at 45˚ around the ring). Then it will ask the `waveField` for a value at `0.125`, and use the result to choose the thickness, then use that to figure out how far the surface is (`sin(0.125 * TWOPI)`, and provide that answer to the renderer.

Here, the meaning of "coordinates" is different in certain parts of the network. Instead of trying to convert an XYZ position to an angle and then use that for a wave, it's presenting the `waveField` with an alternate concept of "coordinates" that matches what we want it to do.

If you've noticed the Coordinate Type on various operators like `waveField` and wondered why it has a 1D option, this is why.

For `mobiusRingSdf`, the angle is useful so that's what it uses for 1D fields. But other operators that use fields will support different types of coordinates in ways that are useful for that operator. 

![https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9e2fefd-ffed-4619-99dd-6008ef9fa704/Untitled.png](https://s3-us-west-2.amazonaws.com/secure.notion-static.com/d9e2fefd-ffed-4619-99dd-6008ef9fa704/Untitled.png)

# Coordinates for `mirrorOctant`

The `mirrorOctant` operator has a field input to control the rotation. It supports 3 different types of coordinates for that field:

- 1D - Distance from the center point
- 2D - The position along the mirror plane. (So for a mirror on the XZ plane, this would be X and Z)
- 3D - The regular 3D position.
