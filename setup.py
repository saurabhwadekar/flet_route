from setuptools import setup

from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name = "flet_route",
    version = "0.3.1",
    author="Saurabh Wadekar [ INDIA ]",
    packages=["flet_route","cli"],
    license="MIT",
    maintainer="Saurabh Wadekar",
    maintainer_email="saurabhwadekar420@gmail.com",
    keywords=["flet","routing","flet_route","routes","flet app","flet-route","flet simple routing"],
    description="This makes it easy to manage multiple views with dynamic routing.",
    long_description=long_description,
    long_description_content_type='text/markdown',
    url="https://github.com/saurabhwadekar/flet_route",
    include_package_data=True,
    install_requires=[
        'click==8.1.3',
        "repath",
        "flet",
    ],
    entry_points= {
        'console_scripts': 
        ['flet-route=cli:make_app']
    }, 
)