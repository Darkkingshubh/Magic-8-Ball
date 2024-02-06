MAGIC 8 Ball
import random

question = input('Question: ')

random_number = random.randint(1, 9)

if random_number == 1:
  print("Definitely.")
elif random_number == 2:
  print("It is decidely so.")
elif random_number == 3:
  print("Without a doubt.")
elif random_number == 4:
  print("Not answering that, please Try again")
elif random_number == 5:
  print("Better not tell you now.")
elif random_number == 6:
  print("My sources say no.")
elif random_number == 7:
  print("Outlook not so good.")
elif random_number == 8:
  print("Very doubtful.")
else:
  print("ERROR 404 NOT FOUND")