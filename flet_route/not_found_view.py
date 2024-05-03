from flet import View, Page,Text,TextButton
from .params import Params
from .basket import Basket


def ViewNotFound(page:Page,params:Params,basket:Basket):
    return View(
        "/notfound/404",
        controls=[
            Text(
                "View / Page not found error 404",
                size=30,
            ),
            TextButton(
                "Go Back OR '/' ",
                on_click=lambda _:page.go(page.views[-2].route)
            )
        ]
    )

async def ViewNotFound_async(page:Page,params:Params,basket:Basket):

    return View(
        "/notfound/404",
        controls=[
            Text(
                "View / Page not found error 404",
                size=30,
            ),
            TextButton(
                "Go Back OR '/' ",
                on_click=lambda _:page.go(page.views[-2].route)
            )
        ]
    )