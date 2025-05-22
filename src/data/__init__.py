from .filecache import FileCache

_cache = FileCache()


def get_cache() -> FileCache:
    """Get the global cache instance."""
    return _cache
