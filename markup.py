from pickle import TRUE
from aiogram.types import ReplyKeyboardMarkup,  KeyboardButton

# тут кнопки знаю очевидно но всё же 

btnHome = KeyboardButton("Home🏠")
btnSave = KeyboardButton("Save📲")
btnSaveReg = KeyboardButton("Exactly save📲")
btnComplainAgain = KeyboardButton("Complained Again🔄")
btnRegestrate = KeyboardButton("Regastrate⬇️")
btnReservate = KeyboardButton("Reservate⬇️")
btnCancelReservate = KeyboardButton("Cancel reservate")



mainMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnRegestrate, btnReservate, btnCancelReservate)
regMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHome,btnSave)
formMenu = ReplyKeyboardMarkup(resize_keyboard=True).add(btnSaveReg,btnComplainAgain,btnHome)
regMenu1 = ReplyKeyboardMarkup(resize_keyboard=True).add(btnHome,btnRegestrate)


# Функция симулирующая пролистывания машин но один фиг все равно я загружаю сразу все машины 

def menuReservateManufactor(arr_model, steps = 0):
    btnM0 = KeyboardButton(arr_model[steps][0]+": "+arr_model[steps][1]+": "+str(arr_model[steps][2])+"💵 - "+arr_model[steps][3])
    btnM1 = KeyboardButton(arr_model[steps+1][0]+": "+arr_model[steps+1][1]+": "+str(arr_model[steps+1][2])+"💵 - "+arr_model[steps+1][3])
    btnM2 = KeyboardButton(arr_model[steps+2][0]+": "+arr_model[steps+2][1]+": "+str(arr_model[steps+2][2])+"💵 - "+arr_model[steps+2][3])
    btnNext = KeyboardButton("Next variation⏩")
    menuManufac = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM0,btnM1,btnM2,btnNext,btnHome)
    return menuManufac
 
# Функция симулирующая пролистывания машин которые зарезервированны 
def menuCancelReservateManufactor(arr_cars, steps = 0):
    btnM0 = KeyboardButton(arr_cars[steps][0]+" ❌")
    btnNext = KeyboardButton("Next reservations⏩")
    menuCarsForCancelReservate = ReplyKeyboardMarkup(resize_keyboard=True).add(btnM0,btnNext,btnHome)
    return menuCarsForCancelReservate
