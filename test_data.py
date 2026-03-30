class CourierData:
   
    @staticmethod
    def valid_courier_data():
        return {
            "login": "test_courier",
            "password": "password123",
            "firstName": "Test"
        }
    
    @staticmethod
    def courier_without_login():
        return {
            "password": "password123",
            "firstName": "Test"
        }
    
    @staticmethod
    def courier_without_password():
        return {
            "login": "test_courier",
            "firstName": "Test"
        }
    
    @staticmethod
    def courier_without_firstname():
        return {
            "login": "test_courier",
            "password": "password123"
        }
    
    @staticmethod
    def login_data(login, password):
        return {
            "login": login,
            "password": password
        }
    
    @staticmethod
    def invalid_login_data():
        return {
            "login": "invalid_login",
            "password": "invalid_password"
        }
    
    @staticmethod
    def courier_with_existing_login(login):
        return {
            "login": login,
            "password": "different_password",
            "firstName": "DifferentName"
        }
    @staticmethod
    def login_data_missing_login():
        return {
            "password": "password123"
        }
    
    @staticmethod
    def login_data_missing_password():
        return {
            "login": "test_courier"
        }

class OrderData:
    
    @staticmethod
    def order_with_black_color():
        return {
            "firstName": "Пупа",
            "lastName": "Пупович",
            "address": "Москва, ул. Тестовая, д. 1",
            "metroStation": "4",
            "phone": "+7 999 999-99-99",
            "rentTime": 5,
            "deliveryDate": "2024-12-31",
            "comment": "Ласковый май",
            "color": ["BLACK"]
        }
    
    @staticmethod
    def order_with_grey_color():
        return {
            "firstName": "Саторо",
            "lastName": "Годжо",
            "address": "Москва, ул. Тестовая, д. 1",
            "metroStation": "4",
            "phone": "+7 989 699-93-69",
            "rentTime": 5,
            "deliveryDate": "2025-10-30",
            "comment": "Жду не дождусь",
            "color": ["GREY"]
        }
    
    @staticmethod
    def order_with_both_colors():
        return {
            "firstName": "Наруто",
            "lastName": "Иванович",
            "address": "Москва, ул. Тестовая, д. 1",
            "metroStation": "4",
            "phone": "+7 999 599-99-83",
            "rentTime": 5,
            "deliveryDate": "2026-01-31",
            "comment": "Приветик",
            "color": ["BLACK", "GREY"]
        }
    
    @staticmethod
    def order_without_color():
        return {
            "firstName": "Ламповый",
            "lastName": "Котик",
            "address": "Москва, ул. Тестовая, д. 1",
            "metroStation": "4",
            "phone": "+7 399 599-99-59",
            "rentTime": 5,
            "deliveryDate": "2024-12-31",
            "comment": "Нужна доставочка",
            "color": []
        }
    
class ListOrderData:

    @staticmethod
    def order_for_list_test():
        
        return {
            "firstName": "Тестовый",
            "lastName": "Клиент",
            "address": "Санкт-Петербург, Невский пр., д. 1",
            "metroStation": "5",
            "phone": "+7 911 111-11-11",
            "rentTime": 3,
            "deliveryDate": "2024-12-25",
            "comment": "Заказ для тестирования списка",
            "color": ["BLACK"]
        }
       
    @staticmethod
    def expected_order_fields():
        
        return ["id", "firstName", "lastName", "address", "metroStation", 
                "phone", "rentTime", "deliveryDate", "comment", "color"]
