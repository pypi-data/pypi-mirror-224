from dataclasses import asdict
import functools
import importlib
import pathlib
import re
from typing import List
import click
import validators
import os
import urllib.request
import trycortex
import rich.console as rich_console
from typing import Dict, List, Tuple
import venv
import subprocess
from trycortex.callables.base import Callable
import json
import sys
import requests
import time
import itertools

from trycortex.cli.callable import callable_config
from trycortex.api import *

# Regex pattern to match valid entry points: "module:object"
VAR_NAME_RE = r"(?![0-9])\w+"
ENTRY_POINT_PATTERN = re.compile(rf"^{VAR_NAME_RE}(\.{VAR_NAME_RE})*:{VAR_NAME_RE}$")
VISIBILITY_RE = r"^(Private|private|Public|public|Unlisted|unlisted)$"
VISIBILITY_PATTERN = re.compile(VISIBILITY_RE)
TEMPLATE_RE = r"^(barbone|chat|chat with history)$"
TEMPLATE_PATTERN = re.compile(TEMPLATE_RE)

REQUIREMENTS_TXT = "requirements.txt"
CURRENT_CORTEX_REQUIREMENT = f"trycortex ~= {trycortex.__version__}"
CORTEX_REQUIREMENT_PATTERN = re.compile(r"^\s*trycortex([^\w]|$)")

CALLABLE_TEMPLATE_URL = (
    "https://raw.githubusercontent.com/kinesysai/cortex-py/main/template.py"
)



@click.group(help="Callable-related commands")
def callable():
    pass

def _slugify(s: str) -> str:
    s = s.lower().strip()
    s = re.sub(r"[^\w\s-]", "", s)
    s = re.sub(r"[\s_-]+", "-", s)
    s = s.strip("-")
    return s


@callable.command("addblock", help="Adds a block to the callable.")
@click.option("--type", help="Type of the block.")
@click.option("--name", help="Name of the block.")
@click.argument("path", required=False)
def add_block(path, type:str, name:str):
    click.echo("add block")
    path = pathlib.Path(path or ".")
    blocks_path = os.path.join(path, "blocks")
    os.makedirs(blocks_path, exist_ok=True)

    if type is None:
        type = click.prompt("Type")

    while name is None or not validators.slug(name):
        if name is not None:
            click.secho("Name can be alpha numerics and dashes only.")
        name = click.prompt("Name")

    block_path = os.path.join(blocks_path, name.upper())
    os.makedirs(block_path, exist_ok=True)
    if type.lower() == "code":
        
        default_code = """\
_fun = (env) => {
  // use `env.state.BLOCK_NAME` to refer output from previous blocks.
 return; 
}
"""
        code_path = os.path.join(block_path, "code.js")
        with open(code_path, "w") as file:
            file.write(default_code)
        
        script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
code_path = os.path.join(path, "code.js")
with open(code_path, 'r') as file:
    js_code = file.read()
spec = blocks.CodeSpec(code=js_code)
block = blocks.Block(type=\"""" + type +  """",name=\"""" + name + """", indent=0, spec=spec, config={})
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)

    # check what type of block it is
    # create block according to type and name and initialize it
    # create new folder in blocks folder for the new block
    # add a python file initializing the new block
    elif type.lower() == "model":
        script_content = """\
from trycortex.callables import blocks

spec = blocks.ModelSpec(temperature=0.7, max_tokens=1024, few_shot_count=3, few_shot_prompt="", few_shot_preprompt="", prompt="", stop=[])
config = blocks.ModelConfig(provider_id="openai", model_id="gpt-3.5-turbo", use_cache=True, use_semantic_cache=False)

block = blocks.Block(type=\"""" + type + """", name=\""""+ name +  """", indent=0, spec=spec, config=config)
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)
    elif type.lower() == "search":
        script_content = """\
from trycortex.callables import blocks

spec = blocks.SearchSpec(query="", num=3)
config = blocks.SearchConfig(provider_id="serpapi", use_cache=True)

block = blocks.Block(type="search", name=\"""" + name + """", indent=0, spec=spec, config=config)
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)
    elif type.lower() == "map":
        map_content = """\
from trycortex.callables import blocks

spec = blocks.MapSpec(from_="INPUT", repeat="")
block = blocks.Block(type="map", name=\"""" + name + """", indent=0, spec=spec, config={})
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(map_content)
        reduce_content = """\
from trycortex.callables import blocks

block = blocks.Block(type="reduce", name=\"""" + name + """", indent=0, spec={}, config={})
"""
        reduce_name = "reduce.py"
        reduce_path = os.path.join(block_path, reduce_name)
        with open(reduce_path, "w") as file:
            file.write(reduce_content)
    elif type.lower() == "knowledge":
        script_content = """\
from trycortex.callables import blocks

spec = blocks.KnowledgeSpec(query="", full_text=False)
config = blocks.KnowledgeConfig(knowledge=None, top_k=8, filter={"tags": None, "timestamp": None}, use_cache=False)
block = blocks.Block(type="knowledge", name=\"""" + name + """", indent=0, spec=spec, config=config)
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)
    elif type.lower() == "data":
        data_content = """\
    from trycortex.callables import blocks

    spec = dict()
    config = dict()
    block = blocks.Block(type="data", name=\"""" + name + """", indent=0, spec=spec, config=config)
    """
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(data_content)
    elif type.lower() == "browser":
        script_content = """\
from trycortex.callables import blocks

spec = blocks.BrowserSpec(url="", selector="body", timeout=16000, wait_until="networkidle2")
config = blocks.BrowserConfig(provider_id="", use_cache=True, error_as_output=True)
block = blocks.Block(type="browser", name=\"""" + name + """", indent=0, spec=spec, config=config)
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)
    elif type.lower() == "curl":
        default_headers_code = '''_fun = (env) => {
  return {"Content-Type": "application/json"};
}
'''
        headers_code_path = os.path.join(block_path, "headers_code.js")
        with open(headers_code_path, "w") as file:
            file.write(default_headers_code)
        
        default_body_code = '''_fun = (env) => {
  // return a string or null to skip sending a body.
  return JSON.stringify({ foo: "bar" });
}
'''
        body_code_path = os.path.join(block_path, "body_code.js")
        with open(body_code_path, "w") as file:
            file.write(default_body_code)
        
        script_content = """from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))

headers_code_path = os.path.join(path, "headers_code.js")
with open(headers_code_path, 'r') as file:
    headers_js_code = file.read()

body_code_path = os.path.join(path, "body_code.js")
with open(body_code_path, 'r') as file:
    body_js_code = file.read()

spec = blocks.CurlSpec(scheme="HTTPS", method="POST", url="", headers_code=headers_js_code, body_code=body_js_code)
config = blocks.CurlConfig(use_cache=True)

block = blocks.Block(type="curl", name=\"""" + name + """", indent=0, spec=spec, config=config)
"""
        script_name = name.lower() + ".py"
        script_path = os.path.join(block_path, script_name)
        with open(script_path, "w") as file:
            file.write(script_content)

    main_path = os.path.join(path, "main.py")
    with open(main_path, 'r') as file:
        main_content = file.read()
    import_statement = f"import blocks.{name.upper()}.{name.lower()} as {name.lower()}\n"
    updated_import = import_statement + main_content
    with open(main_path, 'w') as file:
        file.write(updated_import)




@callable.command("init", help="Creates an callable.yaml file.")
@click.option("--name", help="Name of the callable.")
@click.option("--description", help="Description of the callable.")
@click.option("--visibility", help="Visibility of the callable.")
@click.option("--template", help="Template of the callable.")
@click.option("--entry-point", help="Python entry point of the callable.")
@click.argument("path", required=False)
@click.pass_context
def init_callable(ctx, path, name, description, visibility, template, entry_point:str):
    click.echo("init callable")
    path = pathlib.Path(path or ".")
    path.mkdir(parents=True, exist_ok=True)

    try:
        current_config = callable_config.load_config(path)
    except FileNotFoundError:
        current_config = callable_config.CallableConfig(name=_slugify(path.resolve().name))

    
    while name is None or not validators.slug(name):
        if name is not None:
            click.secho("Name can be alpha numerics, underscores and dashes only.")
        name = click.prompt("Name", default=current_config.name)

    if description is None:
        description = click.prompt("Description", default=current_config.description)

    while entry_point is None or not ENTRY_POINT_PATTERN.match(entry_point):
        if entry_point is not None:
            click.echo(
                "Entrypoint must be in module:attribute format (e.g. 'main:callable', 'main:run')"
            )

        entry_point = click.prompt(
            "Python Entrypoint (module:attribute)", default=current_config.entry_point
        )
    
    while visibility is None or not VISIBILITY_PATTERN.match(visibility):
        if visibility is not None:
            click.secho("Visibility should be one of private, public or unlisted.")
        visibility = click.prompt("Visibility", default=current_config.visibility)

    while template is None or not TEMPLATE_PATTERN.match(template):
        if template is not None:
            click.secho("Template should be one of barbone, chat or chat with history")
        template = click.prompt("Template", default=current_config.template)
    
    current_config.name = name
    current_config.description = description
    current_config.entry_point = entry_point
    current_config.visibility = visibility
    current_config.template = template

    url = "http://127.0.0.1:3000/api/sdk/callable/create"

    apikey = ctx.obj.api_key
    if apikey is None:
        click.echo("No API key found. Please run `cortex auth` first.")
        return

    cortex = CortexAPI(apikey)
    copyTo = cortex.getIDFromKey()

    payload = json.dumps({
    "appName": name,
    "appDescription": description,
    "appVisibility": visibility,
    "callableTemplate": template,
    "copyTo": copyTo
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + apikey
    }

    response = requests.request("POST", url, headers=headers, data=payload)

    sID = response.json()['sID']

    current_config.sID = sID

    callable_config.save_config(current_config, path)

    entry_module, _ = entry_point.split(":")
    expected_main_path = path / (entry_module.replace(".", "/") + ".py")
    if not os.path.exists(expected_main_path):
        urllib.request.urlretrieve(CALLABLE_TEMPLATE_URL, expected_main_path)
        click.secho(
            f"Initialized callable.yaml and made a template callable file at {expected_main_path}",
            fg="green",
        )
    else:
        click.secho(f"Initialized callable.yaml.", fg="green")


    blocks_path = os.path.join(path, "blocks")
    os.makedirs(blocks_path, exist_ok=True)

    output = os.path.join(blocks_path, "OUTPUT")
    os.makedirs(output, exist_ok=True)
    output_path = os.path.join(output, "output.py")
    output_content = """\
from trycortex.callables import blocks

block = blocks.OutputBlock(spec={})
"""
    with open(output_path, "w") as file:
        file.write(output_content)

    input = os.path.join(blocks_path, "INPUT")
    os.makedirs(input, exist_ok=True)
    input_path = os.path.join(input, "input.py")
    input_content = """\
from trycortex.callables import blocks

config = blocks.InputConfig(dataset="QADataset")

block = blocks.Block(type="input", name="INPUT", indent=0, spec={}, config=config)
"""
    with open(input_path, "w") as file:
        file.write(input_content)


def _validate_callable_path(ctx, param, value):
    normalized = callable_config.normalize_path(value)
    if not os.path.exists(normalized):
        if not click.confirm(
            f"{normalized} does not exist. Would you like to create a new callable?",
            default=True,
        ):
            raise click.BadParameter(f"{normalized} does not exist")

        ctx.invoke(init_callable, path=value)

        # Re-normalize it after running init.
        normalized = callable_config.normalize_path(value)

    return normalized

@callable.command("deploy", help="Deploy the current callable.")
@click.argument("path", callback=_validate_callable_path, required=False)
@click.pass_context
def deploy(ctx, path):
    click.echo("Deploying callable...", nl=True)
    path = pathlib.Path(path or ".")
    config = callable_config.load_config(path)
    url = "http://127.0.0.1:3000/api/sdk/callable/deploy"

    sId = config.sID

    payload = json.dumps({
    "sId": sId
    })

    apikey = ctx.obj.api_key

    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + apikey
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    click.secho("Callable has been successfully deployed!", fg='green')


@callable.command("runtests", help="Runs tests for the current callable.")
@click.argument("path", callback=_validate_callable_path, required=False)
@click.pass_context
def runtests(ctx, path):
    console = rich_console.Console(soft_wrap=True)
    click.echo("Running...\n")
    path = pathlib.Path(path or ".")
    config = callable_config.load_config(path)
    callable_dir = os.path.dirname(path) or "."
    sys.path.insert(0, callable_dir)
    entry_point_parts = config.entry_point.split(":", 1)
    module_name = entry_point_parts[0]
    attr = entry_point_parts[1] if len(entry_point_parts) == 2 else "callable"
    module = importlib.import_module(module_name)
    impl = getattr(module, attr)
    if isinstance (impl, Callable):
        callable_impl = impl
    else:
        console.print("configured entry point is not a callable")
        pass
    callable_blocks = callable_impl.get_blocks()
    block_json = [asdict(block) for block in callable_blocks]
    saveSpec = json.dumps(block_json)
    url = "http://127.0.0.1:3000/api/sdk/callable/update"

    sId = config.sID

    apikey = ctx.obj.api_key

    update_payload = json.dumps({
        "sId": sId,
        "specification": saveSpec
    })

    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apikey
    }
    update_response = requests.request("POST", url, headers=headers, data=update_payload)

    runtests_url = "http://127.0.0.1:3000/api/sdk/callable/runtests"

    runtests_payload = json.dumps({
    "sId": sId,
    "mode": "design"
    })

    runtests_response = requests.request("POST", runtests_url, headers=headers, data=runtests_payload)
    runId = runtests_response.json()["run"]["run_id"]
    block_url = "http://127.0.0.1:3000/api/sdk/callable/runblock"


    for block in block_json:
        block_payload = {
            "sId": sId,
            "runId": runId,
            "type": block['type'],
            "name": block['name'],
        }
        block_response = requests.request("POST", block_url, headers=headers, data=json.dumps(block_payload))

        running = block_response.json()["run"]["status"]["run"]
        spinner = itertools.cycle(['-', '/', '|', '\\'])
        click.echo('\033[?25l', nl=False)
        while running == "running":
            click.echo(next(spinner), nl=False)
            click.echo('\b', nl=False)
            time.sleep(0.1)
            block_response = requests.request("POST", block_url, headers=headers, data=json.dumps(block_payload))
            running = block_response.json()["run"]["status"]["run"]
        click.echo('\033[?25h', nl=False)

        name = block['name']
        block_type = block['type']
        values = block_response.json()["run"]["traces"]
        click.echo(click.style(f"{block_type} {name}:", bold=True, fg='green'))
        for value_group in values:
            for value_values in value_group[1]:
                value_data = value_values[0]
                val = value_data.get('input', '') if 'input' in value_data else value_data.get('value', {})
                duration = value_data.get('meta', {}).get('duration', '')
                error = value_data.get('error')
                if error:
                    click.echo(f"    - {val} (Error: {error})")
                else:
                    click.echo(f"    - {val} (Duration: {duration}s)")
                    

    

@callable.command("fetch", help="Fetch the current callable.")
@click.argument("path", callback=_validate_callable_path, required=False)
@click.pass_context
def fetch(ctx, path):
    path = pathlib.Path(path or ".")
    config = callable_config.load_config(path)
    url = "http://127.0.0.1:3000/api/sdk/callable/spec"
    sId = config.sID
    apikey = ctx.obj.api_key
    payload = json.dumps({
    "sId": sId
    })
    headers = {
    'Content-Type': 'application/json',
    'Authorization': 'Bearer ' + apikey
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    app = response.json()['app']
    config.name = app['name']
    config.description = app['description']
    config.visibility = app['visibility']
    callable_config.save_config(config, path)
    spec = app['savedSpecification']
    spec_json = json.loads(spec)
    blocks_path = os.path.join(os.path.dirname(path), "blocks")
    os.makedirs(blocks_path, exist_ok=True)
    for block in spec_json:
        block_path = os.path.join(blocks_path, block['name'].upper())
        os.makedirs(block_path, exist_ok=True)
        if block['type'] == 'code':
            code_path = os.path.join(block_path, "code.js")
            with open(code_path, "w") as file:
                file.write(block['spec']['code'])
            script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
code_path = os.path.join(path, "code.js")
with open(code_path, 'r') as file:
    js_code = file.read()
spec = blocks.CodeSpec(code=js_code)
block = blocks.Block(type=\"""" + block['type'] +  """",name=\"""" + block['name'] + """", indent=0, spec=spec, config={})
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(script_content)
        elif block['type'] == 'knowledge':
            knowledge_path = os.path.join(block_path, "knowledge.txt")
            with open(knowledge_path, "w") as file:
                file.write(block['spec']['query'])
            script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
knowledge_path = os.path.join(path, "knowledge.txt")
with open(knowledge_path, 'r') as file:
    query = file.read()
spec = blocks.KnowledgeSpec(query=query, full_text=False)
config = blocks.KnowledgeConfig(knowledge=[], top_k=8, filter={}, use_cache=False)
block = blocks.Block(type=\"""" + block['type'] +  """",name=\"""" + block['name'] + """", indent=0, spec=spec, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(script_content)
        elif block['type'] == 'model':
            model_path = os.path.join(block_path, "model.txt")
            with open(model_path, "w") as file:
                file.write(block['spec']['prompt'])
            script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
model_path = os.path.join(path, "model.txt")
with open(model_path, 'r') as file:
    prompt = file.read()
spec = blocks.ModelSpec(temperature=0.7, max_tokens=1024, few_shot_count=3, few_shot_prompt="", few_shot_preprompt="", prompt=prompt, stop=[])
config = blocks.ModelConfig(provider_id="openai", model_id="gpt-3.5-turbo", use_cache=True, use_semantic_cache=False)
block = blocks.Block(type=\"""" + block['type'] +  """",name=\"""" + block['name'] + """", indent=0, spec=spec, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(script_content)
        elif block['type'] == 'search':
            search_path = os.path.join(block_path, "search.txt")
            with open(search_path, "w") as file:
                file.write(block['spec']['query'])
            script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
search_path = os.path.join(path, "search.txt")
with open(search_path, 'r') as file:
    query = file.read()
spec = blocks.SearchSpec(query=query, num=3)
config = blocks.SearchConfig(provider_id="serpapi", use_cache=True)
block = blocks.Block(type=\"""" + block['type'] +  """",name=\"""" + block['name'] + """", indent=0, spec=spec, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(script_content)
        elif block['type'] == 'map':
            map_path = os.path.join(block_path, "map.txt")
            with open(map_path, "w") as file:
                file.write(block['spec']['repeat'])
            script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
map_path = os.path.join(path, "map.txt")
with open(map_path, 'r') as file:
    repeat = file.read()
spec = blocks.MapSpec(from_="INPUT", repeat=repeat)
block = blocks.Block(type=\"""" + block['type'] +  """",name=\"""" + block['name'] + """", indent=0, spec=spec, config={})
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(script_content)
        elif block['type'] == 'reduce':
            reduce_content = """\
from trycortex.callables import blocks

block = blocks.Block(type="reduce", name=\"""" + block['name'] + """", indent=0, spec={}, config={})
"""
            reduce_name = "reduce.py"
            reduce_path = os.path.join(block_path, reduce_name)
            with open(reduce_path, "w") as file:
                file.write(reduce_content)
        elif block['type'] == 'search':
            search_path = os.path.join(block_path, "search.txt")
            with open(search_path, "w") as file:
                file.write(block['spec']['query'])
            script_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
search_path = os.path.join(path, "search.txt")
with open(search_path, 'r') as file:
    query = file.read()
spec = blocks.SearchSpec(query=query, num=3)
config = blocks.SearchConfig(provider_id="serpapi", use_cache=True)
block = blocks.Block(type=\"""" + block['type'] +  """",name=\"""" + block['name'] + """", indent=0, spec=spec, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(script_content)
        elif block['type'] == 'browser':
            browser_path = os.path.join(block_path, "browser.txt")
            with open(browser_path, "w") as file:
                file.write(block['spec']['url'])
            browser_content = """\
from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
browser_path = os.path.join(path, "browser.txt")
with open(browser_path, 'r') as file:
    url = file.read()
spec = blocks.BrowserSpec(url=url, selector="body", timeout=16000, wait_until="networkidle2")
config = blocks.BrowserConfig(provider_id="", use_cache=True, error_as_output=True)
block = blocks.Block(type="browser", name=\"""" + block['name'] + """", indent=0, spec=spec, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, "w") as file:
                file.write(browser_content)
        elif block['type'] == 'curl':
            headers_path = os.path.join(block_path, "headers_code.js")
            with open(headers_path, "w") as file:
                file.write(block['spec']['headers_code'])
            body_path = os.path.join(block_path, "body_code.js")
            with open(body_path, "w") as file:
                file.write(block['spec']['body_code'])
            script_content = """from trycortex.callables import blocks
import os
path = os.path.dirname(os.path.abspath(__file__))
headers_path = os.path.join(path, "headers_code.js")
with open(headers_path, 'r') as file:
    headers_js_code = file.read()
body_path = os.path.join(path, "body_code.js")
with open(body_path, 'r') as file:
    body_js_code = file.read()
spec = blocks.CurlSpec(scheme="HTTPS", method="POST", url="", headers_code=headers_js_code, body_code=body_js_code)
config = blocks.CurlConfig(use_cache=True)
block = blocks.Block(type="curl", name=\"""" + block['name'] + """", indent=0, spec=spec, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, 'w') as file:
                file.write(script_content)
        elif block['type'] == 'input':
            script_content = """\
from trycortex.callables import blocks

config = blocks.InputConfig(dataset=\"""" + block['config']['dataset'] + """")

block = blocks.Block(type="input", name="INPUT", indent=0, spec={}, config=config)
"""
            script_name = block['name'].lower() + ".py"
            script_path = os.path.join(block_path, script_name)
            with open(script_path, 'w') as file:
                file.write(script_content)
    


@callable.command("update", help="Deploy the current agent.")
@click.argument("path", callback=_validate_callable_path, required=False)
@click.pass_context
def update(ctx, path):
    console = rich_console.Console(soft_wrap=True)
    path = pathlib.Path(path or ".")
    config = callable_config.load_config(path)
    callable_dir = os.path.dirname(path) or "."
    sys.path.insert(0, callable_dir)
    entry_point_parts = config.entry_point.split(":", 1)
    module_name = entry_point_parts[0]
    attr = entry_point_parts[1] if len(entry_point_parts) == 2 else "callable"
    module = importlib.import_module(module_name)
    impl = getattr(module, attr)
    if isinstance (impl, Callable):
        callable_impl = impl
    else:
        console.print("configured entry point is not a callable")
        pass
    callable_blocks = callable_impl.get_blocks()
    block_json = [asdict(block) for block in callable_blocks]
    with open('output.json', 'w') as file:
        json.dump(block_json, file)
    #with open('output.json', 'r') as file:
    #    saveSpec = file.read()
    #saveSpec = str(block_json).replace("'",'"')
    saveSpec = json.dumps(block_json)

    print(saveSpec)
    url = "http://127.0.0.1:3000/api/sdk/callable/update"

    sId = config.sID

    apikey = ctx.obj.api_key

    payload = json.dumps({
        "sId": sId,
        "specification": saveSpec
    })
    #print(payload)
    headers = {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer ' + apikey
    }
    response = requests.request("POST", url, headers=headers, data=payload)
    #print(response.text)


