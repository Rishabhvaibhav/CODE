
from collections import Counter
text = "My name is rishabh vaibhav , my name is rishabh vaibhav , my name is pritam , my name is aashu , name name rishabh , vaibhav"

word = text.split()


count = Counter(word)
print(count)


# for word in reversed(count):
#     print(f"{word}: {count[word]}")


