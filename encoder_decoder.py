def main():
    while user_choice != 3:
        print("Menu")
        print("-------------")
        print("1. Encode")
        print("2. Decode")
        print("3. Quit")
        print()
        user_choice = int(input("Please enter an option: "))
        if user_choice == 1:
            user_input = input("Please enter your password to encode: ")
            current_password = encoder(user_input)
            print("Your password has been encoded and stored!")
            print()
        elif user_choice == 2:
            #once decoder is added, remove hashtag below
            #print(f"The encoded password is {''.join(current_password)}, and the original password is {decoder(current_password)}.")
            print()



def encoder(user_input):
    password_list = []
    for i in range(len(user_input)):
        password_list.append(user_input[i])
        password_list[i] = int(password_list[i])
    for i in range(len(password_list)):
        if password_list[i] >= 0 and password_list[i] <= 6:
            password_list[i] += 3
        elif password_list[i] == 7:
            password_list[i] = 0
        elif password_list[i] == 8:
            password_list[i] = 1
        elif password_list[i] == 9:
            password_list[i] = 2
    return password_list


