def psswrd():
  password = "red"
  guess = input("Enter password: ")
  count = 0
  limit = 3
  while guess != password and count != limit:
    count += 1
    guess = input("Incorrect " + str(count) + "/" + str(limit) + ", try again: " )
  if count == limit and password != guess:
    print("Too many invalid inputs")
  elif password == guess:
    print("Correct password!")

psswrd()
  