# parMenuUpdater

Updates the contents of a menu parameter based on a table DAT.

This is similar to using `menuSource`, but it updates the menu
imperatively, only when the table changes (or when manually triggered).
Using `menuSource` sets up a dependency that can introduce bugs
and performance issues. This approach allows things like only updating
the menu when in development mode and locking it during the build
process.