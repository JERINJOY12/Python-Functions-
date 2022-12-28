alphabets = ['a','b','i','e','c','d','u','d']
vowels = ['a','e','i','o','u']
ans = list(filter(lambda x: True if x=='a'or x=='e' or x=='i' or x=='o' or x=='u' else False,alphabets))
print(ans)
