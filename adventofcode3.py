def parseLines():
    print('parsing')
    array2D = []
    line1D = []
    with open('adventofcode3.txt') as f:
        lines = f.readlines() # list containing lines of file
        for line in lines:
            for symbol in line:
                if symbol != '\n':
                    line1D.append(symbol)
            array2D.append(line1D)
            line1D = []
    print(array2D)

    number_of_rows = len(array2D)
    number_of_columns = len(array2D[0])
    character_found = False
    list_of_numbers = []
    list_of_star_counters = [[0 for row in range(number_of_rows)] for col in range(number_of_columns)]
    list_of_gear_sums = [[1 for row in range(number_of_rows)] for col in range(number_of_columns)]
    actual_number = str()
    int_actual_number = 0
    sum_of_numbers = 0
    character_added = False
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            print("row: " +str(row) + "      column: " + str(column))
            if array2D[row][column].isalnum():
                
                actual_number += array2D[row][column]
                
                end_of_line_reached, next_character_not_number = 0,0
                if (column + 1 == number_of_columns):
                    end_of_line_reached = True
                elif not array2D[row][column + 1].isalnum():
                    next_character_not_number = True

                if end_of_line_reached or next_character_not_number:
                    #end of Number reached
                    int_actual_number = int("".join(actual_number))
                    for row_offset in range(row - 1 , row + 2):
                        for column_offset in range(column - len(actual_number) , column + 2):
                            try:
                                if not array2D[row_offset][column_offset].isalnum() and array2D[row_offset][column_offset] != '.':
                                    character_found = True
                                    if array2D[row_offset][column_offset] == '*':
                                        list_of_star_counters[row_offset][column_offset] += 1
                                        list_of_gear_sums[row_offset][column_offset] *= int_actual_number

                                    
                            except IndexError:
                                pass
                        if character_found and not character_added:
                            list_of_numbers.append(int_actual_number)
                            sum_of_numbers += int_actual_number
                            character_added = True
                        character_found = False
                        character_added = False
                            
                    actual_number = str()

                 

    print(list_of_numbers)
    print ("finito, sum is " + str(sum_of_numbers))

    gears_sum = 0
    for row in range(number_of_rows):
        for column in range(number_of_columns):
            if (list_of_star_counters[row][column]==2):
                #gear at this position
                #print("gear at row " + str(row) + " and column " + str(column))
                gears_sum += list_of_gear_sums[row][column]

                pass

    print("gears sum is " + str(gears_sum))
    return

def main():
    print('main')
    parseLines()

if __name__ == "__main__":
    main()