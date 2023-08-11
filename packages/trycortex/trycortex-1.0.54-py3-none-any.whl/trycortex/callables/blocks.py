import dataclasses

from trycortex.cli import utils
from typing import Union, Optional
import json
from collections import defaultdict

@dataclasses.dataclass
class CodeSpec:
    """Represents the spec for the code block in a callable."""
    code: str

@dataclasses.dataclass
class DataSource:
    project_id: str
    data_source_id: str

@dataclasses.dataclass
class KnowledgeSpec:
    """Represents the spec for the knowledge block in a callable."""
    query: str
    full_text: bool = False

@dataclasses.dataclass
class KnowledgeConfig:
    """Represents the config for the knowledge block in a callable."""
    knowledge: list[DataSource] = None
    top_k: int = 8
    filter: dict = defaultdict
    use_cache: bool = False

@dataclasses.dataclass
class ModelSpec:
    """Represents the spec for the model block in a callable."""
    temperature: float = 0.7
    max_tokens: int = 1024
    few_shot_count: int = 3
    few_shot_prompt: str = ""
    few_shot_preprompt: str = ""
    prompt: str = ""
    stop: list[str] = None

@dataclasses.dataclass
class ModelConfig:
    """Represents the config for the model block in a callable."""
    provider_id: str = "openai"
    model_id: str = "gpt-3.5-turbo"
    use_cache: bool = True
    use_semantic_cache: bool = False

@dataclasses.dataclass
class CurlSpec:
    """Represents the spec for the curl block in a callable."""
    scheme: str = "HTTPS"
    method: str = "POST"
    url: str = ""
    headers_code: str = '_fun = (env) => {\n  return {"Content-Type": "application/json"};\n}'
    body_code: str = '_fun = (env) => {\n  // return a string or null to skip sending a body.\n  return JSON.stringify({ foo: "bar" });\n}'

@dataclasses.dataclass
class CurlConfig:
    """Represents the config for the curl block in a callable."""
    use_cache: bool = True

@dataclasses.dataclass
class BrowserSpec:
    """Represents the spec for the browser block in a callable."""
    url: str = ""
    selector: str = "body"
    timeout: int = 16000
    wait_until: str = "networkidle2"

@dataclasses.dataclass
class BrowserConfig:
    """Represents the config for the browser block in a callable."""
    provider_id: str = ""
    use_cache: bool = True
    error_as_output: bool = True

@dataclasses.dataclass
class SearchSpec:
    """Represents the spec for the search block in a callable."""
    query: str = ""
    num: int = 3

@dataclasses.dataclass
class SearchConfig:
    """Represents the config for the search block in a callable."""
    provider_id: str = "serpapi"
    use_cache: bool = True

@dataclasses.dataclass
class LoopSpec:
    """Represents the spec for the loop block in a callable."""
    condition_code: str = '_fun = (env) => {\n  // return true to continue the loop, return false to exit loop;\n}'
    max_iterations: int = 8

@dataclasses.dataclass
class MapSpec:
    """Represents the spec for the map block in a callable."""
    from_: str = "INPUT"
    repeat: Optional[str] = None

@dataclasses.dataclass
class InputConfig:
    """Represents the spec for the input block in a callable."""
    dataset: str

Spec = Union[CodeSpec, KnowledgeSpec, ModelSpec, CurlSpec, BrowserSpec, SearchSpec, LoopSpec, MapSpec, dict]

Config = Union[KnowledgeConfig, ModelConfig, CurlConfig, BrowserConfig, SearchConfig, InputConfig, dict]

@dataclasses.dataclass
class Block:
    """Represents a block in a callable."""
    type: str
    name: str
    indent: int
    spec: Spec = defaultdict
    config: Config = defaultdict

def toString(block: Block):
    blockdict = dataclasses.asdict(block)
    return json.dumps(blockdict)

@dataclasses.dataclass
class OutputBlock(utils.DataClassYamlMixin):
    """Represents an output block in a callable."""
    type: str = "output"
    name: str = "OUTPUT"
    indent: int = 0
    spec: dict = defaultdict