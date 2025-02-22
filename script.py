import sys

def main():

# Here we created a function in which, depending on the arguments of sys.argv, behaves differently
# Case in which the arguments are only the script name and the file passed to the script
    if len(sys.argv) == 2:
        print_lines(10)

# If there are more than 2 arguments
    elif len(sys.argv) > 2:

# Case in which the second argument is "-n", the number of last lines printed should be the third argument
        if sys.argv[1] == "-n":

            num = int(sys.argv[2])
            print_lines(num)

# Case in which the first element of the second argument is "+", the program should start to print out lines from the line number equal to whatever follows the "+" 
        elif sys.argv[1][0] == "+":
            
            num = int(sys.argv[1][0:])
            print_lines(-num)


def print_lines(num):

    file = sys.argv[-1]
    with open(file, 'r') as file_name:
        lines = file_name.readlines()
        
    for line in lines[-num:]:
        print(line)


if __name__ == "__main__":
    main()