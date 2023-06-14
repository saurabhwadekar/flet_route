from flet import View, Page,Text,TextButton
# import asyncio


def ViewNotFound(page:Page,params,basket):
    return View(
        "/notfound/404",
        controls=[
            Text(
                "View / Page not found error 404",
                size=30,
            ),
            TextButton(
                "Go Back OR '/' ",
                on_click=lambda e:page.go(page.views[-2].route)
            )
        ]
    )

async def ViewNotFound_async(page:Page,params,basket):

    async def go_back(e):
        await page.go_async(page.views[-2].route)

    return View(
        "/notfound/404",
        controls=[
            Text(
                "View / Page not found error 404",
                size=30,
            ),
            TextButton(
                "Go Back OR '/' ",
                on_click=go_back
            )
        ]
    )