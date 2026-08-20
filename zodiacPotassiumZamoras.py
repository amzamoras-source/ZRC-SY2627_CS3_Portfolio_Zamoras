# #zodiac signgngnng

# print("Hey there, let's determine your Chinese Zodiac Sign! Please input your birth year.")

# def zodiac_sign():
#     while True:
#         birth_year = int(input("Enter your birth year: "))
#         sign = birth_year % 12
        
#         if birth_year < 1900:
#             print("Please enter a valid birth year (1900 or later).")
#         else:
#             break

#         zodiac_animals = {
#             0: "Monkey",
#             1: "Rooster",
#             2: "Dog",
#             3: "Pig",
#             4: "Rat",
#             5: "Ox",
#             6: "Tiger",
#             7: "Rabbit",
#             8: "Dragon",
#             9: "Snake",
#             10: "Horse",
#             11: "Goat"
#         }
    
#         break

#     print(f"Your Chinese Zodiac Sign is: {sign}")
    

# zodiac_sign()

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
        else:
            break

    sign_key = birth_year % 12
    animal = zodiac_animals[sign_key]

    print(f"Your Chinese Zodiac Sign is: {animal}")

zodiac_sign()