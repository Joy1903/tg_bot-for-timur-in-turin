from aiogram import Bot, Dispatcher, executor, types
from config import API_TOKEN
import markup as nav
from datetime import datetime
from dateutil.relativedelta import relativedelta
from db1 import DB, get_db_connect 

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
db_connet = DB()

# я заню что код не очень красивый мягко говоря, но это написаный на коленках по гайдом от горе разработчикови код, так что не судите строго 

# массивы для хранения информации пользователя и проверки всех состояний в момент регестраци 
temp = []
check = []

# массивы для хранения информации пользователя и проверки всех состояний в момент резервироваия машины 
tempR =[]
checkReservation = []

# массивы для хранения информации пользователя и проверки всех состояний в момент закрытия зарезервированой машины 
tempC =[]
checkCR = []

# для пролистования машин в разделе резервирования и закрытия зарезервированых машин
steps = [0]

@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    temp.clear()
    await message.answer("Hi!👋", reply_markup=nav.mainMenu)
    if get_db_connect() == 1: 
        await message.answer("db is not connected, try later😕")

@dp.message_handler()
async def echo(message: types.Message):
    if message.text == 'Reservate⬇️' or message.text == 'Next variation⏩':
        if get_db_connect() != 1:
            arr_models = db_connet.get_inner_join_table_for_reservations()
            user_check = db_connet.get_value_by("*","users","user_id_by_tg",str(message.from_user.id))
            if len(user_check) > 0:
                if type(arr_models) != str: 
                    if len(arr_models)-1 > steps[0]+3:
                        await message.answer("Choose👇", reply_markup=nav.menuReservateManufactor(arr_models, steps[0]))
                        steps[0] = steps[0]+1
                    else:
                        await message.answer("more is not exsist❌", reply_markup=nav.menuReservateManufactor(arr_models, steps[0]))
                else:
                    await message.answer("there is problem with connect data base, please try leter🔄")
            else:
                await message.answer("You have to regestrate", reply_markup=nav.mainMenu)
            
        else:
            await message.answer("db is not connected, try later🔄")
    elif message.text == 'Regastrate⬇️' or message.text == 'Save📲':
        if len(check) <= 0:
            await message.answer("Enter your contact number📱", reply_markup = nav.regMenu)
            check.append(1)
        elif len(check) > 0 and len(check) < 3:
            await message.answer("Enter your seriess passport🔢", reply_markup = nav.regMenu)
    elif message.text == 'Home🏠':
        checkReservation.clear()
        temp.clear()
        check.clear()
        tempR.clear()
        steps.clear()
        tempC.clear()
        checkCR.clear()
        steps.append(0)
        await message.answer("Well👍", reply_markup = nav.mainMenu)
    elif message.text == "Complained Again🔄":
        check.clear()
        temp.clear()
        await message.answer("well👍", reply_markup = nav.regMenu1)
    elif message.text == 'Exactly save📲':
        if get_db_connect() != 1:
            user = db_connet.get_value_by("*", 'users', 'user_id_by_tg', str(message.from_user.id))
            if type(user) == str:
                await message.answer("db is not connected, try later❌")
            else:    
                if db_connet.insert_values_in_users(message.from_user.id, message.from_user.full_name, temp[1], temp[0]) == 1:
                    await message.answer("Sucseed✅")
                    temp.clear()
                else:
                    await message.answer("This accaunt is exist❌")
        else:
            await message.answer("db is not connected, try later❌")
    elif message.text == "Cancel reservate" or message.text == "Next reservations⏩":
        if get_db_connect() != 1:
            user_check = db_connet.get_value_by("*","users","user_id_by_tg",str(message.from_user.id))
            if len(user_check) > 0:
                cars = db_connet.get_value_by("car_id", "reservation", "user_id", str(message.from_user.id))
                if type(cars) != str:
                    if len(cars) > 0:
                        if len(cars)-1 > steps[0]:
                            await message.answer("Choose👇", reply_markup=nav.menuCancelReservateManufactor(cars, steps[0]))
                            steps[0] = steps[0]+1
                        else:
                            await message.answer("more is not exsist❌", reply_markup=nav.menuCancelReservateManufactor(cars, steps[0]))
                    else:
                        await message.answer("You didn't reservate any cars❌")
                else:
                    await message.answer("There is problem with connect data base, please try leter❌")
            else:
                await message.answer("You have to regestrate", reply_markup=nav.mainMenu)
        
        else:
            await message.answer("db is not connected, try later❌")

# регистрация 
    if len(check) > 0 and len(temp) <= 1: 
        if message.text != "Regastrate⬇️" and  message.text != "Save📲":
            temp.append(message.text)
            check.append(2) 
    elif len(check) >= 2 and len(temp) > 1:
        await message.answer("Is it correct? Contact number - "+temp[0]+"; Seriess passport - "+temp[1], reply_markup = nav.formMenu)
        check.clear()
    
# резервирование машины 
    if len(checkReservation) > 0:
       checkReservation.append(1)
       tempR.append(message.text) 

    if "💵" in message.text:
        tempR.append(message.text.split('-')[1])
        if get_db_connect() != 1:
            result = db_connet.get_value_by_car_id(tempR[0])
            if type(result) != str:
                await message.answer("How many days do you want to have a car?🕑 Please write like this 'number days' for example 5 days\nNumber of days have to lass then 20")
                checkReservation.append(1)
            else:
                await message.answer(result)
        else:
            await message.answer("db is not connected, try later❌")
    elif "days" in message.text:
        if len(checkReservation) > 1:
            if (tempR[1].split(' ')[0]).isdigit():
                if int(tempR[1].split(' ')[0]) < 20:
                    if get_db_connect() != 1:
                        date_after_month = datetime.today()+ relativedelta(days=int(tempR[1].split(' ')[0]))
                        responds = db_connet.insert_values_in_reservation(message.from_user.id, tempR[0].strip(), datetime.today().strftime('%Y-%m-%d'), date_after_month.strftime('%Y-%m-%d'))
                        responds_of_change = db_connet.change_status_to_true(tempR[0].strip())
                        if responds == 1 and responds_of_change == 1:
                            await message.answer("Sucseed✅\nWe will call you as soon as possible!📱", reply_markup=nav.mainMenu)
                            steps.clear()
                            steps.append(0)
                            checkReservation.clear()
                            tempR.clear()
                        else:
                            tempR.clear()
                            await message.answer("Something was wrong, try again❌")
                    else:
                        tempR.clear()
                        await message.answer("db is not connected, try later❌")
                else:
                    tempR.clear()
                    await message.answer("number of days have to lass then 186")
            else:
                tempR.clear()
                await message.answer("You have to write like this:\nHow many days do you want to have a car?🕑 Please write like this 'number days' for example 5 days")

# удаление машины из зарезервированых
    if "❌" in message.text:
        tempC.append((message.text.split('❌'))[0])
        result = db_connet.delete_value("reservation", "car_id", tempC[0].strip())
        if result == 1:
            cars = db_connet.change_status_to_false(tempC[0].strip())
            if cars == 1:
                await message.answer("Sucseed✅", reply_markup=nav.mainMenu)  
                steps.clear()
                steps.append(0)
                tempC.clear()
            else:
                await message.answer(cars)
        else:
            message.answer(result)

        

  

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)