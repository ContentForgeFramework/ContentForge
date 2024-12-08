# Framework CLI

The Command Line Interface (CLI) is a tool designed to assist in managing and streamlining project tasks through various commands.

## How to use the CLI

- All CLI commands should be executed from the root of the project.
- To run a command, use the following syntax: `py artisan <command> [options]`.
- To view a list of available commands, run: `py artisan --help`.
- To see detailed help for a specific command, use: `py artisan <command> --help`.


## How to create a new command

1. Create a new Python script file in the `vendor/contentforge/utils/command` directory.
2. The program will automatically detect the command file and add it to the CLI.
3. Define a function named `def cli()` in the new command file.
4. Import the `click` package and apply the `@click.command` decorator to the `cli()` function.
5. Use the `@click.option` decorator to define options for the `cli()` function.
6. Ensure the function's arguments correspond to the command's options.
7. Use `click.echo` within the function to output messages.

> Tips:  
> Refer to the sample file [example.py](../../vendor/contentforge/utils/command/example.py) for guidance on coding a command.  
>  
> Please refer to the [Click documentation](https://click.palletsprojects.com/en/stable/) for more information on creating commands.  
>  
> Check the [Available commands](../usage_guide/cli_usage.md) for a complete list of commands that can be used with the CLI.


