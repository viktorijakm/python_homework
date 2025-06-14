import logging
from functools import wraps

logger = logging.getLogger(__name__ + "_parameter_log")
logger.setLevel(logging.INFO)
logger.addHandler(logging.FileHandler("./decorator.log", "a"))

def logger_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        pos_args = args if args else "none"
        kw_args = kwargs if kwargs else "none"
        result = func(*args, **kwargs)
        logger.info(f"function: {func.__name__} | "
                    f"positional parameters: {pos_args} | "
                    f"keyword parameters: {kw_args} | "
                    f"return: {result}")
        return result
    return wrapper

# Function 1: No params
@logger_decorator
def hello():
    print("Hello, World!")

# Function 2: Variable positional args
@logger_decorator
def many_args(*args):
    return True

# Function 3: Variable keyword args
@logger_decorator
def keyword_only(**kwargs):
    return logger_decorator

if __name__ == "__main__":
    hello()
    many_args(1, 2, 3)
    keyword_only(name="Vi", age=99)