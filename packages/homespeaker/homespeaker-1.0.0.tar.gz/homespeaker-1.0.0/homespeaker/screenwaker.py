"""Wake the screen up code."""
import os
import subprocess


def wake_the_screen():
    """Wake the screen."""
    display_type = os.environ.get("XDG_SESSION_TYPE")
    if display_type == "wayland":
        subprocess.run([
            "dbus-send", "--session", "--dest=org.gnome.ScreenSaver",
            "--type=method_call", "/org/gnome/ScreenSaver",
            "org.gnome.ScreenSaver.SetActive", "boolean:false"
        ], shell=True, check=True)
    elif display_type == "x11":
        subprocess.run([
            "xset",
            "-display",
            os.environ.get("DISPLAY"),
            "s",
            "reset"
        ], shell=True, check=True)
    else:
        raise EnvironmentError(f"Unsupported display server {display_type}!")
