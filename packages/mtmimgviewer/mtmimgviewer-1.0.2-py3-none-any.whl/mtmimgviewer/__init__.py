from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("mtmimgviewer")
except PackageNotFoundError:
    __version__ = "unknown version"