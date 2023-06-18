
MAIN = """import flet as ft
from flet_route import Routing
from routes import app_routes
from middlewares.app_middleware import AppBasedMiddleware

async def main(page: ft.Page):

    Routing(
        page = page,
        app_routes = app_routes,
        middleware = AppBasedMiddleware,
        async_is = True
    )
    await page.go_async(page.route)

ft.app(target=main)

"""

ROUTES = """from flet_route import path
from middlewares.url_middleware import UrlBasedMiddleware
from views.index_view import IndexView 
from views.next_view import NextView 



app_routes = [
    path(url="/",clear=True,view=IndexView), 
    path(url="/next_view/:my_id", clear=False, view=NextView ,middleware = UrlBasedMiddleware),
]

"""

INDEX_VIEW = """import flet as ft
from flet_route import Params,Basket

async def IndexView(page:ft.Page,params:Params,basket:Basket):
    print(params)
    print(basket)

    async def go_next_view(e):
        await page.go_async("/next_view/10")
        
    return ft.View(
        "/",
        controls=[
            ft.Text("This Is Index View"),
            ft.ElevatedButton("Go Next View", on_click= go_next_view ),
        ]
    )

"""

NEXT_VIEW = """import flet as ft
from flet_route import Params,Basket

async def NextView(page:ft.Page,params:Params,basket:Basket):
    print(params)
    print(basket)
    
    async def go_index_view(e):
        await page.go_async("/")

    return ft.View(
        "/next_view/:my_id",
        controls=[
            ft.Text("This Is Next View"),
            ft.ElevatedButton("Go Index View", on_click= go_index_view),
        ]
    )

"""

APP_BASED_MIDDLEWARE = """import flet as ft
from flet_route import Params,Basket

async def AppBasedMiddleware(page:ft.Page,params:Params,basket:Basket):

    print("App Based Middleware Called")
    #page.route = "/another_view" # If you want to change the route for some reason, use page.route
"""

URL_BASED_MIDDLEWARE = """import flet as ft
from flet_route import Params,Basket

async def UrlBasedMiddleware(page:ft.Page,params:Params,basket:Basket):

    print("Url Based Middleware Called")
    #page.route = "/another_view" # If you want to change the route for some reason, use page.route
"""