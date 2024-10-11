from locust import HttpUser, task, between

class DemoblazeUser(HttpUser):
    wait_time = between(1, 5)  # Время ожидания между запросами в секундах

    @task(1)
    def index_page(self):
        self.client.get("/")

    @task(2)
    def product_page(self):
        self.client.get("/prod.html?idp_=1")  # Пример страницы продукта

    @task(1)
    def login(self):
        self.client.post("/login", {"username": "testuser", "password": "secret"})

    @task(1)
    def signup(self):
        self.client.post("/signup", {"username": "newuser", "password": "newpass"})

    @task(1)
    def add_to_cart(self):
        self.client.post("/addtocart", {"id": "1", "cookie": "some_cookie", "prod_id": "1"})