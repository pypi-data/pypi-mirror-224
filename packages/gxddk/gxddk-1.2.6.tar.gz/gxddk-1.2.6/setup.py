"""
Documentation
-------------
to be continue

"""

from setuptools import setup, find_packages

long_description = __doc__

def main():
    setup(
        name="gxddk",
        description="sphinx doc build",
        keywords="sphinx doc",
        long_description=long_description,
        version="1.2.6",
        author="zhaobk",
        author_email="zhaobk@nationalchip.com",
        packages=find_packages(),
        include_package_data=True,
        data_files=[
            ('scripts/_templates', [
                'gxddk/scripts/_templates/layout.html',
                'gxddk/scripts/_templates/search.html',
                ]),
            ('scripts/_static', [
                'gxddk/scripts/_static/style.css',
                ]),
            ('scripts/_ext', [
                'gxddk/scripts/_ext/genmodule.py',
                'gxddk/scripts/_ext/retex.py',
                'gxddk/scripts/_ext/rst_table.py',
                ]),
            ('scripts', [
                'gxddk/scripts/envexec',
                ]),
            ],
        entry_points={
            'console_scripts':[
                'gxddkbuild=gxddk.gxddkbuild:run',
                ]
            }
    )


if __name__ == "__main__":
    main()
