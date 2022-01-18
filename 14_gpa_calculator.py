#defining a function with if, elif and else statement

def grade_calculator(marks):
    if marks==50:
        print("The student is failed")
    elif marks>60:
        print("Grade-C")
    else :
        print("Excellent marks")
    grade_calculator()