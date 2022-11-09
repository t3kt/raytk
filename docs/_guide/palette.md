---
layout: page
title: The Palette
nav_order: 3
---

# The RayTK Palette

The palette is the main tool for creating RayTK operators.

The palette can be opened using the ALT+R shortcut. The shortcut can be customized by changing the `Keyboard Shortcut`
parameter on the main toolkit COMP.

The palette can also be opened by clicking the `Show Palette` parameter on the toolkit COMP.

By default, the palette closes after creating an operator, but it can be pinned open using the button on the top right
next to the close button.

## Parts of the Palette

![RayTK Palette](/raytk/assets/images/guide/palette-parts.png)

1. Toolkit version.
2. Pin toggle to keep the palette open after creating operators.
3. Button to close the palette.
4. Shortcut for an operator that can be entered into the search field.
5. An operator. Clicking this will create one of these operators.
6. Thumbnail for an operator (if available). This can be shown or hidden (for a more condensed layout) using the thumbnails toggle.
7. An operator category. Clicking this will expand or collapse a category of operators in the list.
8. Search field. Searching will match operator names, operator keywords, shortcuts (e.g. `sph` for `sphereSdf`), and abbreviations (e.g. `fgr` for `functionGraphRender`).
9. Button to clear the search field.
10. Filter toggles that show/hide:
  * Alpha operators: experimental operators, which are only available in experimental releases.
  * Beta operators: operators that work, but are still in development and may change in future releases.
  * Deprecated operators: operators that have been replaced by newer alternatives and may be removed in future releases.
11. Button to toggle showing thumbnails. Hiding thumbnails condenses the layout of the list.
12. Toggle to expand/collapse the help section.
13. Help section which shows a description of the highlighted operator (if available).


## Keyboard Interaction

When the palette opens, keyboard focus is automatically put into the filter field, so you can search for operators by
typing, without having to click on anything.

Using the up/down arrow keys will move focus in the main list, stepping through whatever operators are shown. Using the
enter key will create the selected operator (and close the palette if it isn't pinned).