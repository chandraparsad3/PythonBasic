#lambda Functions
# A lambda function is a short, nameless function 
# in Python, ideal for simple tasks. It's created 
# without a full function definition and is handy 
# for quick operations, like doubling a number 
# with `lambda x: x * 2`.

adds= lambda x,y: x+y

print(adds(5,6))

finding_max=lambda x,y: x if x>y else y
print(finding_max(5,6))

s="Pradeep"
lengths= lambda s: len(s)
print(lengths(s))