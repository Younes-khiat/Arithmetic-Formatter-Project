def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5:
        raise ValueError("Error: Too many problems.")
    
    operations = []
    for problem in problems:
        ppp = problem.split(" ")
        if ppp[1] != "+" and ppp[1] != "-":
            return ("Error: Operator must be '+' or '-'.")
        if not ppp[0].isnumeric() or not ppp[2].isnumeric():
            return ('Error: Numbers must only contain digits.')
        if int(ppp[0]) > 9999 or int(ppp[2]) > 9999:
            return ('Error: Numbers cannot be more than four digits.')
        if ppp[1] == "+":
            result = str(int(ppp[0]) + int(ppp[2]))
        elif ppp[1] == "-":
            result = str(int(ppp[0]) - int(ppp[2]))
        lent = (len(ppp[2]) - len(ppp[0]))
        lentt = max(len(ppp[0]), len(ppp[2]))
        if lent>0:
            ppp[0] = " "*abs(lent) + ppp[0]
        else:
            ppp[2] = " "*abs(lent) + ppp[2]   
        if len(result) < lentt:
            result = " "*abs(len(result) - lentt) + result
        if len(result) > lentt:
                result = " " +result
        elif len(result) < lentt:
            result = "   " + result 
        else:
            result = "  " + result    
        pp = {'major': "  " +ppp[0] + "    ",
              'minor': ppp[1] + " " + ppp[2] + "    ",
              'maximum': lentt,
              'result': result + "    "
        }  
        operations.append(pp)
    solution = ""
    for operation in operations:
        # print(operation["major"], end="")
        solution += operation["major"]
    # print("")    
    solution += "\n"
    for operation in operations:
        # print(operation["minor"], end="")
        solution += operation["minor"]
    # print("")
    solution += "\n"
    for operation in operations:
        # print("--" + "-"*operation["maximum"] ,end="    ")
        solution += "--" + "-"*operation["maximum"] + "    "
    # print("")
    solution += "\n"
    if show_answers == True:  
        for operation in operations:
            # print(operation["result"], end="")
            solution += operation["result"]
        solution+= "\n"  
    return solution
rigl = ["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"]
go = arithmetic_arranger (rigl, True)
print("") 
print(go)
