dict2={"skill":"A quality in a human being",
       "python":"Most easily recognisable language on the planet",
       "human":"species of animals also known as homo sapiens",
       "racism":"a bad behaviour towards different races",
       "mother":"tinimini"}
print("Enter your word out of")
print(dict2.keys())
inpum=input()

print("meaning is", dict2.get(inpum))