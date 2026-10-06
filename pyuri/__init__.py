"""Python URI Handling"""

try:
    from importlib.metadata import PackageNotFoundError, version
except ImportError:  # Python 2.7 and 3.6
    from pkg_resources import DistributionNotFound as PackageNotFoundError
    from pkg_resources import get_distribution

    def version(name):
        return get_distribution(name).version

from .uri import URI

__all__ = ['URI']

try:
    __version__ = version(__name__)
except PackageNotFoundError:
    __version__ = '0.0.0-dev'
