from math import fabs
import mysql.connector

# Класс DB для конекта с базой данных пыталься сдеть его гибким но из за обьёмных запросов это было бы не читабельно 
# Хотя мой код всё равно не читабелен 

def get_db_connect(host = "localhost", user="root", password = "", database = "cars"):
    try:
        mydb = mysql.connector.connect(
            host=host,
            user=user,
            password=password,
            database=database
        )
        return mydb
    except mysql.connector.Error:
        return 1


class DB:
    def __init__(self, mdb = get_db_connect()): 
        if mdb != 1:
            self.mycursor = mdb.cursor()
            self.sdb = mdb
            self.state = True
        else:
            self.state = False


    def get_all_values_from(self, table):
        if self.state:
            try:
                self.mycursor.execute("SELECT * FROM "+table+"")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."
    
    def get_value_from(self, name_of_space, table):
        if self.state:
            try:
                self.mycursor.execute("SELECT "+name_of_space+" FROM "+table+"")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."

     
    def get_all_values_for_customers(self, table, name_of_space, value):
        if self.state:
            try:
                self.mycursor.execute("SELECT * FROM "+table+" where "+name_of_space+" = "+str(value)+"")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время." 

    def get_value_by(self, name_of_spaces, table, name_of_space_for_choose, value):
        if self.state:
            try:
                self.mycursor.execute("SELECT "+name_of_spaces+" FROM "+table+" where "+name_of_space_for_choose+" = '"+value+"'")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время." 

    def get_value_by_car_id(self, value):
        if self.state:
            try:
                self.mycursor.execute("SELECT * FROM cars where `number_id` = '"+value+"'")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."


    def get_all_values_for_customers(self, table, name_of_space, value, name_of_space2, value2):
        if self.state:
            try:
                self.mycursor.execute("SELECT * FROM "+table+" where "+name_of_space+" = "+value+" and "+name_of_space2+" = "+value2+"")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."



    def insert_values_in_users(self, value1, value2, value3, value4):
        if self.state:
            val = (value1, value2, value3, value4)
            try:
                self.mycursor.execute("INSERT INTO users (user_id_by_tg, fullname, passport_seriess, cantact_number) VALUES (%s, %s, %s, %s)", val)
                self.sdb.commit()
                return 1
            except mysql.connector.Error as err:
                if err.errno != 1062:
                    return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."

    
    def insert_values_in_reservation(self, value1, value2, value3, value4):
        if self.state:
            val = (value1, value2, value3, value4)
            try:
                self.mycursor.execute("INSERT INTO reservation (user_id, car_id, data_get, data_return) VALUES (%s, %s, %s, %s)", val)
                self.sdb.commit()
                return 1
            except mysql.connector.Error as err:
                if err.errno != 1062:
                    return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."
        

    def get_inner_join_table_for_reservations(self):
        if self.state:
            try:
                self.mycursor.execute("SELECT car_canufacturer.car_manufacturer_name, model.model_of_car, cars.price, cars.number_id FROM cars INNER JOIN car_canufacturer INNER JOIN model ON cars.car_manufacturer_id = car_canufacturer.car_manufacturer_id and cars.model_id = model.id WHERE cars.status_of_reservation = 0")
                return self.mycursor.fetchall()
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."
    
    def change_status_to_true(self, id):
        if self.state:
            try:
                self.mycursor.execute("UPDATE `cars` SET `status_of_reservation`= '1' WHERE `number_id` = '"+id+"'")
                self.sdb.commit()
                return 1
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."

    def change_status_to_false(self, id):
        if self.state: 
            try:
                self.mycursor.execute("UPDATE `cars` SET status_of_reservation= '0' WHERE number_id = '"+id+"'")
                self.sdb.commit()
                return 1
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."
    
    def delete_value(self, table, name_of_space_for_choose, value):
        if self.state:
            try:
                self.mycursor.execute("DELETE FROM `"+table+"` WHERE "+name_of_space_for_choose+" = '"+value+"'")
                self.sdb.commit()
                return 1
            except mysql.connector.Error as err:
                return f"Неполадки с базой данных.\nКод ошибки{err}"
        return "Неполадки с базой данных.\nПовторите попытку через какоето время."