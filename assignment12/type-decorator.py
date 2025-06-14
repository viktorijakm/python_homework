# decorator that takes an argument
def type_converter(type_of_output):
    def actual_decorator(func):
        def wrapper(*args, **kwargs):
            x = func(*args, **kwargs)  # Call the function
            return type_of_output(x)   # Convertion to the specified type
        return wrapper
    return actual_decorator

# Function that returns an integer, decorated to convert result to a string
@type_converter(str)
def return_int():
    return 5

# Function that returns a string, decorated to convert result to an integer
@type_converter(int)
def return_string():
    return "not a number"

# Mainline code to test behavior
if __name__ == "__main__":
    y = return_int()
    print(type(y).__name__)  # Expected output: "str"

    try:
        y = return_string()  # This will raise an error
        print("shouldn't get here!")
    except ValueError:
        print("can't convert that string to an integer!")  # Expected error message
