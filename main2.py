import re

pattern = "\w{5,50}@\w{3,10}.\w{2,3}.\w{2,3}"  # email
text = "aaabbbcc rodrigo123@gmail.com.br"
answer = re.search(pattern, text)

print(answer.group())
