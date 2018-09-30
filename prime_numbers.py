#Tusubira David 2018/HD05/198U
#Angole Daniel
#Allan Murungi
#Nanziri Eunice

def primes(number):                    #Function has one argument for the input number
    output_list = []                   #create output list variable
    for i in range(2, number):         #for loop iterates over the range of numbers between 2 and the input number
        if i%2 != 0:                   #check if current number is a prime number
            output_list.append(i)      #append the current number only if it is a prime number
    return output_list

#TESTING
print(primes(20))
