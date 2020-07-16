from injector import Injector

from sheetgo.app_module import AppModule

MODULES = [AppModule]


def create_injector(modules):
    """
    Creates the injector and install in the modules
    :param modules: The optional modules to load instead of the entry point
    :return: Returns the injector
    """
    assert modules

    injector = Injector()
    for module in modules:
        injector.binder.install(module)

    return injector
