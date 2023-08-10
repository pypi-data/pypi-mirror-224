import setuptools

setuptools.setup(
    name="monita_icons",                     # This is the name of the package
    py_modules=["monita_icons"],             # Name of the python package
    package_data={'monita_icons': ['./vendor_map.json']},
    version="0.2.6",                        # The initial release version
)
