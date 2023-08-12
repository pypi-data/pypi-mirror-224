import click
import trycortex.cli.callable.commands as callable_commands
import os

CONFIG_PATH = os.path.expanduser("~/.cortex_config")

class CliContext:
    def __init__(self):
        self.api_key = None

def save_config(api_key):
    with open(CONFIG_PATH, "w") as fp:
        fp.write(api_key)

def load_config():
    if not os.path.exists(CONFIG_PATH):
        return None
    with open(CONFIG_PATH, "r") as fp:
        return fp.read()

@click.group()
@click.pass_context
def cortex(ctx):
    ctx.ensure_object(CliContext)
    ctx.obj.api_key = load_config()

@click.command("auth", help="Authenticates with Cortex.")
@click.option("--apikey", help="API key to use.")
@click.pass_context
def auth(ctx, apikey):
    if apikey is None:
        apikey = click.prompt("API Key")
    save_config(apikey)
    ctx.obj.api_key = apikey

# subcommands
cortex.add_command(callable_commands.callable)
cortex.add_command(auth)

# aliases
cortex.add_command(callable_commands.init_callable, "init")

if __name__ == '__main__':
    cortex()