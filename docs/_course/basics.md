# What is RayTK?

- The toolkit is a self-contained TOX that can be dropped into any project, though having multiple copies of it in a project can cause issues.
- The toolkit contains a collection of types of OPs, and some tools for creating and working with them.
- Once those OPs are created though, they can function without the toolkit TOX. But you do need the toolkit TOX if you want editor tools like the Palette and Inspector.
- In general you shouldn't need to do anything inside the toolkit or the OPs that you create with it. But if you're interested you're welcome to take a look.

# Where to get the toolkit

- The toolkit TOX is available in the [Releases page of the GitHub repository](https://github.com/t3kt/raytk/releases).
- The files in the main repository are for development purposes only, and should not be used in projects.

# Core toolkit concepts

There are 3 types of OPs that you can create with the toolkit.

- ROPs
    - ROPs are the basic building blocks of the toolkit.
    - They define various types of elements of a scene.
    - The term "scene" refers to a network of one or more ROPs connected to each other.
- Output OPs
    - An Output OP is a special type of ROP that takes in one or more ROPs, and uses them to build a shader. It then runs that shader in a `GLSL TOP` and produces one or more `TOP` outputs.
    - They are kind of like the `Render TOP`, which takes in a few different kinds of operators (geometry, lights, camera) and uses them to render an image.
- Supplemental components
    - There are a handful of other components that you can use with a scene, mostly for post-processing.

# Palette

- The Palette is equivalent to the TouchDesigner "Create OP" dialog.
- It is used to create new ROPs and related components.
- Open the palette using **ALT+r**.
- OPs are grouped into categories like Filters, Materials, Lights, etc.
- The filter bar in the palette searches the list of OPs.
    - You can either search for pieces of text in names, or for initials of names like "rr3" for `raymarchRender3D`.
    - You can also search for keywords. For example, searching for "ring" will show `torusSdf`.
- The status filter toggle buttons show and hide:
    - Beta OPs: new ones that might still have some bugs, and are likely to change in newer versions of the toolkit.
    - Deprecated OPs: old ones that have been replaced by better alternatives or weren't useful.
