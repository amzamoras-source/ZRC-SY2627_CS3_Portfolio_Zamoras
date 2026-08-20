#Chinese Zodiac Sign

#Requirements
- Prompt the user to enter their birth year (1900 or later).
- Calculate and display the corresponding Chinese Zodiac sign
- Stop the program execution if an invalid year (< 1900) is entered.

#Python Code

    print("Hey there, let's determine your Chinese Zodiac Sign! Please input your birth year.")

    def zodiac_sign():
        zodiac_animals = {
            0: "Monkey (猴 - Hóu)",
            1: "Rooster (鸡 - Jī)",
            2: "Dog (狗 - Gǒu)",
            3: "Pig (猪 - Zhū)",
            4: "Rat (鼠 - Shǔ)",
            5: "Ox (牛 - Niú)",
            6: "Tiger (虎 - Hǔ)",
            7: "Rabbit (兔 - Tù)",
            8: "Dragon (龙 - Lóng)",
            9: "Snake (蛇 - Shé)",
            10: "Horse (马 - Mǎ)",
            11: "Goat (羊 - Yáng)"
    }

    while True:
        birth_year = int(input("Enter your birth year: "))
        
        if birth_year < 1900:
            print("Please enter a valid birth year (1900 or later).")
            return
        else:
            sign_key = birth_year % 12
            animal = zodiac_animals[sign_key]
            print(f"Your Chinese Zodiac Sign is: {animal}")
            break

   <img width="1279" height="576" alt="Screenshot 2026-08-20 172637" src="https://github.com/user-attachments/assets/de90ceb4-4caf-4ab4-86c2-2886df6e10ed" />
