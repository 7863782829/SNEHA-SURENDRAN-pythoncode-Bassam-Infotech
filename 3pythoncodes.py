#1. to swap values of two variables without the intervention of third variable.
var1 = int(input(""))
var2 = int(input(""))
var1 == var2
var1,var2 = var2,var1
print(var1,var2)




#2. to convert uppercase to lowercase and viceversa
string = input("")
new_string = ("")
for i in range(len(string)):
    if string[i].isupper():
      new_string = new_string + string[i].lower()
    else:
      new_string = new_string + string[i].upper()
print(new_string)




#3. to find no of  substring occurs in a string
def count_substring(string, sub_string):
    count=0
    for i in range(len(string)):
        if string[i:i+len(sub_string)]==sub_string:
            count+=1
    return count

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)
