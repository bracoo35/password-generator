import random    #uses system time as default seed


print("Random Password Generator")

length = int(input("Enter the desired password length (1-64 characters): "))
#upp_and_low = input("Include upper and lower case? (Y/N) ")
#special_char = input("Include special characters? ( !@#$%^&*() ) (Y/N) ")

#alpha_list_lower = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n',
#'o','p','q','r','s','t','u','v','w','x','y','z']

#alpha_list_upper = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N',
#'O','P','Q','R','S','T','U','V','W','X','Y','Z']

#special_list = ['!','@','#','$','%','^','&','*','(',')']

'''
if user answers yes to wanting lower/upper/special chars
can combine lists, in a couple ways   
list3 = alpha_list_lower + special_list
or
for x in list2:
	list1.append(x)
or
list1.extend(list2)
'''

num_list = [1,2,3,4,5,6,7,8,9,0]

new_pw = []

for i in range(length):
	#x = (num_list[rand_int])
	#new_pw[i] = str(x)
	rand_int = random.randrange(0,10)     #makes num_list redundant?
	new_pw.append(rand_int)

	print(new_pw)

#print("length is",length)


#print("Your password is: ")

