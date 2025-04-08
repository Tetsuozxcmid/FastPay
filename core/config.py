import os
from dotenv import load_dotenv

load_dotenv()


class Config:
    @staticmethod
    def get_stripe_secret_key():
        return os.getenv("STRIPE_KEY")

    @staticmethod
    def get_stripe_publish_key():
        return os.getenv("STRIPE_PUBLISH_KEY")

    @staticmethod
    def get_premium_price_id():
        return os.getenv("PREMIUM_PRICE_ID")

    @staticmethod
    def get_basic_price_id():
        return os.getenv("BASIC_PRICE_ID")

    @staticmethod
    def get_customer_id():
        return os.getenv("CUSTOMER_ID")
