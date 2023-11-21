import os

from locust import task
from locust import FastHttpUser


def login(user, username, password):
    response = user.client.get("/login/")
    csrftoken = response.cookies["csrftoken"]
    user.client.post(
        "/login/",
        data={
            "username": username,
            "password": password,
            "csrfmiddlewaretoken": csrftoken,
        },
    )


class Trader1(FastHttpUser):
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        login(self, "trader", "ar_exchange")

    @task
    def profile(self):
        self.client.get("/profile/")

    @task
    def deposit(self):
        response = self.client.get("/profile/deposit/")
        self.client.post(
            "/profile/deposit/",
            data={
                "name": "trader",
                "card_number": "1111222233334444",
                "card_ccv": "123",
                "amount": "1000",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )

    @task
    def get_tether_page(self):
        self.client.get("/token/tether")

    @task
    def buy_tether(self):
        response = self.client.get("/token/tether")
        self.client.post(
            "/token/tether",
            data={
                "amount": "30",
                "buy_token": "",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )


class Trader2(FastHttpUser):
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        login(self, "trader2", "ar_exchange")

    @task
    def profile(self):
        self.client.get("/profile/")

    @task
    def deposit(self):
        response = self.client.get("/profile/deposit/")
        self.client.post(
            "/profile/deposit/",
            data={
                "name": "trader2",
                "card_number": "1111222233334444",
                "card_ccv": "123",
                "amount": "10000",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )

    @task
    def get_tether_page(self):
        self.client.get("/token/tether")

    @task
    def buy_tether(self):
        response = self.client.get("/token/tether")
        self.client.post(
            "/token/tether",
            data={
                "amount": "300",
                "buy_token": "",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )

    @task
    def sell_tether(self):
        response = self.client.get("/token/tether")
        self.client.post(
            "/token/tether",
            data={
                "amount": "30",
                "sell_token": "",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )

    @task
    def get_ethereum_page(self):
        self.client.get("/token/ethereum")

    @task
    def buy_ethereum(self):
        response = self.client.get("/token/ethereum")
        self.client.post(
            "/token/ethereum",
            data={
                "amount": "10",
                "buy_token": "",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )

    @task
    def sell_ethereum(self):
        response = self.client.get("/token/ethereum")
        self.client.post(
            "/token/ethereum",
            data={"amount": "1", "sell_token": "", "csrfmiddlewaretoken": response.cookies["csrftoken"]},
        )


class Trader3(FastHttpUser):
    host = os.getenv("HOST", "http://localhost:8000")

    @task
    def home(self):
        self.client.get("/")

    @task
    def login(self):
        login(self, "trader3", "ar_exchange")

    @task
    def profile(self):
        self.client.get("/profile/")

    @task
    def deposit(self):
        response = self.client.get("/profile/deposit/")
        self.client.post(
            "/profile/deposit/",
            data={
                "name": "trader3",
                "card_number": "1111222233334444",
                "card_ccv": "123",
                "amount": "1500",
                "csrfmiddlewaretoken": response.cookies["csrftoken"],
            },
        )

    @task
    def get_tether_page(self):
        self.client.get("/token/tether")

    @task
    def get_ethereum_page(self):
        self.client.get("/token/ethereum")

    @task
    def get_bitcoin_page(self):
        self.client.get("/token/bitcoin")


class ReadonlyUser(FastHttpUser):
    host = os.getenv('HOST', 'http://localhost:8000')

    @task
    def get_admin_page(self):
        self.client.get('/admin/login/?next=/admin/')