from random import randint

def dice(param):
    """
    function returns result of dice roll
    :param param: number of rolls, type of dice and modifier, split by space
    :return: result of x dice rolls + modifier
    """
    list_of_parameters = param.split()

    number_of_dice_rolls = int(list_of_parameters[0])
    dice_type = list_of_parameters[1]
    modifier = int(list_of_parameters[2])
    types_of_dice = ["D3", "D4", "D6", "D8", "D10", "D12", "D20", "D100"]
    dice_walls = {"D3":3, "D4":4, "D6":6, "D8":8, "D10":10, "D12":12, "D20":20, "D100":100}

    if dice_type in types_of_dice:
        dice_result = randint(1, dice_walls[dice_type])
        result = number_of_dice_rolls * dice_result + modifier
        return result
    else:
        return "Wrong data"

my_result = dice("01 D6 05")
print(my_result)






