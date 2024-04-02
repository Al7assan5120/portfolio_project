#!/usr/bin/python3
from model.admin import Admin
from model import storage

admin_data = {
        "first_name": "Alhassan",
        "last_name": "Ramadan",
        "password": "hassan123",
        "email": "alhassan@gmail.com"
    }

admin1 = Admin(**admin_data)
storage.new(admin1)
storage.save()

print(admin1.first_name)
print(admin1.password)
