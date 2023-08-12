# IO-TEMPLATE-LIB - Template for Library Repositories

This repository is a sample repository for developing Python related IO-Aero libraries.

## Documentation

Since this is a private repository, the complete documentation is only available in a local version of the repository in the file directory **`site`**. 
You just have to open the file **`site/index.html`** with a web browser.

## Directory and File Structure of this Repository

### 1. Directories

| Directory         | Content                                                    |
|-------------------|------------------------------------------------------------|
| .github/workflows | **[GitHub Action](https://github.com/actions)** workflows. |
| .vscode           | Configuration data for **Visual Code**.                    |
| data              | Application data related files.                            |
| dist              | Deployable libraries.                                      |
| docs              | Documentation files.                                       |
| iotemplatelib     | Python script files.                                       |
| libs              | Required third party libraries.                            |
| resources         | Selected manuals and software.                             |
| scripts           | Scripts supporting Ubuntu and Windows.                     |
| site              | Documentation as static HTML pages.                        |
| tests             | Scripts and data for **pytest**.                           |

### 2. Files

| File                           | Functionality                                                   |
|--------------------------------|-----------------------------------------------------------------|
| .gitignore                     | Configuration of files and folders to be ignored.               |
| .pylintrc                      | **pylint** configuration file.                                  |
| .settings.io_template_lib.toml | Configuration data - secrets.                                   |
| LICENSE.md                     | Text of the licence terms.                                      |
| logging_cfg.yaml               | Configuration of the Logger functionality.                      |
| Makefile                       | Tasks to be executed with the **`make`** command.               |
| Pipfile                        | Definition of the Python package requirements.                  |
| pyproject.toml                 | Optional configuration data for the software quality tools.     |
| README.md                      | This file.                                                      |
| run_io_template_lib            | Main script for using the functionality of **IO-TEMPLATE-LIB**. |
| settings.io_template_lib.toml  | Configuration data.                                             |
| setup.cfg                      | Optional configuration data for **flake8**.                     |
