from importlib.metadata import version, PackageNotFoundError

try:
    __version__ = version("test_api_5")
except PackageNotFoundError:
    # package is not installed
    pass