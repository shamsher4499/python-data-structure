# def first():
#     second()
#     print('first')

# def second():
#     third()
#     print('second')

# def third():
#     fourth()
#     print('third')

# def fourth():
#     print('fourth')

# first()

#-------------------------factorial-----------------------------

# def factorial(n):
#     assert n>=0 and int(n)==n, 'The number must be + integer only.'
#     if n in [0,1]:
#         return 1
#     else:
#         return n * factorial(n-1)

# print(factorial(4)) 

#---------------------end----------------------


#-------------------fibonacci------------------
# def fibonacci(n):
#     assert n>=0 and int(n)==n, 'The number must be + integer only.'
#     if n in [0,1]:
#         return n
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# print(fibonacci(4)) 

#------------------------end---------------------