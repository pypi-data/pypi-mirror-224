import setuptools

setuptools.setup(
    name="monita_icons",
    py_modules=["monita_icons"],
    data_files={"vendor_map.json": ["./vendor_map.json"]},
    #include_package_data=True,
    version="0.2.12",
)
