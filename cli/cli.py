import click,os
from .contents import MAIN,ROUTES,INDEX_VIEW,NEXT_VIEW,APP_BASED_MIDDLEWARE,URL_BASED_MIDDLEWARE


@click.option('-ac',default="N",prompt='Do you want to create async app ? [Y/N] ')
@click.option('-c',default="N",prompt='Do you want class based app ? [Y/N] ')
@click.option('-appname',prompt='App Name')
@click.command()
def init(appname,c,ac):
    print(appname)
    print(c)
    print(ac)
    # create dir's
    dirs = [appname,f"{appname}/views",f"{appname}/components",f"{appname}/middlewares"]
    for i in dirs:
        os.mkdir(i)

    # create files
    files_and_content = [
        #./
        [f"{appname}/main.py",MAIN],
        [f"{appname}/routes.py",ROUTES],
        #./views
        [f"{appname}/views/__init__.py",""],
        [f"{appname}/views/index_view.py",INDEX_VIEW],
        [f"{appname}/views/next_view.py",NEXT_VIEW],
        #./middlewares
        [f"{appname}/middlewares/__init__.py",""],
        [f"{appname}/middlewares/app_middleware.py",APP_BASED_MIDDLEWARE],
        [f"{appname}/middlewares/url_middleware.py",URL_BASED_MIDDLEWARE],
        #./components
        [f"{appname}/components/__init__.py",""],
    ]

    for i in files_and_content:
        with open(i[0],"w") as f:
            f.write(i[1])
    


@click.group()
def make_app():
    pass

make_app.add_command(init)

# if __name__ == '__main__':
#     make_app()