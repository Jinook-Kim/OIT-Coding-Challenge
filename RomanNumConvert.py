def decimal_to_rom(num):
    data_dict = {1000:"M", 900:"CM", 500:"D", 400:"CD", 100:"C", 90:"XC", 50:"L", 40:"XL", 10:"X", 9:"IX", 5:"V", 4:"IV", 1:"I"}
    
    result = ""
    for key, value in data_dict.items():
        quotient = num // key
        remainder = num % key
        result += value * quotient
        num = remainder
        
    return result


def data_to_dict():
    result = {}
    for i in range(1, 4000):
        result[decimal_to_rom(i)] = i
    
    return result


def main():
    rom_dict = data_to_dict()
    
    while(1):
        user_input = input('\nEnter a Roman numeral or "EXIT" to exit: ')
        user_input = user_input.upper()
        if user_input == "EXIT":
            return
        
        try:
            print(f'Roman numerl "{user_input}" is equivalent to {rom_dict[user_input]} in decimal.')
        except KeyError:
            print("Invalid input. Please try again.")


if __name__ == "__main__":
    main()