from pluggy import HookspecMarker

hookspec = HookspecMarker("plugin_name")

@hookspec
def some_hook(arg1, arg2):
    """This hook allows other plugins to do something with these arguments."""

@hookspec
def another_hook(data):
    """Another hook for different functionality."""
