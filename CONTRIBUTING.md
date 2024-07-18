# Contributing to RayTK

## Developer Environment and Editor Setup

RayTK is written in Touch Designer (.toe & .tox files) and Python.

- Lastest Touch Designer should be used.

- Python version is tracked in `.python-version` file.

- [PyCharm](https://www.jetbrains.com/pycharm/) is the easiest to get started. Refer to [.idea.example/](/.idea.example/) for PyCharm specific configuration.

- You can use either macOS or Windows OS

## Developer Workflow

### Updating RayTK

To modify RayTK, open `raytk-development.toe` in Touch Designer. You should see `RayTK Toolkit Editor` and TD project open up.

To modify python files, open the cloned repository in `PyCharm`. TD native pythong imports do not get LSP support by default. In python files, change `if False:` to `if True:` to see stubbed definitions.

Python files should automatically reload in TD.

You can test your changes within `raytk-development.toe` by pressing `alt + r`.

### Generate new `.tox` file

To build a new `.tox` file, open `raytk-build.toe` in Touch Designer.

At the bottom, click the `Run Toolkit Build` button. TD might hang for a few minutes but build logs should come up.

After the build completes, check the `build/` directory for a new `RayTK-0.XX-exp.tox` file. You can use this to test RayTK in a fresh project.

