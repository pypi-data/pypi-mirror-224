# homespeaker
Code to turn a laptop into a home speaker.

## Functionality

Currently only supports scheduling "waking the screen" and "playing an alarm."

## Installation

pip install homespeaker

## Configuration

Install a config file like below in `$XDG_CONFIG_HOME/homespeaker/config.yaml` or `$HOME/.config/homespeaker/config.yaml`:

```yaml
# Example Configuration
---
alarm: /opt/alarm.mp3
```

## Calling

### Wake the screen

```bash
curl http://localhost:8000/wakescreen
```

### Play audio

`alarm` is the key from the config file.

```bash
curl http://localhost:8000/playaudio/alarm
```
