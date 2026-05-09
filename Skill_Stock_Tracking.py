def log_skill(name, progress):
    bar = "#" * (progress // 10)
    print(f"\n--- {name} Progress ---")
    print(f"[{bar:<10}] {progress}%")
    if progress >= 100:
        print("Mastered! 🏆")
    else:
        print("Work hard")
    with open("Projectbirthday.txt", "a")as f:
        f.write(
            f"Skill: {name} | Progress: {progress}% | Visual: [{bar:<10}]\n")


def get_stock_signal(price):
    if price < 400:
        return "Buy"
    else:
        return "Hold"


def announcment(reason, date):
    Notice = f"Tommorow date {date}college is holiday due to {reason}"
    with open("Announcement Detail.txt", "a")as f:
        f.write(Notice + "\n")

def history():
    print("\n--- Project Birthday LoG---\n")
    with open("Projectbirthday.txt","r") as f:
        content=f.read()
        print(content)
    
 
while True:
    print("1. Log a Skill")
    print("2. Check a Stock")
    print("3. Create a Notice")
    print("4. History Checking")
    print("5. Exit")

    choice = int(input("Enter option 1-4: "))

    if choice == 1:
        s_name = input("Enter the skill name: ")
        S_progress = int(input("Enter you progress (1-100): "))

        log_skill(s_name, S_progress)

    if choice == 2:
        price = int(input("Enter the price of Stock: "))
        result = get_stock_signal(price)
        print(f"The signal is {result}")
    if choice == 3:
        reason = input("What is the reason of holiday ?")
        date = input("On what date the holdiay is give? ")
        announcment(reason, date)
    if choice==4:
        history()

    if choice ==5:
        print("Exitiing....")
        break
