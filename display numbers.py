"""
This code is to act like a seven-segment display. The task is to write a program which is able to simulate
the work of a seven-display device. When you input a number you want to display on the monitor, the program
will work for you for the purpose.
"""


number = input("Enter a number you want to display: ")
num_list = list(number)
#print(num_list)

display_dict = {
    '1': [' # ', ' # ', ' # ', ' # ', ' # '],
    '2': ['###', '  #', '###', '#  ', '###'],
    '3': ['###', '  #', '###', '  #', '###'],
    '4': ['# #', '# #', '###', '  #', '  #'],
    '5': ['###', '#  ', '###', '  #', '###'],
    '6': ['###', '#  ', '###', '# #', '###'],
    '7': ['###', '  #', '  #', '  #', '  #'],
    '8': ['###', '# #', '###', '# #', '###'],
    '9': ['###', '# #', '###', '  #', '###'],
    '0': ['###', '# #', '# #', '# #', '###']
}

for i in range(5):
    for num in num_list:
        if num in display_dict.keys():
            print(('').join(display_dict[num][i]), end=' ')
        else:
            print("Please input a valid number!")
    print('')
