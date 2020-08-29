# Take the input value to start with
input_string = input("Enter a 5 digit number")
while True : #keep the loop running till user doesnt input the valid input
    if len(input_string) == 5: # Check if the input lengeth is equal to 5
        try: # try statement because if user inputs alphabets istead of number we will get an exception
            total = sum([int(num) for num in input_string]) # sum all 5 digits with list compression
            print(total) # if everything went ok print the total
            break # and break out of the while loop
        except: #if we got exception in above try statement the we will run everything below this line
            pass
    print("invalid input")
    input_string = input("Enter a 5 digit number \n")














