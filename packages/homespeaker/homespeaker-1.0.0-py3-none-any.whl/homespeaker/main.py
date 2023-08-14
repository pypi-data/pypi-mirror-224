"""Do the thing."""
import os
from typing import Dict, Any
from typing_extensions import Annotated
import yaml
import uvicorn
from playsound import playsound
from fastapi import FastAPI, Depends
from homespeaker.screenwaker import wake_the_screen

app = FastAPI()


def load_configuration() -> Dict[str, Any]:
    """Load the configuration file if it exists."""
    if os.environ.get("XDG_CONFIG_HOME"):
        config_path = os.path.join(
            os.environ.get("XDG_CONFIG_HOME"), "homespeaker", "config.yaml"
        )
    else:
        config_path = os.path.join(
            os.environ.get("HOME"), ".config", "homespeaker", "config.yaml"
        )
    with open(config_path, "r", encoding="utf8") as f:  # pylint: disable=invalid-name
        return yaml.safe_load(f)


@app.get("/playaudio/{key}")
def playaudio(key: str, config: Annotated[dict, Depends(load_configuration)]):
    """Play audio of some type."""
    playsound(config[key])
    return {}


@app.get("/wakescreen")
def wakescreen():
    """Wake the screen for the specified amount of time."""
    wake_the_screen()
    return {}

def homespeaker_entrypoint():
    """Launch the homespeaker server."""
    uvicorn.run(app, host="0.0.0.0", port=8000)
