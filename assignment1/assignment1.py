# Write your code here.
# Task 1
def hello():
    return "Hello!"
print(hello())

# Task 2
def greet(name):
    return (f"Hello, {name}!")
print(greet("John"))

# Task 3
def calc(a, b, operation="multiply"):
    try:
        match operation:
            case "add":
                return a + b
            case "subtract":
                return a - b
            case "multiply":
                return a * b
            case "divide":
                return a / b 
            case "modulo":
                return a % b 
            case "expon":
                return a ** b
            case "int_divide":
                return a // b 
            case _:
                return "Invalid operation!"
    except ZeroDivisionError:
        return "You can't divide by 0!"
    except TypeError:
        return "You can't multiply those values!"

print(calc( 5,2))
print(calc( 5,2, "add"))
print(calc( 5, 0,"divide"))
print(calc(5,"2", "multiply"))  
print(calc(5, 2, "subtract"))   
print(calc(5 ,2, "modulo"))       
            
#Task4
def data_type_conversion(value, data_type):
    try:
        if data_type == "int":
            return int(value)
        elif data_type == "float":
            return float(value)
        elif data_type == "str":
            return str(value)
        else:
            return f"Invalid target type: {data_type}"
    except ValueError:
        return f"You can't convert {value} into a {data_type}."
print(data_type_conversion("123", "int"))  
print(data_type_conversion("123.45", "float"))  
print(data_type_conversion(456, "str")) 
print(data_type_conversion("nonsense", "float"))  

#Task5
def grade(*args):
    try:
        if not args:
            return "invalid data was provided."
        
        avg = sum(args) / len(args)

        if avg >= 90:
            return "A"
        elif avg >= 80:
            return "B"
        elif avg >= 70:
            return "C"
        elif avg >= 60:
            return "D"
        else:
            return "F"
    except (TypeError, ValueError):
        return "Invalid data was provided."    
 
print(grade(90, 85, 92))    
print(grade(70, 75, 78))    
print(grade(50, 40, 55))     
print(grade("nonsense", 85)) 
print(grade())  

#Task6
def repeat(string, count):
    result = ""
    for _ in range(count):
        result += string
    return result

print(repeat("acdc", 3))    
print(repeat("hey", 5))
print(repeat("o", 0))
print(repeat(" ", 4))
print(repeat("Holly!Holly!", 2))

#Task7
def student_scores(mode, **kwargs):
    if mode == "best":
        best_student = max(kwargs, key=kwargs.get)
        return best_student
    
    elif mode == "mean":
        if kwargs:
            average_score = sum(kwargs.values()) / len(kwargs)
            return average_score
        else:
            return "No scores provided."
        
    else:
        return "Invalid mode. Use 'best' or 'mean'."  

print(student_scores("best", Manny=95, Joe=88, Dan=92))  #
print(student_scores("mean", Manny=95, Joe=88, Dan=92))  
print(student_scores("mean")) 
print(student_scores("wrong", Manny=95, Joe=88))      
    
#Task8
def titleize( text ):
    little_words = {"a", "on", "an", "the", "of", "and", "is", "in"}
    words = text.split()

    for i, word in enumerate(words):
        if i == 0 or i == len(words) -1 or word.lower() not  in little_words:
            words[i] = word.capitalize()
        else:
            words[i] = word.lower()

    return " ".join(words)

print(titleize("the long way in dunes"))
print(titleize("while you were sleeping"))
print(titleize("pirates of the carribean: the curse of the black pearl"))        

#Task9
def hangman(secret, guess):
    return "".join(letter if letter in guess else "_" for letter in secret)

print(hangman("customer", "cm"))  
print(hangman("basement", "bnt"))  
print(hangman("mississippi", "sip"))  
print(hangman("crayon", "aeiou"))  
print(hangman("giraffe", "gleft"))

#Task10
def pig_latin(sentence):
    vowels = "aeiou"
    words = sentence.split()
    pig_latin_words = []

    for word in words:
        if word[:2] == "qu":  
            pig_latin_words.append(word[2:] + "quay")
        else:
            for i, letter in enumerate(word):
                if letter in vowels:
                    if word[i - 1: i + 1] == "qu":
                        pig_latin_words.append(word[i + 1:] + word[:i + 1] + "ay")
                    else:
                        pig_latin_words.append(word[i:] + word[:i] + "ay")
                    break 
    return " ".join(pig_latin_words)

print(pig_latin("apple"))            
print(pig_latin("banana"))           
print(pig_latin("quick brown fox"))  
print(pig_latin("square"))           
