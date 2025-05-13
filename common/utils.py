# Utility functions placeholder
import hashlib
from cerberus import Validator
from common.schema import item_schema

def generate_id(url, title):
    return hashlib.sha256(f"{url}{title}".encode()).hexdigest()

def validate_item(item):
    v = Validator(item_schema)
    return v.validate(item)
