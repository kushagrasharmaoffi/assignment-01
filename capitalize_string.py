def capitalize(set1):
     set1, result = set1.title(), ""
     for word in set1.split():
        result += word[:-1] + word[-1].upper() + " "
     return result[:-1]  

print(capitalize ("Python is a high level programming language"))