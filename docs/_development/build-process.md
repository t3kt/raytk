---
layout: page
title: The Build Process
nav_order: 2
---

# The Build Process

The toolkit uses a build process which produces a totally self-contained "built" tox. End users of the toolkit drop one of those built tox files into their projects and use the integrated tools such as the palette to create instances of the types of ROPs defined in the toolkit.

## Why There is a Build Process

The build process exists to ensure that projects using the toolkit will always work on their own and cannot be broken by changes to dependencies or external files. It also allows developers to work on the toolkit without breaking any of their own projects that use built versions of the toolkit.

## Toolkit Source

The source used to build the toolkit is defined in a structure of directories and files which are stored an managed in the github repository. The source is split into many files in order to simplify source control and version management. Most COMPs are attached to external files, and most code DAT, tables, and other such data is also synced with external files.

## Versioning

Development on the toolkit is managed by versions, with an associated git branch, and a tag (for completed versions). All development work is done in these versioned branches. When a version is completed, a tag is created along with a release on github. The branch is then merged into master using a pull request.

Starting a new version involves starting a new numbered branch off of master, and then the properties of the toolkit tox are updated with the new version.

## The Build Tool

The build tool is a launchable project file named `raytk-build.toe`. The interface shows some options, a build log, and buttons for performing build-related actions. When starting a build, the tool loads the entire toolkit from the source files, and then walks through it applying various types of modifications. As it does this, it prints messages to the build log, which are shown in the UI. At the end of the process, the tool exports the toolkit tox file, using a name based on the current version (e.g. `raytk-0.7.tox`).

## Modifications Applied in the Build Process

The build tool performs several types of modifications, including:

* Detaching from external files (such as tox and text files).
* Freezing generated data tables and properties.
* Detaching cloned COMPs from their masters.
* Stripping out development-only items.
* Extracting and exporting documentation files.

## OP Tags

The build process looks for several types of tags on OPs and applies different modifications to them.

* `fileSync`: A DAT that is bound to an external text file. During the build process these references are detached and sync is deactivated. This tag is also used in editing tools as an indication that OPs are synced to external files.
* `buildLock`: A DAT or other OP that is dynamically generated while in development mode, but is locked during the build process. This can be used to avoid having to run processes such as searching for OPs when the built toolkit is loaded into a project.
* `buildExclude`: An OP that is stripped out during the build process. For example, OPs used to produce tables that use `buildLock` are not needed in the built toolkit. Master instances of shared components are also removed (since clones of them are detached during build).

## Build Scripts

## Documentation Processing
