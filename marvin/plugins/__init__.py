from .base import BaseHandler
import importlib
import importlib.util
import pkgutil
import inspect


def all_handlers():
    classes = []
    for importer, module_name, _ in pkgutil.iter_modules(__path__):
        plugin_module = importlib.import_module('.' + module_name, __name__)
        for name, cls in inspect.getmembers(plugin_module, inspect.isclass):
            if issubclass(cls, BaseHandler) and cls != BaseHandler:
                classes.append(cls)
    return classes

__all__ = all_handlers()
