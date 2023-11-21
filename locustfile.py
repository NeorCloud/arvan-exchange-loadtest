import os

from locust import task
from locust import FastHttpUser


class Trader1(FastHttpUser):
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.get("/login/")
        self.client.post(
            "/login/",
            data={"username": "trader", "password": "ar_exchange"},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def profile(self):
        self.client.get("/profile/")

    @task
    def deposit(self):
        self.client.get("/profile/deposit/")
        self.client.post(
            "/profile/deposit/",
            data={
                "name": "trader",
                "card_number": "1111222233334444",
                "card_ccv": "123",
                "amount": "1000",
            },
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def get_tether_page(self):
        self.client.get("/token/tether/")
    
    @task
    def buy_tether(self):
        self.client.post(
            "/token/tether/",
            data={"amount": "30", "buy_token": ""},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

class Trader2(FastHttpUser):
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.get("/login/")
        self.client.post(
            "/login/",
            data={"username": "trader2", "password": "ar_exchange"},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def profile(self):
        self.client.get("/profile/")

    @task
    def deposit(self):
        self.client.get("/profile/deposit/")
        self.client.post(
            "/profile/deposit/",
            data={
                "name": "trader2",
                "card_number": "1111222233334444",
                "card_ccv": "123",
                "amount": "10000",
            },
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def get_tether_page(self):
        self.client.get("/token/tether/")
    
    @task
    def buy_tether(self):
        self.client.post(
            "/token/tether/",
            data={"amount": "300", "buy_token": ""},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def sell_tether(self):
        self.client.post(
            "/token/tether/",
            data={"amount": "30", "sell_token": ""},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def get_ethereum_page(self):
        self.client.get("/token/ethereum/")

    @task
    def buy_ethereum(self):
        self.client.post(
            "/token/ethereum/",
            data={"amount": "10", "buy_token": ""},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )
    
    @task
    def sell_ethereum(self):
        self.client.post(
            "/token/ethereum/",
            data={"amount": "1", "sell_token": ""},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

class Trader3(FastHttpUser):
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        self.client.get("/login/")
        self.client.post(
            "/login/",
            data={"username": "trader3", "password": "ar_exchange"},
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def profile(self):
        self.client.get("/profile/")

    @task
    def deposit(self):
        self.client.get("/profile/deposit/")
        self.client.post(
            "/profile/deposit/",
            data={
                "name": "trader3",
                "card_number": "1111222233334444",
                "card_ccv": "123",
                "amount": "1500",
            },
            headers={"X-CSRFToken": self.client.cookies["csrftoken"]},
        )

    @task
    def get_tether_page(self):
        self.client.get("/token/tether/")
    
    @task
    def get_ethereum_page(self):
        self.client.get("/token/ethereum/")

    @task
    def get_bitcoin_page(self):
        self.client.get("/token/bitcoin/")