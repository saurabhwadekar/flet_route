
MAIN = """import flet as ft
from flet_route import Routing
from routes import app_routes
from middlewares.app_middleware import AppBasedMiddleware

def main(page: ft.Page):

    Routing(
        page = page,
        app_routes = app_routes,
        middleware = AppBasedMiddleware().call_me
    )
    page.go(page.route)

ft.app(target=main)

"""

ROUTES = """from flet_route import path
from middlewares.url_middleware import UrlBasedMiddleware
from views.index_view import IndexView 
from views.next_view import NextView 



app_routes = [
    path(url="/",clear=True,view=IndexView().view), 
    path(url="/next_view/:my_id", clear=False, view=NextView().view ,middleware = UrlBasedMiddleware().call_me),
]

"""

INDEX_VIEW = """import flet as ft
from flet_route import Params,Basket

class IndexView:
    def __init__(self):
        ...

    def view(self,page:ft.page,params:Params,basket:Basket):
        print(params)
        print(basket)

        return ft.View(
            "/",
            controls=[
                ft.Text("This Is Index View"),
                ft.ElevatedButton("Go Next View", on_click=lambda _: page.go("/next_view/10")),
            ]
        )
"""

NEXT_VIEW = """import flet as ft
from flet_route import Params,Basket

class NextView:
    def __init__(self):
        ...

    def view(self,page:ft.page,params:Params,basket:Basket):
        print(params)
        print(basket)

        return ft.View(
            "/next_view/:my_id",
            controls=[
                ft.Text("This Is Next View"),
                ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/")),
            ]
        )
"""

APP_BASED_MIDDLEWARE = """import flet as ft
from flet_route import Params,Basket

class AppBasedMiddleware:
    def __init__(self):
        ...

    def call_me(self,page:ft.Page,params:Params,basket:Basket):

        print("App Based Middleware Called")
        #page.route = "/another_view" # If you want to change the route for some reason, use page.route
"""

URL_BASED_MIDDLEWARE = """import flet as ft
from flet_route import Params,Basket

class UrlBasedMiddleware:
    def __init__(self):
        ...

    def call_me(self,page:ft.Page,params:Params,basket:Basket):

        print("Url Based Middleware Called")
        #page.route = "/another_view" # If you want to change the route for some reason, use page.route
"""