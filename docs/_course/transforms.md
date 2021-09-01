> Shift not the shape, but the space in which the shape lives

~ Ancient raymarching proverb.

# Transform concepts

Filters take in a ROP and alter its behavior. The most common type of filters are transform-based filters.

When taking in a ROP that answers some question about point `p`, they change that position before giving it to their input and asking it that same question.

# Standard transform operators

## Translate

The `translate` operator applys an offset to points in space.

- For example:
    - Let's say there's a `sphereSdf` centered at `1.0, 0.0, 0.0` and radius `0.2`, connected to a `translate` that offsets X by `+0.3`.
    - Without the `translate`, if the `raymarchRender3D` asks the `sphereSdf` how far it is from `0.0, 0.0, 0.0`, the `sphereSdf` would say the distance is `0.8`., (`= 1.0 - 0.0 - 0.2`).
    - But when the `raymarchRender3D` asks the `translate` how far the shape is from point `0.0, 0.0, 0.0`, the `translate` asks the `sphereSdf` how far away the shape is from `-0.3, 0.0, 0.0`, and provides that result to `raymarchRender3D`.
    - That may seem like it's going in the wrong direction, but it isn't moving **the sphere**, it's moving **the point**. So by moving the point by `-0.3` in X, when the `sphereSdf` is asked how far it is from `-0.3, 0.0, 0.0`, it will say the distance is `1.1` instead of `0.8`.
    - So moving the point by `-0.3` is equivalent to moving the sphere by `+0.3`.
- You can think of this as a conversation between the OPs:
    - Renderer: "Hey translate, how far is the closest surface to point `p`?
    - Translate: "Hey box, how far is the closest surface to point `p - (0.3, 0, 0)`?"
    - Box: "It's a cube and it's `1.1` units from that point you were asking about!"
    - Translate: "Hey renderer, I checked and the nearest thing is a cube that's `1.1` units from `p`"
    - Renderer: "Thanks!"

### Rotate

`rotate` is similar to `translate` in that it changes the position that gets used by its input. But instead of offsettting the position, it rotates it around a pivot point (usually the origin `0,0,0`).

### Scale

`scale` changes the position by scaling it, as one might expect.

- It does the scaling around the origin (`0,0,0`). If you need to scale around a different pivot point, the `transform` operator has options for that.
- Why non-uniform scale is problematic.
    - But since scaling changes the *size* of the input shape, it needs to adjust the SDF result to counteract that.
    - For uniform scaling on all axes, that can be done cleanly without any distortion.
    - But for non-uniform scaling, the amount of adjustment could be different depending on where the point is relative to the shape. So it doesn't even attempt to adjust the distance.
    - That can be ok in some cases, but often it will produce distortion.

### Transform

`transform` is a combination of `translate`, `rotate`, and `scale` in a single ROP.

- It provides options for choosing which types of transformations to apply and in what order. It's equivalent to the `transform SOP`, and the parameters are designed to be mostly the same as they are in the `SOP` version.

# Other types of transforms

### Twist

`twist` twists space around an axis.

- It's basically like `rotate`, but the amount of rotation that it applies is different depending on how far a point is along that axis.

### Iterated Transform

- So far these have all been familiar types of things that you can do with SOPs. But there are some things that you can do with raymarching that are much much harder with SOPs.
- `iteratedTransform` is similar to `transform` in that it provides options for translation, rotation, and scaling.
- But instead of just applying those operations once, it applies them multiple times, and can use reflection (covered in more detail later) in between each step.
