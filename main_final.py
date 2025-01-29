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
    
    for problem in problems:
        answer = eval(problem)
        first_num = problem.split(' ')[0]
        operator = problem.split(' ')[1]
        second_num = problem.split(' ')[2]
        max_length = max(len(first_num),len(second_num))+2
        top = first_num.rjust(max_length)
        bot = operator+second_num.rjust(max_length-1)
        dash = '-'*max_length
        solution=str(answer).rjust(max_length)
        if problem ==problems[-1]:
            top_line+=(top)
            bottom_line+=(bot)
            dashes +=(dash)
            solutions +=(solution)
            break
        top_line+=(top+'    ')
        bottom_line+=(bot+'    ')
        dashes +=(dash+'    ')
        solutions +=(solution+'    ')
    output+=top_line
    output+='\n'+bottom_line
    output+='\n'+dashes
    if show_answers:
        output+='\n'+solutions
    return output



print(f'\n{arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"],True)}')
