import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

with open("requirements.txt", "r", encoding="utf8") as f:
    requires = f.read()

setuptools.setup(
    name='coo-img-sorter',
    version='0.0.1',
    license="MIT",
    author="xcenweb",
    author_email="xcenweb@qq.com",
    url="https://github.com/xcenweb/coo-img-sorter",

    description="多种图片分类工具脚手架",
    long_description=long_description,
    long_description_content_type="text/markdown",

    packages=[
        "coo_imgSorter",
        "coo_imgSorter.util",
    ],

    python_requires=">=3.8",
    install_requires=requires.splitlines(),
)