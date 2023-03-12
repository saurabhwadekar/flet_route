from flet import View,Page
from repath import match
from flet_route import ViewNotFound



def path(url: str, clear: bool, view: View):
    """
    ```
    path(
        url = "/", # Here you have to give that url which will call your view on mach
        clear = True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
        view = IndexView # Here you have to pass a function or method which will take page and params and return ft.View
    )
    ```
    """
    return [url, clear, view]



class Routing:
    """
    Routing Example
    ```
    import flet as ft
    from flet_route import Routing,path

    def index_view(page,params):
        return ft.View(
            "/",
            controls=[
                ft.Text("This Is Index View")
            ]
        )

    def main(page: ft.Page):

        app_routes = [
            path(url="/", clear=True, view=IndexView),
        ]

        Routing(
            page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
            app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
            not_found_view:View=ViewNotFound # If you want that there should be a different view call when no path matches, then you can pass that view here. otherwise no need to give it it will call ViewNotFound by default
            )
        page.go(page.route)
    ft.app(target=main)
    ```
    """

    def __init__(self, page: Page, app_routes: list,not_found_view:View=ViewNotFound):
        self.page = page
        self.not_found_view = not_found_view
        self.page.on_route_change = self.change_route
        self.page.on_view_pop = self.view_pop
        self.app_routes = app_routes

    def change_route(self, route):
        notfound = True
        for url in self.app_routes:
            path_match = match(url[0], self.page.route)
            if path_match:
                if url[1]:
                    self.page.views.clear()
                self.page.views.append(
                    url[2](page=self.page, params=path_match.groupdict()))
                notfound = False
                break
        if notfound:
            self.page.views.append(self.not_found_view(page=self.page,params={"url":self.page.route}))
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
