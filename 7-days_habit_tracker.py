
perfect_days = []
for day in range(1, 8):
    print(f"Day {day}")
    status = (input("Is today a rest day(y/n):"))
    if status == "y":
        print("Rest day")
        continue
    elif status == "n":
        for Set in range(1, 4):
            rep = 1
            while (rep <= 5):
                print(f"Set Number{Set},Rep{rep}")
                rep += 1
        print("*" * 5+"Success tracker" + "*"*5)
        protien_intake = int(input("How much Protien intake did you took"))
        video = input("Did you made you daily Video(y/n): ")
        if protien_intake >= 100 and video == "y":
            print("🌟 PERFECT DAY! You are winning at life.")
            perfect_days.append(day)
        elif protien_intake < 100 and video == "y":
            print("🌟 Please Improve you protien intake!.")
        elif protien_intake > 100 and video == "n":
            print("🌟 Please Focus on you Content Creation")
        else:
            print("Rest is okay, but don't lose the momentum!")
print(perfect_days)
