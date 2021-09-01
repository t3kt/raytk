# SDF concepts

- Geometry is defined by SDF operators.
- SDF stands for "signed distance function".
- SDF ROPs answer the question: How far away is the surface of the shape from point `p`?
    - That's the "distance" part of the name.
    - The "signed" part refers to how they will produce answers that are positive when **outside** a shape, and negative when **inside** it.

- The simplest example of this is a sphere.
    - You can define a sphere as a position and a radius.
    - To check how far away `p` is from the sphere, you take the distance between that point and the center of the sphere, and subtract the radius.
    - When the distance between `p` and the center of the sphere is smaller than the radius of the sphere, subtracting it will produce a negative value, meaning that `p` is **inside** the sphere.
    - When that distance is larger than the radius, it will produce a positive value, meaning that `p` is **outside** the sphere.
- That's where the "signed" part of SDF comes in. The sign is the + or - that indicates outside vs inside.
- Other shapes use different logic to answer that same question.

# SDF operators

- In RayTK, these are defined using OPs in the "Sdf" category like `sphereSdf` and `boxSdf`.
- We've already discussed how `sphereSdf` works. The `boxSdf` operator is similar, but it uses a different calculation for the distance. Instead of producing a sphere, it produces a cube.
- SDFs can also be more complicated than simple geometric primitives. The `boxFrameSdf` for example is similar to `boxSdf` but instead of producing a solid cube, it produces a hollow frame of the edges of a cube.
- The `linkSdf` produces a "chain link" shape, sort of like an stretched torus with straight sides.
- There are a whole bunch of other SDFs. Try some out and see what they produce!
- Some SDFs are simple and some (like `kaliGeneratorSdf` are rather complex).
