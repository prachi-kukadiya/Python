# it is used when we dont know the number of iteration and we want to execute our loop body code as long as our condition is true.

#syntax :-
# initialization -> condition -> loop body -> increment/decrement -> condition again


# 1.
# i=1  #initialization

# while i<=1000:  #condition
#     print(i)  #loop body
#     i+=1   #increment


# 2.
# i=2

# while i<=100:
#     print(i)
#     i+=2


# 3. 
# 5 table using while loop :-
i=1
j=5

while i <= 10:
    k = j * i
    print(j, "X", i, "=", k)
    i += 1