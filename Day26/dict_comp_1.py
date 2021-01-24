sentence = "What is the Airspeed Velocity of an Unladen Swallow?"

list_words = sentence.split()

result = {word:len(word) for word  in list_words}


print(result)

