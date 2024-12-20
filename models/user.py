from pymongo import MongoClient
from werkzeug.security import generate_password_hash, check_password_hash
from config import Config

client = MongoClient(Config.MONGO_URI)
db = client["brain_rot_checker"]
user_collection = db["users"]

class User:
    @staticmethod
    def create_user(username, password, role="user"):
        if user_collection.find_one({"username": username}):
            return False
        hashed_password = generate_password_hash(password)
        user_collection.insert_one({
            "username": username,
            "password": hashed_password,
            "role": role
        })
        return True

    @staticmethod
    def authenticate(username, password):
        user = user_collection.find_one({"username": username})
        if user and check_password_hash(user["password"], password):
            return user
        return None

    @staticmethod
    def get_user(username):
        return user_collection.find_one({"username": username})
