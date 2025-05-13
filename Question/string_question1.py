#Q1) WAP to input a string and print the frequency of the characters.
#I/O :  aabccy
#O/P :  a:2, b:1, c:2, y:1 
       
       
content = input("Enter your string:")       

#convert in lower case
content = content.lower()
print(content)


for i in range(97,123): #a = 97, z=122
    count=0
    j=chr(i)
    for l in content:
        if j==l:
            count = count+1
    
    if count > 0:
       print(j, ":", count)
