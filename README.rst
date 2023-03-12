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
from views.index_view import IndexView # Here IndexView is imported from views/index_view.py
from views.next_view import NextView # Here NextView is imported from views/next_view.py

def main(page: ft.Page):

    app_routes = [
        path(
            url="/", # Here you have to give that url which will call your view on mach
            clear=True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=IndexView # Here you have to pass a function or method which will take page and params and return ft.View (If you are using function based view then you just have to give the name of the function.)
            ), 
        path(url="/next_view/:my_id", clear=False, view=NextView),
    ]

    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        #not_found_view:View=ViewNotFound # If you want that there should be a different view call when no path matches, then you can pass that view here. otherwise no need to give it it will call ViewNotFound by default
        )
    page.go(page.route)

ft.app(target=main)


```

### views/index_view.py

This is a basic python function that takes `page` and `params` and returns `ft.View`.

In `page` we get the `page` passed in `path`.

In `params` we get the values ​​passed from `url` in the form of `dictionary`

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

This is a basic python function that takes `page` and `params` and returns `ft.View`.

In `page` we get the `page` passed in `path`.

In `params` we get the values ​​passed from `url` in the form of `dictionary`

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
from views.index_view import IndexView # Here IndexView is imported from views/index_view.py
from views.next_view import NextView # Here NextView is imported from views/next_view.py

def main(page: ft.Page):

    app_routes = [
        path(
            url="/", # Here you have to give that url which will call your view on mach
            clear=True, # If you want to clear all the routes you have passed so far, then pass True otherwise False.
            view=IndexView().view # Here you have to pass a function or method which will take page and params and return ft.View (If you are using class based view then you have to pass method name like IndexView().view .)
            ),
        path(url="/next_view/:my_id", clear=False, view=NextView().view),
    ]

    Routing(
        page=page, # Here you have to pass the page. Which will be found as a parameter in all your views
        app_routes=app_routes, # Here a list has to be passed in which we have defined app routing like app_routes
        #not_found_view:View=ViewNotFound().view # If you want that there should be a different view call when no path matches, then you can pass that view here. otherwise no need to give it it will call ViewNotFound by default
        )
    page.go(page.route)

ft.app(target=main)


```

### views/index_view.py
This is a basic python `class` whose `view` method takes `page` and `params` and returns `ft.view`.

In `page` we get the `page` passed in `path`.

In `params` we get the values ​​passed from `url` in the form of `dictionary`.

It is not necessary that the name of the method should be `view`, you can also give a different name.

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
This is a basic python `class` whose `view` method takes `page` and `params` and returns `ft.view`.

In `page` we get the `page` passed in `path`.

In `params` we get the values ​​passed from `url` in the form of `dictionary`.

It is not necessary that the name of the method should be `view`, you can also give a different name.

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