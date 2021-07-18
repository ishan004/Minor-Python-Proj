# # # string concatenation (aka how to put string together )
# #suppose we want to create a string that says subscribe to  ____"

# youtuber = "kylie Ying " # some string variable 

# # a few ways to do this is
# print("subscribe to " + youtuber )
# print ("subscribe to {}".format(youtuber ))
# print (f"subscribe to {youtuber } ")

adj = input("Adjective: ")
verb1 = input("verb: ")
verb2 = input("verb: ")
famous_person = input("famous person: ")

madlib = f"Computer programming is so {adj}! It makes me so excited all the time because  I love to {verb1}. stay hydrated and {verb2} like you are {famous_person}!"

print(madlib)
 