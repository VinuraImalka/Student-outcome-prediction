# I declare that my work contains no examples of misconduct, such as plagiarism, or collusion. 
# Any code taken from other sources is referenced within my code solution.
# Student ID:20222258
# Date: 2023.11.29

# importing all the modules from the graphics library
from graphics import *

# initializing global variables
progression_results = []
count_list = [0,0,0,0]

def print_doted_line():
    """Display a line for better visual separation in the console."""
    print("+" + "-" * 100 + "+")

def response_validation():
    """Validates user response for continuing or quitting the program.
    Returns:
        response(str): 'y' for yes, 'q' for quit.
    """
    # Initializing local variables needed for the function
    response_list = ('y','q')
    
    # Geting user input for response as 'y'or'q'
    response = input("Would you like to enter another set of data?\nEnter 'y' for yes or 'q' to quit and view results:").lower()
    if response in response_list:
        return response 
    else:
        print_doted_line()
        print("Invaild response!,Please enter'y'or'q'.")
        print_doted_line()
        # If user-response not in the response_list,recursively call the response_validation function and return the value.
        return response_validation()

def user_validation():
    """Validates the user who is using the program as a 'staff'or'student'
    Returns:
        user(str): 'staff' or 'student'
    """
    # Initializing local variables needed for the function
    user_list = ('staff','student')
    
    # Geting user input for response as 'staff'or'student'
    user = input("Are you a staff member or are you a student,please enter 'staff' or 'student':").lower()
    if user in user_list:
        return user
    else:
        print_doted_line()
        print("Invaild response!,Please enter'staff'or'student'")
        print_doted_line()
        # If user-response not in the user_list,recursively call the response_validation function and return the value.
        return user_validation() 
        
def get_credit_input():
    """Get input values form user for pass credit,defer credit and fail credit.
    Returns:
        credit_input_list(list): List containing three integers for each entry,
        representing pass credit,defer credit and fail credit respectively.
    """
    # Initializing local variables needed for the function
    credit_types = ('pass','defer','fail')
    credit_input_list = [0,0,0]
    repeat = True
    
    # Looping through the list to get each credit(pass credit,defer credit and fail credit).
    for credit_type in range (len(credit_types)):
        while repeat:
            try:
                credit_input=int(input(f"Enter credits at {credit_types[credit_type]}:"))
                # Validating entered credit.
                if credit_input not in range(0,121,20):
                    print("Invaild credits,credit is out of range!\nCredits must be one of: 0, 20, 40, 60, 80, 100, or 120.")
                    # If validation fails ,reprompt for respective credit.
                    continue
                else:
                    credit_input_list[credit_type] = credit_input
                    break
            # If a not-integer is inputed ,reprompt user for respective credit.
            except ValueError:
                print("Please enter a number(integer)!")
                continue
    return credit_input_list

def progression_outcome(pass_credit,defer_credit,fail_credit):
    # Checking if the total credits is equal 120.
    if (pass_credit+defer_credit+fail_credit) == 120:
        # Determine the progression outcome based on pass credit,defer credit and fail credit.
        if (pass_credit == 120):
            msg = "Progress"
            count_list[0]+= 1
        elif (pass_credit == 100):
            msg = "Progress(module trailer)"
            count_list[1]+= 1
        elif (fail_credit >=80):
            msg = "Exclude"
            count_list[3]+= 1
        else:
            msg = "Module retriever"
            count_list[2]+= 1
        print(f"Progression Outcome - {msg}")
        
        # Appending each progression data as a formated string to progression_results list.
        progression_results.append(f"{msg} - {pass_credit},{defer_credit},{fail_credit}")
    else:
        print("Invaild credits,credit total is incorrect!\ncredit total must be equal to 120.")
        # If the total credits is not equal 120, recursively call the progression_predictor function.
        progression_predictor()

def draw_column(count_list,graph):
    """Draws histogram columns based on progression outcome counts.
    Parameters:
        count_list (list): List containing counts of outcomes (Progress, Trailer, Retriever, Excluded).
        graph (GraphWin): Graphical window for drawing.
    """
    # Initializing local variables needed for the function
    outcomes = ("Progress","Trailer","Retriever","Excluded")
    colors = ("palegreen","yellowgreen","olive","pink")
    
    # Calculating the multiplier for scaling the histogram bars.
    multiplier = (400 // max(count_list))
    # using list comprehension
    value_list = [count * multiplier for count in count_list]
    
    # Drawing columns for each progression outcome.
    for i in range(4):
        x_value = i*120
        column = Rectangle(Point((x_value+40),479),Point((x_value+140),(479 - value_list[i])))
        count = Text(Point((x_value+90),(470 - value_list[i])),(count_list[i]))
        label = Text(Point((x_value+90),500),outcomes[i])
        
        # Setting column properties and drawing on the graph.
        column.setFill(colors[i])
        count.setStyle("bold")
        count.setTextColor("gray")
        label.setStyle("bold")
        label.setTextColor("gray")
        column.draw(graph)
        count.draw(graph)
        label.draw(graph)

def draw_lines(graph):
    """Draws horizontal lines on the graph.
    Parameters:
        graph (GraphWin): Graphical window for drawing.
    """
    for i in range(2):
        y_value = (i*430)+50
        line = Line(Point(20,y_value),Point(520,y_value))
        line.setWidth(2)
        line.draw(graph)
        
def welcome():
    """"Displays a welcome message."""
    print_doted_line()
    print("""                          **Welcome to the Progression Outcome Predictor**                      
    .This program helps you predict your progression outcome at the end of each academic year.
    .Please enter if you are student or staff member.students can predict progression outcome once,
    .while staff members can predict progression outcome of multiple students.
    .Then please enter the number of credits at pass, defer, and fail.
    .You will receive the appropriate progression outcome based on the given credits.""")
    print_doted_line()
    
def terminate_program():
    print_doted_line()
    print("""                                        Exiting the program!""")
    print_doted_line()
    # Exit the program.
    exit()

# Main function to execute the program.
def progression_predictor():
    """The progression_predictor function of the Progression Outcome Predictor.
    This function guides the user through the input process, validates the credits,
    determines the progression outcome, displays results, and handles user responses.
    """
    # Displays a line on terminal for better visual separation.
    print_doted_line()    
    # Asigning values for pass credit,defer credit and fail credit.
    pass_credit,defer_credit,fail_credit = get_credit_input()
    print_doted_line()
    # Determine the progression outcome based on pass credit,defer credit and fail credit.
    progression_outcome(pass_credit,defer_credit,fail_credit)
    # if user is student terminate the program
    if user == "student":
        terminate_program()
    else:
        # Validating response for continuing or quitting the program.
        print_doted_line()
        response = response_validation()
    
    if response == "q":
        print_doted_line()
        print("Displaying the histogram")
        print_doted_line()
        # Creates a window for Histogram.
        graph = GraphWin("Histogram",540,560)
        graph.setBackground("whitesmoke")
        # Display graph title.
        title = Text(Point(130,25),"Histogram Results")
        title.setSize(17)
        title.setStyle("bold")
        title.draw(graph)
        
        # Draw the lines in the histogram.
        draw_lines(graph)
        # Draw the columnS in the histogram.
        draw_column(count_list,graph)
        
        # Display total outcomes.
        total = Text(Point(140,535),f"{sum(count_list)} outcomes in total.")
        total.setSize(15)
        total.setStyle("bold")
        total.setTextColor("gray")
        total.draw(graph)
        
        try:
            # Close the graph window on mouse click.
            graph.getMouse()
        except GraphicsError:
            # If GraphicsError occurs ignore it.
            pass
        graph.close()
        
        # Display progression data using progression_results list.
        print("Part 2:--Using lists--")
        for progression_data in progression_results:
            print(progression_data) 
        print_doted_line()
        # Create a file named 'progression_data.txt' and write the progression data in the file,
        # Then read the data form 'progression_data.txt' and display progression data using the text file.
        print("Part 3:--Using text file--")
        with open ("progression_data.txt","w+") as file:
            file.write("\n".join(progression_results))
            file.seek(0)
            print(file.read())
        terminate_program()
    elif response == "y":
        # If user chooses to continue, recursively call the progression_predictor function.
        progression_predictor()
        
# Display the welcome message.
welcome()
# Validates the user who is using the program as a 'staff'or'student'
user = user_validation()
# If user is staff member program will allow user to predict progression outcome until user decide to stop
progression_predictor()
    