#while loop template #1
#do something n times
ct = 0
while ct < 4:
    print("hi")
    #ct = ct + 1
    ct += 1

#while loop template #2
#do something for each item in a list
lst = ["berg", "law", "custodio", "hsieh"]
while lst != []:
    print(lst.pop(0))

#while loop template #3
#do something for each item in a list but we care about the index
lst2 = ["berg", "law", "custodio", "hsieh"]
ctr = 0
while ctr < len(lst2):
    print(f"Name #{ctr} is: {lst2[ctr]}")
    ctr += 1

#while loop template #4 
#do something until a condition is met (more generally)
# while True:
#     print("yay spring!!!!")

#print vs return  example
def foo(x):
    return x*2
    #print(x*2)

z = foo(3)
print(f"z is: {z}")

#None or NoneType
def factorial(n: int) -> int: 
    if n < 0:
        return None
    result = 1
    while n > 1:
        result *= n  #result = result * n
        n -= 1 # n = n - 1
    return result

#break
for i in [1,2,3,4,5,6]:
    if i%3 == 0:
        break
print(f"after loop completed, i is {i}")

#continue
for j in range(10):
    if j%2 ==0:
        continue 
    print(f"j is {j}")


#pass 
for k in [1,2,3,4,5,6]:
    if k%3 == 0:
        pass
    else:
        print(f"{k} is not a multiple of 3.")

print("   string".strip())

from typing import List, Any 

#type hints
#y = 5
y: int = 5
#foo = []
bar: List[str] = []
tushar: List[Any] = []

def mult_lists(l1: List[int], l2: List[int]) -> List[int]:
    result: List[int] = [] 
    if len(l1) != len(l2):
        return None
    for i in range(len(l1)):
        #result.append(l1[i]*l2[i])
        result += [l1[i]*l2[i]]  
    return result

#x += y
#x = x + y

assert mult_lists([1,2,3], [2,2,2]) == [2,4,6]