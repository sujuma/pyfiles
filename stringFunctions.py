print("'spam eggs'")
print('doesn\'t')
print("doesn't")
print('"Yes," he said.')
print("\"yes,\" he said.")
print("I'm in Kolkata but i dont't know that \"you are also here\" . I'll see you in Howrah!. But i'll request 'you' to bring \"Rasagulla\" for me.")
print(isinstance(4,object))
print(isinstance("Hello",object))
print(isinstance(None,object))
print(isinstance([1,2,3],object))
print((64).__sizeof__())


def compute(a,b,c):
    return (a+b)*c
a=1
b=2
c=3
print(compute(a,b,c))
print(compute([1],[2,3],2))
print(compute('o','la',4))
print(1==1.0)
print("Apple" == "apple")
greeting = "Hello World i am here so what to do"
print(len(greeting))
print(greeting.find('lo'))
print(greeting.replace('h','y'))
print(greeting)
print(greeting.startswith('Hell'))
print(greeting.isalpha())
print(greeting.replace('h','y'))
print(greeting.lower())
print(greeting.title())
print(greeting.strip())
print(greeting.strip('o'))
print("ram and sam are god".split())
print('01-10-19'.split(sep='-'))
print('   '.join(['Hello','John','How','are','you']))
print('{} {}'.format('Monte', 'Carlo'))
print("{0} can be {1} {0}s".format("Strings", "formatted"))
print("{name} loves {food}".format(name="Sam", food="plums"))
print("{} squared is {}".format(5, 5**2))


