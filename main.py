def arithmetic_arranger(problems, show_answers=False):
    problems_list = list(map(lambda x: x.split(), problems))
    #print(problems_list)
    
    #error handling
    if len(problems)>5:
        return'Error: Too many problems.'
    
    for problem in problems_list:
        if problem[1] == '/' or problem[1] == '*':
            return "Error: Operator must be '+' or '-'."
        popped_operator = problem[1]
        problem.pop(1)
        if not all(map(lambda x: x.isdigit(), problem)):
            return 'Error: Numbers must only contain digits.'
        if not all(map(lambda x: len(x)<5,problem)):
            return 'Error: Numbers cannot be more than four digits.'
        problem.insert(1,popped_operator)
    #string building
    # There should be a single space between the operator and the longest of the two operands, the operator will be on the same line as the second operand, both operands will be in the same order as provided (the first will be the top one and the second will be the bottom).
    # Numbers should be right-aligned.
    # There should be four spaces between each problem.
    # There should be dashes at the bottom of each problem. The dashes should run along the entire length of each problem individually. (The example above shows what this should look like.)
    
    #splitting it into a top line output and bottom lineout put will probably be easiest as we can use .join and /n
    
    top_line=''
    bottom_line =''
    dashes = ''
    solutions =''
    output=''
    output_list = []
    print(problems_list)
    for first_num in problems_list:
        temp_output=''
        max_length=max(map(lambda x:len(x),first_num))
        spacing = max_length+1
        expression = ''.join(first_num)
        answer =  eval(expression)
        counter=0
        
        for item in first_num:
            if counter == 0:
                temp_output+= ' '*(spacing-len(item))
                temp_output+=item
                temp_output+='\n'
            elif counter==1:
                temp_output+=item
            else:
                temp_output+=' '*(spacing-len(item))
                temp_output+=item
                temp_output+='\n'
                temp_output+='_'*spacing
            counter+=1
        output_list.append(temp_output)
    for output  in output_list:
        output.join(output)
        
    print(output_list)
    print(output)
            
     
    return problems



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])}')