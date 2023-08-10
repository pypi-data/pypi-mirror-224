#!/usr/bin/env python
# -*- coding: utf-8 *-*


""" ~*~ Docstring ~*~
      PyQuickTest is an experimental python testing
             framework designed to deliver an
    easy-and-quick-to-start python testing mechanism.
        decorators.py is the file containing every
            decorators, useful for the tests.
                                    ~*~ Docstring ~*~

    ~*~ CHANGELOG ~*~
     ____________________________________________________________________________________
    | VERSION |    DATE    |                           CONTENT                           |
    |====================================================================================|
    |         |            | Initial release, including the following features:          |
    |         |            |     -Decorators for test functions.                         |
    |         |            |     -Assertions functions for test functions.               |
    |         |            |     -Testing routine functions for:                         |
    |  0.0.1  | 2023/08/06 |         *A single function.                                 |
    |         |            |         *A given group/subgroup of functions.               |
    |         |            |         *All functions from a given file.                   |
    |         |            |     -Generators functions for random inputs.                |
    |         |            |     -a CLI tool for running tests.                          |
    |------------------------------------------------------------------------------------|
    |         |            | Adding a smart assertion error printing to avoid useless    |
    |  0.1.0  | 2023/08/06 | lines, and a more detailed test session start message that  |
    |         |            | includes informations about the OS & the software versions. |
     ‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾‾
                                                                         ~*~ CHANGELOG ~*~ """


#=--------------=#
# Import section #
#=--------------=#

from   __future__           import annotations
import typing
import threading
import queue
import inspect
import re
from pyquicktest.utils      import map1, get_str_tab
from pyquicktest.assertions import TestTimeoutException

# =-------------------------------------------------= #


#=------------------=#
# Authorship section #
#=------------------=#

__filename__     = "decorators.py"

# =--------------------------------------------------------= #


#=------------------------------------=#
# Constants & Global variables section #
#=------------------------------------=#

NL     = '\n'
DQUOTE = '"'

# =----------------------------------= #


# ===================================================== #
# General purpose decorators required functions section #
# ===================================================== #

def copy_function_attributes(src_func: typing.Callable, dest_func: typing.Callable) -> typing.Callable:
    """Copy every safe-copy attributes from one function to another, and return the destination function."""
    setattr(dest_func, "__annotations__", {"return": getattr(src_func, "__annotations__").get("return", typing.Any)})
    for attr in dir(src_func):
        if attr not in [
            "__annotations__", "__builtins__", "__call__", "__class__", "__closure__", "__code__", "__defaults__", "__delattr__", "__dir__", "__eq__",
            "__format__", "__ge__", "__get__", "__getattribute__", "__globals__", "__gt__", "__hash__", "__init__", "__init_subclass__", "__kwdefaults__",
            "__le__", "__lt__", "__ne__", "__new__", "__reduce__", "__reduce_ex__", "__repr__", "__setattr__", "__sizeof__", "__str__", "__subclasshook__"
        ]:
            setattr(dest_func, attr, getattr(src_func, attr))
    return dest_func

def return_or_raise(value: typing.Any) -> typing.Any:
    """Return or raise the given value <value> if it is an Exception."""
    if type(value) == Exception:
        raise value
    return value

# =----------------------------------------------------------------------------------------------------------------------------------------------------= #


# ================================== #
# General purpose decorators section #
# ================================== #

def add_flag(flag: str) -> typing.Callable:
    """Add a given attribute name with a <None> value to the decorated function."""
    def decorator(func: typing.Callable) -> typing.Callable:
        setattr(func, flag, None)
        return func
    return decorator
# Marking the decorator itself as tested.
add_flag.tested = None

@add_flag("tested")
def add_attribute(attribute: str, value: typing.Any = None) -> typing.Callable:
    """Add a given attribute name and value [default: None] to the decorated function."""
    def decorator(func: typing.Callable) -> typing.Callable:
        setattr(func, attribute, value)
        return func
    return decorator

@add_flag("tested")
def add_flags(*flags: str) -> typing.Callable:
    """Add a given attribute name with a <None> value to the decorated function."""
    def decorator(func: typing.Callable) -> typing.Callable:
        for flag in flags:
            setattr(func, flag, None)
        return func
    return decorator

@add_flag("tested")
def add_attributes(*attributes_and_values: typing.Union[str, typing.Tuple[str, typing.Any]]) -> typing.Callable:
    """Add a given list of attribute name and value to the decorated function."""
    def decorator(func: typing.Callable) -> typing.Callable:
        try:
            if type(attributes_and_values[0]) == tuple:
                for attribute_and_value in attributes_and_values:
                    (attribute, value) = attribute_and_value
                    setattr(func, attribute, value)
            else:
                for i in range(0, int(len(attributes_and_values)+1/2), 2):
                    (attribute, value) = attributes_and_values[i], attributes_and_values[i+1]
                    setattr(func, attribute, value)
        except IndexError:
            pass
        return func
    return decorator

def alias(*aliases: str) -> typing.Callable:
    """Create aliases for the decorated object.
       This might cause your IDE to generate warning on undefined functons because decoratord are applied when interprated,
       that's why this utils file use explicit aliasing instead of elegant use of this decorator."""
    def decorator(func: typing.Callable) -> typing.Callable:
        map1(lambda x: globals().update({x: func}), aliases)
        return func
    return decorator

def timeout(duration: float, default: typing.Any) -> typing.Callable:
    """Add a timeout to the decorated object."""

    # Creating the decorator function.
    def decorator(func: typing.Callable) -> typing.Callable:
        # Creating a queue object for storing the potentially returned value from the given <func> function.
        queue_ = queue.Queue(maxsize=1)

        # Creating a temporary function that simply put the result of the <func> function
        # to the previously created queue whatever its result is (even Exceptions).
        def target():
            try:
                queue_.put(func())
            except Exception as e:
                queue_.put(e)
        
        # Creating the modified function that use a Thread to run in background the <func> function.
        # After a given amount of time, the function result is ignored, and the default value is returned.
        def timeout_func():
            action = threading.Thread(target=target, daemon=True)
            action.start()
            action.join(timeout=duration)
            if action.is_alive():
                return_or_raise(default)
            return_or_raise(queue_.get())

        # Copy the <func> function attributes to the newly created <timeout_func> function.
        return copy_function_attributes(func, timeout_func)
    return decorator

# =---------------------------------------------------------------------------------------------------------------------= #


#=------------------------=#
# Tests decorators section #
#=------------------------=#

def is_test() -> typing.Callable:
    """Mark a function as a test."""
    def decorator(func: typing.Callable) -> typing.Callable:
        func.test = None
        if not hasattr(func, "__source__"):
            func.__source__           = inspect.getsource(func)
            func.__rewritten_source__ = func.__source__
        return func
    return decorator

def pqt_group(*groups: str) -> typing.Callable:
    """Mark a function as belonging to a given test group."""
    def decorator(func: typing.Callable) -> typing.Callable:
        func.test_group = list(groups)
        if not hasattr(func, "__source__"):
            func.__source__           = inspect.getsource(func)
            func.__rewritten_source__ = func.__source__
        return func
    return decorator

def pqt_execnbr(exec_nbr: int) -> typing.Callable:
    """Mark a function as requiring <exec_nbr> execution during tests."""
    def decorator(func: typing.Callable) -> typing.Callable:
        func.test_execution_number = exec_nbr
        if not hasattr(func, "__source__"):
            func.__source__           = inspect.getsource(func)
            func.__rewritten_source__ = func.__source__
        return func
    return decorator

def pqt_parametrize(*args: typing.Any) -> typing.Callable:
    """Fill a functions parameters with the given arguments."""
    def decorator(func: typing.Callable) -> typing.Callable:

        # Retrieving the source code of the given function
        source = inspect.getsource(func)

        # Retrieving its prefixed tabulation
        tab = get_str_tab(source)

        # Creating the output function source code
        res_source  = f"{tab}def {func.__name__}() -> typing.Union[TestPassedException, TestFailedException]:\n"
        if func.__doc__:
            res_source += f"""{tab}    \"\"\"{func.__doc__}\"\"\"\n"""
            res_source += "\n".join(f"""{tab}    {arg[0]} = {arg[1]}\n""" for arg in zip(inspect.getfullargspec(func).args, args))
            res_source += '\n'.join(source.split(func.__doc__)[1].split('\n')[1:])
        else:
            
            res_source += "\n".join(f"""{tab}    {arg[0]} = {arg[1]}\n""" for arg in zip(inspect.getfullargspec(func).args, args))
            res_source += (':'.join(source.split(re.findall(r"(def " + func.__name__ + r"\s?\(.*\))", source)[0])[1].split(':')[1:]))
            pass

        func.__source__           = source
        func.__rewritten_source__ = res_source
        return func
    return decorator

def pqt_timeout(duration: float) -> typing.Callable:
    """Add a timeout to the decorated tests after what the test fail."""
    return timeout(duration=duration, default=TestTimeoutException(f"Timeout after {duration} seconds."))

# =-------------------------------------------------------= #