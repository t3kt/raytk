> Basically a raygun for reverse light.

# Camera concepts

In keeping with the theme of "ROPs answer questions about space", the Camera operators answer this question:

- For a given pixel in the rendering, where does the ray start, and what direction is it pointing towards?

# Standard cameras

- The `lookAtCamera` is similar to a `camera COMP` when using the "Look At" feature. You set the position of the camera, and a position that it is looking at, and then you can adjust the rotation if needed.
    - It's important to keep in mind that it is always using the "Look At" feature. So if you move the camera sideways, it won't just move sideways, it also rotate so it's still facing the target position.
    - It makes it easy to keep focus on an object or location while moving the camera around it.
- The `linkedCamera` copies the position, rotation, and other properties of a regular `camera COMP` (in other words it uses the same view matrix).
    - It works with regular `camera COMP`s and also with the special `camera` component from the TD palette (with built-in mouse and keyboard interaction, and even support for Spacemouse navigation!).
    - It's useful when you want to combine a RayTK scene with a regular rendering, since you can ensure that both are rendered from the same viewpoint and field of view.
    - It's also useful if you just want the simplicity of working with a standard `camera COMP`.
- The `orthoCamera` uses a orthogonal (non-perspective) view, similar to the "Front" / "Top" / etc options in SOP viewers or in modeling programs.

# Special cameras

- The `fisheyeCamera` is a special camera that uses several different types of "lens" behaviors to capture 180° or 360° views.
- The `splitCamera` uses two or more other cameras and divides up the rendering into areas with a different camera assigned to each.
    - It supports layouts like horizontal or vertical slices, or a 2x2 grid.
    - It also supports a `TOP` input that you can use to create other types of layouts.
