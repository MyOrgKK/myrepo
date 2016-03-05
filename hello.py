print ("Hello World from Geany")
sum = 1+1
print (sum)
name="Kavin"
print ("Hello "+name)
age = 6
# adding single line comment

print ("Happy " + str(age) + "th Birthday")
friends = ["kiran","kishori","vaishali","anjali","lakshmi"]

print (friends)
friends.reverse()
print (friends)
friends.sort()
print (friends)

for name in friends:
	print ("Hello "+name)
	
squares = [value**2 for value in range(1,11)]
print (squares)

squares = [value**2 for value in range(1,11,2)]
print (squares)

dimensions = (200,400)
print (dimensions)

aliens = {"color" : "green", "type" : 1}

print (aliens['color'])

