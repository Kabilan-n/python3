secret_no=7
guess_count=0
guess_limit=3
while guess_count< guess_limit:
    guess=int(input("guess: "))
    guess_count+=1
    if guess==secret_no:
        print("u won!")
        break
else:
    print("u failed!")