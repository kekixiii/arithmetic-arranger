def arithmetic_arranger(*args):
    problem_list = args[0]
    if len(args) > 1:
        show_answer = args[1]
    # check for too many problems
    if len(problem_list) > 5:
        return "Error: Too many problems."
    
    # split problems into a list of different parts and put them in a list of dictionaries
    problem_dict_list = []
    for problem in problem_list:
        operator = problem.split(" ")[1].strip()
        first_num = problem.split(" ")[0].strip()
        second_num = problem.split(" ")[2].strip()
        problem_dict = {"first_num": first_num, "second_num": second_num, "operator": operator}
        problem_dict_list.append(problem_dict)
    
    #check operator
    for problem in problem_dict_list:
        if problem["operator"] != "+" and problem["operator"] != "-":
            return "Error: Operator must be '+' or '-'."

    #check only digits
    for problem in problem_dict_list:
        if not problem["first_num"].isdigit() or not problem["second_num"].isdigit():
            return "Error: Numbers must only contain digits."
    
    #check number of digits in problems
    for problem in problem_dict_list:
        if len(problem["first_num"]) > 4 or len(problem["second_num"]) > 4:
            return "Error: Numbers cannot be more than four digits."
    
    #get total length required for the problem
    for problem in problem_dict_list:
        problem_length = max(len(problem["first_num"]),len(problem["second_num"]))
        total_length = problem_length + 2
        problem["total_length"] = total_length
    
    #construct the lines for text to return
    
    first_line = ""
    second_line = ""
    third_line = ""
    i = 0
    while i < len(problem_dict_list):
        first_str = " " * (problem_dict_list[i]["total_length"] - len(problem_dict_list[i]["first_num"])) + problem_dict_list[i]["first_num"]
        second_str = problem_dict_list[i]["operator"] + " " * (problem_dict_list[i]["total_length"] - len(problem_dict_list[i]["second_num"]) - 1) + problem_dict_list[i]["second_num"]
        third_str = "-" * problem_dict_list[i]["total_length"]
        i+= 1
        if i < len(problem_dict_list):
            first_str = first_str + "    "
            second_str = second_str + "    "
            third_str = third_str + "    "
        first_line = first_line + first_str
        second_line = second_line + second_str
        third_line = third_line + third_str

    combined_string = first_line + "\n" + second_line + "\n" + third_line

    #if show answer is true
    if  len(args) > 1 and show_answer:
        fourth_line = ""
        answer_str = ""
        #calculate the answers
        for problem in problem_dict_list:
            if problem["operator"] == "+":
                answer = int(problem["first_num"]) + int(problem["second_num"])
            else:
                answer = int(problem["first_num"]) - int(problem["second_num"])
            problem["answer"] = str(answer)
        i = 0
        while i < len(problem_dict_list):
            answer_str = " " * (problem_dict_list[i]["total_length"] - len(str(problem_dict_list[i]["answer"]))) + str(problem_dict_list[i]["answer"])
            i += 1
            if i < len(problem_dict_list):
                answer_str += "    "
            fourth_line = fourth_line + answer_str
        combined_string = combined_string + "\n" + fourth_line

    return combined_string
