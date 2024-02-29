def space(x):
    existing=False
    for i in x:
        if i==' ':
            existing=True
    return(existing)

def wordFromSentence(x):
    newx=''
    for i in x:
        if i!=' ': newx+=i
    return newx

word=input("a vizsgalnivalo szo: ")

if word[0] == word[-1]:
    print("egyezik")
else:
    print("nem egyezik")

y=space(word)

#if y==true:
#   print("van szokoz")
#else:
#   ("nincs szokoz")

# a felso rovidebben:
print("van szokoz") if y else print("nincs szokoz")


x=True
newWord=wordFromSentence(word)

for i in range(len(newWord)//2+1):
    if newWord[i]!=newWord[-1-i]: x=False
print("palindrom") if x else print("nem palindrom")

#print(wordFromSentence(word))