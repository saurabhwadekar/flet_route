# This makes it easy to manage multiple views with dynamic routing.

This is an utility class based on repath library which allows matching ExpressJS-like routes and parsing their parameters, for example `/account/:account_id/orders/:order_id`.

## Installation
```
pip install flet-route
```

## Upgradation
```
pip install flet-route --upgrade
```



## function based view:

### main.py
```python
import flet as ft
from flet_route import Routing,path
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

### views/index_view.py
```python
import flet as ft

def IndexView(page,params):
    print(params)
    return ft.View(
        "/",
        controls=[
            ft.Text("This Is Index View"),
            ft.ElevatedButton("Go Next View", on_click=lambda _: page.go("/next_view/10")),
        ]
    )

```

### views/next_view.py
```python
import flet as ft

def NextView(page,params):
    print(params)
    return ft.View(
        "/next_view/:my_id",
        controls=[
            ft.Text("This Is Next View"),
            ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/")),
        ]
    )

```





## Class based view:

### main.py
```python
import flet as ft
from flet_route import Routing,path
from views.index_view import IndexView
from views.next_view import NextView

def main(page: ft.Page):

    app_routes = [
        path(url="/", clear=True, view=IndexView().view),
        path(url="/next_view/:my_id", clear=False, view=NextView().view),
    ]

    Routing(page=page,app_routes=app_routes)
    page.go(page.route)

ft.app(target=main)


```

### views/index_view.py
```python
import flet as ft

class IndexView:
    def __init__(self):
        ...

    def view(self,page,params):
        print(params)
        return ft.View(
            "/",
            controls=[
                ft.Text("This Is Index View"),
                ft.ElevatedButton("Go Next View", on_click=lambda _: page.go("/next_view/10")),
            ]
        )

```

### views/next_view.py
```python
import flet as ft

class NextView:
    def __init__(self):
        ...

    def view(self,page,params):
        print(params)
        return ft.View(
            "/next_view/:my_id",
            controls=[
                ft.Text("This Is Next View"),
                ft.ElevatedButton("Go Index View", on_click=lambda _: page.go("/")),
            ]
        )

```


## Author

<b>Name :</b> Saurabh Wadekar<br>
<b>Email :</b> saurabhwadekar420@gmail.com<br>
<b>County :</b> 🇮🇳INDIA🇮🇳<br>

<h1>❤️ THANK YOU ❤️</h1><br>