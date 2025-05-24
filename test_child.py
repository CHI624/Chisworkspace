birth = 0624
class day:
  input(int(u = "Enter Victors Birthday(Month and Day only)"))
    while(i<5):
      if u == birth:
        print("You Guessed my Birthday!")
        return 0
      else if u !== birth:
        print("Wrong Try Again")
        i+=1
        day()
      else if i == 5:
        print("After 5 tries your Wrong, His Birthday is 0624")
    return 1
day()    
