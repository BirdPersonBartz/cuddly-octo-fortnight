def fizzandbuzz(n):
    if n % 3 == 0 and n % 5 == 0:
        print 'Fizzbuzz'
    elif n % 3 == 0:
        print 'Fizz'
    elif n % 5 == 0:
        print 'buzz'
    else:
        print n


for i in range(1,100):
    print fizzandbuzz(i)

    
