#!/usr/bin/python3

from model.engine.db_model import DBStorage
import secrets

secret_key = secrets.token_hex(16)
storage = DBStorage()
storage.reload()

