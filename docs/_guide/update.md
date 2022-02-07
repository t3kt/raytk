---
layout: page
title: Updating Scenes
nav_order: 9
---

# Updating Toolkit Versions

When a new version of RayTK is available, if you want to use it with older scenes, there's a tool that lets you update the operators in-place.

For very early versions (before 0.11), this feature is not available.

You can have older RayTK operators in a project alongside newer ones, but they can't be connected ops from different versions.

1. Save a backup of the project.
1. Remove the old toolkit COMP from your project.
1. Download the new toolkit tox and drop it into your project.
1. Select all RayTK operators in your scene. That means any operator that has the RayTK-style viewer image on the COMP, as well as any RayTK panel COMPs like `raymarchPreviewPanel`.
1. In the parameter panel, on the first page, click "Update OP"

## Warning

It is possible that parts of the scene may behave differently or might get disconnected (which is why backups are important).

One particularly common issue is a change in the scaling of the `Period` parameter in `waveField` and similar operators. Early versions of the toolkit incorrectly scaled the period to much larger values than they were supposed to. So you may need to increase those settings after the update.

