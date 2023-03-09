from flet import View, Page,Text,TextButton



def ViewNotFound(page:Page,params):
    return View(
        "/notfound/404",
        controls=[
            Text(
                "page not found error 404",
                size=30,
            ),
            TextButton(
                "Go Back OR '/' ",
                on_click=lambda e:page.go(page.views[-2].route)
            )
        ]
    )