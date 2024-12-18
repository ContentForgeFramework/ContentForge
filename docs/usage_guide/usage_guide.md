# How to use this framework

## Getting started

First, you need to install pipx. The recommended approach is to install pipx within a virtual environment (venv).
If you don't have a venv, you can create one by running the following command:

```bash
python -m venv venv
```

Then, open a terminal and activate the venv:

```bash
# On Windows
venv\Scripts\activate
```

Now you can install pipx:

```bash
python -m pip install pipx
```

After installing pipx, it's recommended to set the pipx venv path and home path to a convenient location.
For example, to install to ```D:\Global\Location``` on Windows PowerShell, use the following commands:

```powershell
$env:PIPX_HOME="D:\Global\Location\env"
$env:PIPX_BIN_DIR="D:\Global\Location\bin"
```

> Tips:
> The commands must be run every time you open a new terminal session before installed success poetry.

Wait for a moment, and then make sure to add ```D:\Global\Location\bin``` to your system's PATH environment variable.
Alternatively, you can use the following command to add it to the PATH (within the venv):

```bash
pipx ensurepath
```

Please ensure that the pipx path is correctly added to the PATH environment variable.

Now, you can install Poetry using pipx:

```bash
pipx install poetry
```

After installing Poetry, check the Poetry version with:

```bash
poetry --version
```

Good Job! You can install [ContentForge](../../README.md) framework now.

## Install ContentForge

Download zip file from [ContentForge](https://github.com/ContentForgeFramework/ContentForge.git) and extract it to your project directory.

You can also download the repository using the following command:

```bash
curl -L -o ContentForge.zip https://github.com/ContentForgeFramework/ContentForge/archive/refs/heads/main.zip
```

Now, navigate to the ContentForge directory.

Please rebuild the git repository by running the following command:

```bash
git init
git add -A
git commit -m "Initial commit"
```

and install the framework dependencies using the following command:

```bash
poetry install
```

Dependencies will be installed in the venv directory. Use the following command to check the framework version:

```bash
# installed py launcher
py artisan -v

# or
python artisan -v

# Output
version: 0.1.0
```

If you need help with the CLI, use the following command:

```bash
py artisan --help
```

## Create a new project

## Available commands

Check the [Available commands](../usage_guide/cli_usage.md) for a complete list of commands that can be used with the CLI.

## Q&A

Please visit the [FAQ](./FAQ.md) page for more information.
