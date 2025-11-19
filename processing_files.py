"""
1. Open sales_totals in read mode (Download the start file)
2. Read each line in a loop
3. Strip newline and convert to float
4. Add to running total
5. Count the lines
6. Format and print each number
7. Print the total, count, and average
8. Use a main() function
9. Use try and except for errors
"""
def main(): #define main
    #initialize starting variables
    total_sales = 0.0
    line_count = 0

    try:
        with open('sales_totals.txt','r') as file: #opens sales_totals in read mode
            print("\n---Sales Report---\n") #title w/break
            for line in file: #read each line in for loop
                edited_line = line.strip() #strip each line

                if edited_line: #check if each line isn't empty before converting
                    try:
                        """ lines 29 & 31 used += assignment operators https://www.w3schools.com/python/python_operators_assign.asp"""

                        sale_amount = float(edited_line) #convert stripped line to float

                        total_sales += sale_amount #add to running total

                        line_count += 1 #count the lines, adding 1 each time

                        average_sale = total_sales/line_count #calculate average

                        formatted_sale = f"{sale_amount:,.2f}" #format each number w/comma + round to nearest hundredth
                        print(f"Sale #{line_count}: ${formatted_sale}") #print each sale w/line count & formatted sale

                    except ValueError: #if one of the values is not a valid number; e.g. multiple '.'s
                        print(f"{line.strip()} is not a valid number.") 

            #print summary of total, count, and average
            print("\n---Summary---\n") 
            print(f"Total sales amount: ${total_sales:,.2f}")
            print(f"Number of sales: {line_count}")
            print(f"Average sale amount: ${average_sale:,.2f}")

    except IOError: #if the file is not found, since using external file: sales_totals.txt
        print("An IOError has occurred.")

    except Exception as e: #catches errors that happen w/in try block
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__": #call main; code only works when executed
        main() 