---
layout: page
title: Getting Started With RayTK
---

## Download the Library

The first step to using RayTK is to download the latest tox file, from the [repository](https://github.com/t3kt/raytk/releases).

Note that there are many of files in the repository itself, but these are only needed for development purposes. If you only want to *use* the library rather than *modify* it, use the release tox file.

## Load the Library

Drag the tox file into the project. It's generally good to add it to the *root* network (`/` rather than `/project1`), but it's not strictly necessary.

## Creating a Network

To create your first ROP, use the keyboard shortcut `alt + r` to open up the editor tools popup. It will show a list of available ROPs, organized into categories. You can search by typing a name. This popup is like the main TouchDesigner "OP Create Dialog" (using `tab`), but it shows the available ROPs rather than the standard TouchDesigner OPs.

![Create OP Menu](/assets/img/guide/intro-createOpMenu.png)

1. Choose a `boxFrameSdf`, and a new COMP will be created in the network editor.
1. Create a `raymarchRender3d` and connect the output of your `boxFrameSdf` to the input of the `raymarchRender3d`.
1. Create a `lookAtCamera` and connect it to the second input ("camera_definition_in") on the `raymarchRender3d`.
1. Connect a `Null TOP` to the first output of `raymarchRender3d`.
1. Play around with the parameters of the `boxFrameSdf`.

You've just created your first RayTK network!

![Basic RayTK Network](/assets/img/guide/intro-basicNetwork.png)

The `boxFrameSdf` is an `SDF` (signed distance function) operator, which is how you define geometry. It's equivalent to `SOP`s like `Sphere`, `Box`, etc.

## Add to Your Network

Now that you have a complete render setup, you can start to add to and change your scene.

1. Add a `rotate` between the `boxFrameSdf` and the `raymarchRender3d`.
2. Adjust the "Rotate XYZ" parameters and watch the box rotate in the output.

![Basic RayTK Network](/assets/img/guide/intro-basicNetwork2.png)

You've just created your first "filter" ROP! It modifies the behavior of another ROP.

3. Add a `basicMat` between the `rotate` and the `raymarchRender3d`.
4. Try out different color settings.

![Basic RayTK Network](/assets/img/guide/intro-basicNetwork3.png)

You've just created your first "material" ROP. It assigns a material to a ROP, which is used to determine what colors it should use.
