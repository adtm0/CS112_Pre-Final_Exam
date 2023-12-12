n_start = eval(input("Enter a number [start]: "))

if n_start == 0:
    print("Program terminated.")
    exit()

while (n_start < 0):
     print("Enter a non-negative number.")
     n_start = eval(input("\nEnter a number [start]: "))
     
n_end = eval(input("Enter a number [end]: "))

while (n_end < n_start):
     print(f"Enter a number greater than {n_start}.")
     n_end = eval(input("\nEnter a number [end]: "))

prime_list = []
for i in range(n_start, n_end + 1):
    
    if i == 1:
        continue
    
    for j in range(2,i):
        if (i % j) == 0:
            break
    else:
            prime_list.append(i)
            
print(f"Prime numbers between {n_start} and {n_end} are: {str(prime_list).strip('[],').replace(',','')}")
