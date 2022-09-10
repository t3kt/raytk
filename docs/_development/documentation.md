---
layout: page
title: Documentation Processing
nav_order: 6
---

# Documentation Processing

The RayTK [documentation site](https://t3kt.github.io/raytk/) is served by GitHub pages, from the main branch of the repository, using the Jekyll [Just the Docs](https://github.com/just-the-docs/just-the-docs) theme.

The documentation content itself falls several categories:

1. Manually written documentation, like this page.
2. Operator reference pages ([example](/raytk/reference/operators/sdf/boxSdf)).
3. Generated index / list pages ([example](/raytk/reference/operators/sdf/)).

## Operator Reference Pages

During the [build process](/raytk/development/build-process/), the builder generates a page of documentation for each operator.

For each operator, documentation is pulled from several sources:

* Manually written Markdown file (not present for all operators)
* Metadata from the operator definition
* Parameter help
* Metadata from inputs

The manually written documentation files contain:

* Summary paragraph(s) that describe what the operator does
* A list of parameters with a description for each (though not all parameters may have written documentation)
  * For menu parameters, a list of the menu options with descriptions

The toolkit editor can synchronize the parameter documentation between manually written docs and the help properties of the custom parameters on the operator.
During the build process, the builder pulls the help properties for any parameters that don't appear in the documentation to produce a complete list. Certain special parameters (like `Update OP` and `Inspect`) are stripped out from the list.

Each `inputHandler` within the operator can have properties and dynamically generated metadata that describes what the input is used for, whether it's required, and what coordinate/context/return types it supports.

All of this data is compiled together and output into a file in the `docs/_reference/` directory.