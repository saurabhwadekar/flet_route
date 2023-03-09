# This makes dynamic routing easier.

Excuse me I don't know English. This has been translated by Google Translate.
Let me know if you don't understand anything

We have to write a lot of (if, else) statements for routing and passing the params to the view is very difficult.
But now all we need to do is to create a routing object in the main function and pass the page and routing list.
in routing list We'll use the path function. it returns a list
In this function we have to pass the routing url, in clear we have to (true/false) and in view we have to pass a function which will return ft.view


example:

## main.py
```python
import flet as ft
from flet_core import Routing,path
from views.index_view import IndexView
from views.next_view import NextView

def main(page: ft.Page):

    app_routes = [
        path(url="/", clear=True, view=IndexView),
        path(url="/next_view/:my_id", clear=False, view=NextView),
    ]

    Routing(page=page,app_routes=app_routes)
    page.go(page.route)

ft.app(target=main)

```

## views/index_view.py
```python
import flet as ft

def IndexView(page: ft.Page,params={}):
    print(params)
    return ft.view(
        "/",
        controls=[
            ft.Text("This Is Index View"),
            ft.ElevatedButton("Go Next View", on_click=lambda _: page.go("/next_view/10")),
        ]
    )

```

## views/next_view.py
```python
import flet as ft

def NextView(page: ft.Page,params={}):
    print(params)
    return ft.view(
        "/next_view/:my_id",
        controls=[
            ft.Text("This Is Next View"),
            ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/")),
        ]
    )

```

