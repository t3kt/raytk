---
layout: page
title: Addons
nav_order: 12.5
---

# RayTK Addons

RayTK addons are additional components that extend the toolkit's functionality. They are not included in the core toolkit, but are available as separate downloads available from Tekt's [Patreon](https://patreon.com/tekt).

Versions of addons line up with versions of the main toolkit, and are only compatible with that same version of RayTK.

Like the main toolkit, each addon is a tox file that can be added to a project. They require the main toolkit to also be loaded in order to use tools like the palette to create operators from the addon.

**Important Note**: Read the licensing and rules section at the bottom of this page!

# RayTKVolumes

RayTKVolumes is a collection of components that make it easier to work with volumes in RayTK.

Volumes are sort of part way between an SDF and a field. They have a density value at each point in space as well as some SDF properties like a color attribute. They can be created from SDFs, fields, or even 3D textures.

Many operators in the main toolkit support volumes, especially transformations.

There are a few areas:

1. Converting RayTK content (SDFs, fields, volumes, etc.) into 3D textures, which can be used with [Josef Pelz's T3D](https://patreon.com/josefpelz).
2. Creating and modifying volumes
3. Rendering them use a specialized version of the RayTK renderer that supports things like clouds that are fields of density rather than hard surfaces.

A typical scene could do something like this:

1. Use RayTK SDF operators to create some scene content, combining and transforming the SDFs.
2. That gets converted to a 3D texture using the `texture3dRender` operator.
3. Use T3D to process that texture, doing things that RayTK can't, like feedback.
4. Either using T3D's surface operator to render it.
5. Or bringing it back into RayTK with a `texture3dVolume` and render it as a cloud using `volumetricRaymarchRender3D`.

# RayTKAbstractions

The RayTKAbstractions addon is a collection of components that take common patterns and workflows in RayTK and package them up into more user-friendly operators, or add enhanced functionality to existing operators.

# Licensing and Rules

RayTK addons are available through [Patreon](https://patreon.com/tekt) subscriptions. An active subscription is required to download the latest versions of the addons. But like the main toolkit, once you create operators from the addon, they can be used in any project without needing to have the addon package loaded.

**Important Note**: The licensing and policies around the addons will likely be changing, including rules about what you are or are not allowed to share with other people or post publicly.

The policy *as of this release* is:

1. You **can** share files that contain operators created from the addon.
2. You **CANNOT** share files that contain the entire addon package.

If users break that rule, even if it's unintentional, there may need to be more restrictions on accessing and using the addons. But it's better for everyone if we avoid having to do that.

What this means is that you **CANNOT** do this:

1. Open a TD project
2. Load the toolkit and the addon into the project
3. Create some content using addon operators
4. Save the project
5. Share that project file (`.toe`) with someone else

Doing that would include the entire addon package in the project file, which is not allowed.

Instead, you should do this:

1. Open a TD project
2. Load the toolkit and the addon into the project
3. Create some content using addon operators
4. Save the project
5. Put the content in a COMP, which **does not** have the addon package inside it
6. Save that COMP as a `.tox` file
7. Share the **tox file** with someone else
