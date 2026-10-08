import random
def select_random():
  random_choice= [8,15,18,20]
  selected=random.choice(random_choice)
  return selected
#print(select_random())


def make_choices():
  make_wish = input("what do you wish: ")
  return make_wish


def compare_num(name):
  choises=select_random()
  if choises <= 10:
    return f"{name} You are {choises} years old, Sorry you an infant"
  elif choises <= 17:
    return f"{name} You are {choises} years old, Sorry you are underage"
  elif choises == 18:
    wishes=make_choices()
    return f"{name} You are {choises} years old, You are an adult, you wish for a {wishes}"
  else:
    return f"{name} You are {choises} years old, You are are old"


print(compare_num("Kenneth"))