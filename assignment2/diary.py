import traceback

try:
    with open('diary.txt', 'a') as file:
        prompt = "What happened today?" 
        while True:
           entry = input(prompt).strip().lower()

           if entry == "done for now":
                file.write(entry + "\n") 
                break
           
           file.write(entry + "\n") 
           prompt = "What else? "

except Exception as e:
   trace_back = traceback.extract_tb(e.__traceback__)
   stack_trace = [f'File: {trace[0]}, Line: {trace[1]}, Func: {trace[2]}, Message: {trace[3]}' for trace in trace_back]
    
   print(f"Exception type: {type(e).__name__}")
   message = str(e)
   if message:
        print(f"Exception message: {message}")
   print(f"Stack trace: {stack_trace}")
