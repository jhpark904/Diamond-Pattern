# PROGRAMMING ASSIGNMENT 05
# Filename: 'exercise1.py'
#
# Write the code for function diamond.
# The function diamond:
#   • takes one parameter N (type int), its value must be odd and in the range [3, 99]
#   • it draws a square shape made of integer values and spaces:
#       - integer values are always printed with 2 digits (for example, value 7 is printed 07)
#       - every line consists of integer values from 1 up to N , where some values have to be
#       replaced by spaces instead
#       - the first and last row are full (no space)
#       - the middle row is empty except for values 1 and N ,
#       - each row from the FIrst one to the middle one is increasingly empty from its center
#       - each row from the middle one to the last one is increasingly full to its center

def main():
    #try to draw some diamonds by calling the function diamond
    print('Calling: diamond(5)')
    diamond(5)
    
    #empty line
    print()
    
    print('Calling: diamond(15)')
    diamond(15)


def diamond(N):
    #WRITE YOUR CODE HERE
    # set a starting and ending index
    start = (N + 1) / 2 + 1
    finish = (N + 1) / 2 - 1
    for i in range(N):  # each line
        for j in range(1,N + 1):    # each number/space in one line
            if i == 0 or i == N - 1:    # just number in first and last lines
                print('{0:02d}'.format(j), end='')
            elif j >= start and j <= finish:    # to print space
                print('  ', end='')
            else:
                print('{0:02d}'.format(j), end='')
        # code to change starting and ending index
        # switch the direction for the second half of the diamond
        if i < (N - 1) / 2:
            start -= 1
            finish += 1
        else:
            start += 1
            finish -= 1
        print()
    


#Call the main() function
main()
