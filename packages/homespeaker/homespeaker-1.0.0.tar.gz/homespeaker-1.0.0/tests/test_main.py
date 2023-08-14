"""Test main module."""
import pathlib
import pytest
from mockito import expect
from fastapi.testclient import TestClient
from homespeaker import main as sut

pytestmark = pytest.mark.usefixtures("unstub")  # pylint: disable=unused-argument


def test_load_configuration_with_home_ev(tmp_path: pathlib.Path):
    """Test the load_configuration function with a HOME environment variable."""
    config_dir = tmp_path / ".config" / "homespeaker/"
    config_dir.mkdir(parents=True)
    config_file_path = config_dir / "config.yaml"
    with open(
        config_file_path, "w", encoding="utf8"
    ) as f:  # pylint:disable=invalid-name
        f.write(
            (
                "---\n"
                "- cron:\n"
                "    schedule: 20 21 * * *\n"
                "    actions:\n"
                "      - light-screen:\n"
                "          duration: 8\n"
                "- cron:\n"
                "    schedule: 20 21 * * *\n"
                "    actions:\n"
                "      - play-sound:\n"
                "          src: alarm.mp3\n"
            )
        )
    expect(sut.os.environ).get("XDG_CONFIG_HOME").thenReturn(None)
    expect(sut.os.environ).get("HOME").thenReturn(tmp_path)
    result = sut.load_configuration()
    assert result == [
        {
            "cron": {
                "schedule": "20 21 * * *",
                "actions": [{"light-screen": {"duration": 8}}],
            }
        },
        {
            "cron": {
                "schedule": "20 21 * * *",
                "actions": [{"play-sound": {"src": "alarm.mp3"}}],
            }
        },
    ]


def test_load_configuration_with_xdg_home(tmp_path: pathlib.Path):
    """Test the load_configuration function with XDG_CONFIG_HOME environment variable."""
    config_dir = tmp_path / "homespeaker/"
    config_dir.mkdir(parents=True)
    config_file_path = config_dir / "config.yaml"
    with open(
        config_file_path, "w", encoding="utf8"
    ) as f:  # pylint:disable=invalid-name
        f.write(
            (
                "---\n"
                "- cron:\n"
                "    schedule: 20 21 * * *\n"
                "    actions:\n"
                "      - light-screen:\n"
                "          duration: 8\n"
                "- cron:\n"
                "    schedule: 20 21 * * *\n"
                "    actions:\n"
                "      - play-sound:\n"
                "          src: alarm.mp3\n"
            )
        )
    expect(sut.os.environ, times=2).get("XDG_CONFIG_HOME").thenReturn(tmp_path)
    result = sut.load_configuration()
    assert result == [
        {
            "cron": {
                "schedule": "20 21 * * *",
                "actions": [{"light-screen": {"duration": 8}}],
            }
        },
        {
            "cron": {
                "schedule": "20 21 * * *",
                "actions": [{"play-sound": {"src": "alarm.mp3"}}],
            }
        },
    ]


client = TestClient(sut.app)

def configuration():
    """Build a configuration."""
    return {"song1": "/some/path/some.where"}

@pytest.fixture
def override_config():
    """Override the configuration."""
    sut.app.dependency_overrides[sut.load_configuration] = configuration
    yield
    sut.app.dependency_overrides = {}


def test_playaudio(override_config):  # pylint: disable=redefined-outer-name, unused-argument
    """Test the playaudio function."""
    expect(sut).playsound("/some/path/some.where")
    response = client.get("/playaudio/song1")
    assert response.status_code == 200
    assert not response.json()

def test_wakescreen():
    """Test the wakescreen function."""
    expect(sut).wake_the_screen()
    response = client.get("/wakescreen")
    assert response.status_code == 200
    assert not response.json()

def test_homespeaker_entrypoint():
    """Test the homespeaker entrypoint."""
    expect(sut.uvicorn).run(sut.app, host="0.0.0.0", port=8000)
    sut.homespeaker_entrypoint()
