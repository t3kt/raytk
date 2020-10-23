# RayTK Development and Design Principles

## End User Experience Requirements

* It needs to be extremely stable for end users. A library that cannot be consistently relied upon is largely pointless.
* Once the library is dropped into a project and a scene is constructed using it, that scene should always work correctly in the future.
* Version updates should be (a) entirely optional and deliberate, and (b) managed by automated tools.
* End users should only ever use built packages, which are versioned (e.g. RayTK-0.5.tox). These are added as release binaries on GitHub.
* Once created (and merged into the main branch), a built package should never change again.
* The built package should be 100% self-contained.
* All references to external files should be stripped off in the build process.

Anything unnecessary for the end user should be stripped off in the build process.

## End User vs Developer

While end users only use the "binaries", the source of the repo itself is the developer view of the system.

It consists of a structure of a set of "apps" (launchable .toe projects) that serve several different purposes, and several directories of components and dependencies.

## Developer Apps

* `raytk-development.toe`: This is used for most development activities, including making changes to ROPs or the related infrastructure.
* `raytk-build.toe`: This is used to run the build process to create a new release.
