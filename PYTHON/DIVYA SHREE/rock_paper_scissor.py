import random

value = True
while value:  # infinite run of the game

    computer_choose = random.randint(0, 2)
    try:
        user_input = input("Your Turn: \nrock(0) \npaper(1) \nscissors(2)\nChoose any: ")
        user_choose = int(user_input)
        print("Computer Turn:", computer_choose)

        if computer_choose == user_choose:
            print("                                                                                  🔥 𝑀𝒶𝓉𝒸𝒽 𝒟𝓇𝒶𝓌 🔥 ")
        elif computer_choose > user_choose:
            print("                                                                           ✴✧    🔥 𝒞❀𝑀𝒫𝒰𝒯𝐸𝑅 𝒲𝐼𝒩 🔥    ✧✴   ")
        elif computer_choose == 0 and user_choose == 1:
            print("                                                                                    🅨 🅞 🅤   🅦 🅘 🅝۫    ")
        elif computer_choose == 1 and user_choose == 2:
            print("                                                                                    🅨 🅞 🅤   🅦 🅘 🅝۫    ")
        elif computer_choose == 2 and user_choose == 0:
            print("                                                                                    🅨 🅞 🅤   🅦 🅘 🅝۫    ")
        elif computer_choose == 0 and user_choose == 2:
            print("                                                                           ✴✧    🔥 𝒞❀𝑀𝒫𝒰𝒯𝐸𝑅 𝒲𝐼𝒩 🔥    ✧✴   ")
        elif 0 <= user_choose <= 2:
            print("                                                                                       🅸🅽🆅🅰🅻🅸🅳")
        else:
            print("                                                                                       🅸🅽🆅🅰🅻🅸🅳")
    except ValueError:
        print("Invalid input! Please enter a valid number.")
