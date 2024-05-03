from flet import View, Page, AppBar, NavigationBar
from repath import match
from .not_found_view import ViewNotFound, ViewNotFound_async
from .params import Params
from .basket import Basket
from typing import Callable


def route_str(route):
    if type(route) == str:
        return route
    else:
        return str(route.route)


def path(url: str, clear: bool, view: Callable[[Page, Params, Basket], View], middleware: Callable[[Page, Params, Basket], None] = None):
    """
    ```
    path(
        url = "/", # Here you have to give that url which will call your view on mach
        clear = True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
        view = IndexView # Here you have to pass a function or method which will take page and params and return ft.View
    )
    ```
    """
    return [url, clear, view, middleware]


class Routing:
    """
    Routing Example
    ```
    import flet as ft
    from flet_route import Routing,path

    def index_view(page,params,basket):
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
            not_found_view = ViewNotFound # If you want that there should be a different view call when no path matches, then you can pass that view here. otherwise no need to give it it will call ViewNotFound by default
            )
        page.go(page.route)
    ft.app(target=main)
    ```
    """

    def __init__(
            self,
            page: Page,
            app_routes: list,
            middleware: Callable[[Page, Params, Basket], None] = None,
            async_is=False,
            not_found_view: Callable[[Page, Params, Basket], View] = None,
            appbar: AppBar = None,
            navigation_bar: NavigationBar = None,
    ):

        self.async_is = async_is
        self.page = page
        self.app_routes = app_routes
        self.appbar = appbar
        self.navigation_bar = navigation_bar
        self.__middleware = middleware
        self.__params = Params({})
        self.__basket = Basket()
        if self.async_is:
            self.page.on_route_change = self.change_route_async
            self.page.on_view_pop = self.view_pop_async
            if not_found_view == None:
                self.not_found_view = ViewNotFound_async
            else:
                self.not_found_view = not_found_view
        else:
            self.page.on_route_change = self.change_route
            self.page.on_view_pop = self.view_pop
            if not_found_view == None:
                self.not_found_view = ViewNotFound
            else:
                self.not_found_view = not_found_view

    def change_route(self, route):
        notfound = True
        for url in self.app_routes:
            path_match = match(url[0], self.page.route)
            if path_match:
                self.__params = Params(path_match.groupdict())
                if self.__middleware != None:
                    self.__middleware(  # call main middleware
                        page=self.page,
                        params=self.__params,
                        basket=self.__basket
                    )
                # if chnge route using main midellware recall change route
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[3] != None:
                    url[3](  # call url middleware
                        page=self.page,
                        params=self.__params,
                        basket=self.__basket
                    )

                # if chnge route using url midellware recall change route
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[1]:
                    self.page.views.clear()
                view = url[2](
                    page=self.page,
                    params=self.__params,
                    basket=self.__basket
                )
                view.appbar = self.appbar
                view.navigation_bar = self.navigation_bar
                self.page.views.append(
                    view
                )
                notfound = False
                break
        if notfound:
            self.__params = Params({"url": self.page.route})
            self.page.views.append(
                self.not_found_view(
                    page=self.page,
                    params=self.__params,
                    basket=self.__basket
                )
            )
        self.page.update()

    def view_pop(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)

    async def change_route_async(self, route):
        notfound = True
        for url in self.app_routes:
            path_match = match(url[0], self.page.route)
            if path_match:
                self.__params = Params(path_match.groupdict())
                if self.__middleware != None:
                    await self.__middleware(  # call main middleware
                        page=self.page,
                        params=self.__params,
                        basket=self.__basket
                    )
                # if chnge route using main midellware recall change route
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[3] != None:
                    await url[3](  # call url middleware
                        page=self.page,
                        params=self.__params,
                        basket=self.__basket
                    )

                # if chnge route using url midellware recall change route
                if self.page.route != route_str(route=route):
                    self.page.go(self.page.route)
                    return

                if url[1]:
                    self.page.views.clear()
                view = await url[2](
                    page=self.page,
                    params=self.__params,
                    basket=self.__basket
                )
                view.appbar = self.appbar
                view.navigation_bar = self.navigation_bar

                self.page.views.append(
                    view
                )
                notfound = False
                break
        if notfound:
            self.__params = Params({"url": self.page.route})
            self.page.views.append(
                await self.not_found_view(
                    page=self.page,
                    params=self.__params,
                    basket=self.__basket
                )
            )
        self.page.update()

    async def view_pop_async(self, view):
        self.page.views.pop()
        top_view = self.page.views[-1]
        self.page.go(top_view.route)
