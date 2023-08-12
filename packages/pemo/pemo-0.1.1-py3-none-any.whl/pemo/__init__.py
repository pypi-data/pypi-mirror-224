from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("pemo")
except PackageNotFoundError:
    __version__ = "unknown version"