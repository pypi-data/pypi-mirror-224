import click
import trycortex.cli.callable.commands as callable_commands

class CliContext:
    def __init__(self):
        self.api_key = None

@click.group()
@click.pass_context
def cortex(ctx):
    ctx.ensure_object(CliContext)

@click.command("auth", help="Authenticates with Cortex.")
@click.option("--apikey", help="API key to use.")
@click.pass_context
def auth(ctx, apikey):
    ctx.ensure_object(CliContext).api_key = apikey

# subcommands
cortex.add_command(callable_commands.callable)

# aliases
cortex.add_command(callable_commands.init_callable, "init")

if __name__ == '__main__':
    cortex()