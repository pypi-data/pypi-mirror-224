"""Test the screenwaker module."""
import pytest
from mockito import expect
from homespeaker import screenwaker as sut

pytestmark = pytest.mark.usefixtures("unstub")  # pylint: disable=unused-argument

def test_wake_the_screen_x11():
    """Test the wake_the_screen function on x11."""
    with expect(sut.os.environ).get("XDG_SESSION_TYPE").thenReturn("x11"):
        with expect(sut.os.environ).get("DISPLAY").thenReturn(":0"):
            with expect(sut.subprocess).run(
                ["xset", "-display", ":0", "s", "reset"], shell=True, check=True
            ):
                sut.wake_the_screen()


def test_wake_screen_wayland():
    """Test the wake_the_screen function on wayland."""
    with expect(sut.os.environ).get("XDG_SESSION_TYPE").thenReturn("wayland"):
        with expect(sut.subprocess).run(
            [
                "dbus-send",
                "--session",
                "--dest=org.gnome.ScreenSaver",
                "--type=method_call",
                "/org/gnome/ScreenSaver",
                "org.gnome.ScreenSaver.SetActive",
                "boolean:false",
            ],
            shell=True,
            check=True,
        ):
            sut.wake_the_screen()

def test_wake_screen_other():
    """Test the wake_the_screen function on other."""
    with pytest.raises(EnvironmentError, match="Unsupported display server custom."):
        with expect(sut.os.environ).get("XDG_SESSION_TYPE").thenReturn("custom"):
            sut.wake_the_screen()
