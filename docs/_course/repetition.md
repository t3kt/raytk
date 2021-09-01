> Literally infinite cubes. So many cubes.

# Spatial repetition and remapping concepts

So far the filters we've discussed have been modifying positions in a fairly uniform manner. For each point in the original space, there's one equivalent point in the transformed space, though it may be in a different location.

But not all filters follow that rule. In some, a single point in the original space may appear in multiple positions in the transformed space.

# Mirroring with the `reflect` operator

The `reflect` operator picks a plane in space, and takes everything on one side of it, and flips it over to the other side.

The conversation between the ROPs goes like this:

- For a ray moving through the right side:
    - Renderer: "Hey modulo1D, what's near this spot on the right?"
    - modulo1D: "Hey boxSdf, what's near that spot on the right?"
    - boxSdf: "A cube!"
    - modulo1D: "Hey renderer, I looked into it and it turns out there's a cube!"
    - Renderer: "Thanks!"
- For a ray moving through the left side:
    - Renderer: "Hey modulo1D, what's near this spot on the left?"
    - modulo1D: "Pretty sure you mean on the right.... Hey, boxSdf, what's near this spot on the right?"
    - boxSdf: "A cube!"
    - modulo1D: "Hey renderer, seems like you actually meant on the right, so.... there's a cube there."
    - Renderer: "Thanks!"

- So if the reflection plane is along the X axis at `0`, is asked about a point that's on the right side of that plane, like `1, 2, 0.5`, it will just turn around and ask its input about that same point.
- But if it's asked about a point that's on the left side, like `-1.5, 0, 4`, it will flip the X, and ask its input about `1.5, 0, 4` instead.

TODO: Insert repetition-reflect diagram.

# Repeating with the `modulo1D`

The `modulo1D` takes a slice of space along an axis, and tiles that same range of coordinates infinitely along the axis.

- Essentially the conversation between the ROPs would be like:
    - For a ray moving straight through the original slice of space:
        - Renderer: "Hey what's near this spot here?"
        - modulo1D: "Hey boxSdf, what's near this spot here?"
        - boxSdf: "A cube!"
        - modulo1D: "Hey renderer, I check and it turns out there's a cube!"
        - Renderer: "Thanks!"
    - For another ray somewhere else:
        - Renderer: "Hey what's near that spot over there?"
        - modulo1D: "I think you actually mean this spot over here, where there's a cube."
        - Renderer: "Oh neat, there's a cube over there."
        - modulo1D: "Yeah I guess you could interpret it that way"
        - Renderer: "Thanks!"
- If you fit a shape entirely inside the range where the slice is taken from, that shape will be repeated infinitely in a row.
- If the shape stretches over the boundary of the slice, that outside part gets cut off. That can sometimes cause some rendering errors though.
- There are two ways to deal with that:
    - Make sure the input shape never goes outside the range.
    - Use the mirroring setting, which flips every other tile, so if anything crosses the edge of the slice, that same shape will be mirrored on the other side, perfectly lined up with it.
- It's important to note that even though this has the effect of making infinite copies of a shape, it has almost no performance impact. It isn't actually making "copies". It just shifts where rays pass through so they all hit the same shape.

TODO: Insert repetition-modulo1d and repetition-modulo1d-mirror diagrams

# Repeating in a grid with a `modulo2d` or `modulo3d`

The `modulo2D` is like `modulo1D`, but it repeats in a grid along two axes.

There's even `modulo3D`, which repeats on all three axes!

- But when using `modulo3D`, keep in mind that it is tiling in all directions, so it can be easy to end up with the camera stuck inside a shape if you aren't careful about the positioning.
- That can also happen with `modulo1D` and `modulo2D`, but at least with those, you can move the camera along another axis to keep it away from all the shapes.

TODO: insert repetition-modulo2d diagram

# Kaleidoscopic repetition

### moduloPolar

The `moduloPolar` operator is similar, but instead of repeating things along linear axes, it repeats them in radial slices around an axis.

- It's kind of like a kaleidoscope, but in 3D space.
- It has the same kinds of behavior as the other "modulo" operators, with a mirroring option, and potential for shapes getting cut off.

### mirrorOctant

The `mirrorOctant` operator is kind of like `moduloPolar` or `reflect`, but it reflects across two axes, and across their diagonals.

# Spatial repetition vs duplication

- The filters discussed so far all have the benefit of being relatively cheap in terms of performance, since they all still only ask their input the question once, they just alter the coordinates that they include in that question. But there are limitations to that approach.
- In the `reflect` operator, if you have a shape that's partially across the reflection plane, you only get two mirrored "copies" of one of the sections, coming from one side of the plane. If you want to have two copies that each include the whole shape though, you can use the `flip` operator with the "Merge" setting.
    - When asked what the closest surface is at point `p`, it will ask its input that question, and then flip `p` and ask the input again with that new position, and then combine the two results.
    - That lets you control how those two copies are combined, and it lets you use the entirety of both copies, but it's important to note that it *doubles* the cost of *everything* that's upstream from it, since it has to ask the input two different variations of the question with different coordinates.
    - Flip's conversations go like:
        - Renderer: "Hey flip, what's near this spot over there on the right"
        - flip: "Hey boxSdf, what's near this spot over there on the right?"
        - boxSdf: "A cube!"
        - flip: "Hey boxSdf, another question: what's near that spot over there on the left?"
        - boxSdf: "Also a cube!"
        - flip: "Renderer, so I checked it out and it's actually these two cubes that I mushed together"
- The `radialClone` operator is like the `moduloPolar` equivalent of `flip`. It will create multiple copies of the input, around an axis, and then combine them.
    - Like `flip` though, it has to ask its input the question once for each separate copy of the shape. That means that if it's using 5 copies of the input, it's using 5 times as much processing!
    - Sometimes that's worth it, but it can be costly!
