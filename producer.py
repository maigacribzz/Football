from faker import Faker
import random
import datetime as dt 
from datetime import timedelta
import time
import pprint
import asyncio
from azure.eventhub import EventData
from azure.eventhub.aio import EventHubProducerClient
import json

class Products:

    def __init__(self):
        self.product_list= []
        self.total = 0
        self.fk = Faker()
    def setTotal(self):
        self.total = 0

    def get_product_list(self):
        return self.product_list
    def current_product(self):
        return self.product_list

    def generate_product_id(self):
        number = '01293456789'
        p_id = "P-"
        temp =[]
        for i in range(6):
            temp.append(random.choice(number))
        random.shuffle(temp)
        return p_id + "".join(temp)
    
    def create_product_list(self):
        product_name = ["iphoneX","iphoneX pro","mac book pro","dell","bike","pen","monitor"]
        price =[1000,1100,1200,920,200,19,240]
        stock = [1000,1000,1000,1000,1000,1000,1000]
        for i in range(len(product_name)):
            inner_data ={}
            inner_data["productName"] = product_name[i]
            inner_data["productPrice"] = price[i]
            inner_data["productStock"] = stock[i]
            inner_data["productId"] = self.generate_product_id()
            self.product_list.append(inner_data)
    def add_product(self,name,price=None,stock=None):
        inner_data = {}
        inner_data["productName"] = name
        inner_data["productPrice"] = 0 if price is None else price
        inner_data["productStock"] = 0 if stock is None else stock
        inner_data["productId"] = self.generate_product_id()
        self.product_list.append(inner_data)
    
    def del_product(self,product_id):
        for i in range(len(self.product_list)):
            if self.product_list[i]["productId"] == product_id:
                self.product_list.pop(i)
                break

    def update_stock(self,number,product_id):
        for i in self.product_list:
            if i["productId"] == product_id :
                updated_stock = i["productStock"] - number
                if number >= 0:
                    i["productStock"] = updated_stock
                else:
                    i["productStock"] = 1000

    def generate_random_items(self,number):
        items_list = []
        print(len(self.product_list))
        if len(self.product_list) == 0:
            self.create_product_list()
        if len(self.product_list) > 0:
            for i in range(number):
                inner_data={}
                product = random.choice(self.product_list)
                qty = random.randint(1,11)
                self.total += qty * product["productPrice"]
                inner_data["productName"] = product["productName"]
                inner_data["productPrice"] = product["productPrice"]
                inner_data["quantity"] = qty
                inner_data["productId"] = product["productId"]
                inner_data["subTotal"] =  qty * product["productPrice"]
                self.update_stock(qty,product["productId"])
                items_list.append(inner_data)

        return items_list

class Customer:
    customer_data =[]
    @classmethod
    def generate_customer_id(cls):
        upper_letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        lower_letters = 'abcdefghijklmnopqrstuvwxyz'
        digits = '1234567890'
        customer_id = "C-"
        option = [upper_letters,lower_letters,digits]
        for i in range(1,11):
            value = random.choice(option)
            customer_id += random.choice(value)
        return customer_id

    @classmethod
    def generate_customer_data(cls,number=1):
        fk = Faker()
        for i in range(number):
            inner_data = {}
            customer_name = fk.name()
            customer_email = fk.email()
            customer_phone_number = fk.phone_number()
            customer_country = fk.country()
            customer_id = Customer.generate_customer_id()
            customer_ssn = fk.ssn()
            inner_data["customerId"]=customer_id
            inner_data["customerName"] = customer_name
            inner_data["customerEmail"] = customer_email
            inner_data["customerPhoneNumber"] = customer_phone_number
            inner_data["customerCountry"] = customer_country
            inner_data["customerSSN"] = customer_ssn 
            cls.customer_data.append(inner_data)
        return cls.customer_data
    @classmethod
    def get_random_customer(cls):
        return random.choice(cls.customer_data)
    
class Orders(Products,Customer):
    orders_list =[]

    @classmethod
    def get_orders_list(cls):
        return cls.orders_list
    @classmethod
    def create_order_number(cls):
        order_number = []
        number = "0123456789"
        for i in range(11):
            order_number.append(random.choice(number))
        random.shuffle(order_number)
        return "".join(order_number)
    @classmethod
    def generate_order_details(cls,how_many_order=1,how_many_item=1):
        obj = cls()
        inner_order_list=[]
        for i in range(how_many_order):
            obj.setTotal()
            inner_data ={}
            inner_data["orderId"] = Orders.create_order_number()
            inner_data["orderCreatedDate"] =   str(dt.datetime.now() - timedelta(days=random.randint(0,5)))
            inner_data["orderItems"] = obj.generate_random_items(how_many_item)
            inner_data["status"] = "OC"
            inner_data["total"] = obj.total
            inner_data["customerDetails"] = Customer.get_random_customer()
            cls.orders_list.append(inner_data)
            inner_order_list.append(inner_data)
        return inner_order_list
    @classmethod
    def update_order_status(cls):
        updated_order_list =[]
        for i in range(len(cls.orders_list)):
            value = random.choice(cls.orders_list)
            if value["status"] == "OC":
                value["status"] = "IT"
                cls.orders_list[i]["status"] = "IT"
                value["updatedDate"] = str(dt.datetime.now())
                updated_order_list.append(value)
                
            elif value["status"] == "IT":
                value["status"] = "DL"
                cls.orders_list[i]["status"] = "DL"
                value["updatedDate"] = str(dt.datetime.now())
                updated_order_list.append(value)
        return updated_order_list

class SendDataToEventHub:
    
    def __init__(self):
        self.eventhub_namespace ="" #eventhub connection str
        self.eventhub = "" #eventhub name

    def producer(self,data):
        async def run():
            producer = EventHubProducerClient.from_connection_string(
                conn_str = self.eventhub_namespace,
                eventhub_name = self.eventhub
            )
            async with producer:
                event_data_batch = await producer.create_batch()
                for i in data:
                    event_data_batch.add(EventData(json.dumps(i)))
                    print(f"message sent :: {json.dumps(i)}")
                await producer.send_batch(event_data_batch)
                
        asyncio.run(run())

def Main():
    Customer.generate_customer_data(100)
    eh = SendDataToEventHub()
    while True:
        time.sleep(1)
        if random.randint(1,10) == 7:
            order_data = Orders.generate_order_details(random.randint(1,5),random.randint(1,10))
            eh.producer(order_data)

        elif random.randint(1,10) == 5:
            update_order_data = Orders.update_order_status()
            if len(update_order_data) > 0:
                eh.producer(update_order_data)     
        else:
            print("missed out....")
if __name__ == "__main__":
    Main()










