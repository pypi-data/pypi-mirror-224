from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="hzexcel",
    version="0.0.12",
    author="汉卓软件",
    author_email="1739951529@example.com",
    description="提供了一个根据参数配置，通用的导入和导出excel文件功能",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/your-username/your-package-repo",
    packages=find_packages(),
    # packages=["your_package"],
    install_requires=[
        "openpyxl==3.0.0",
        "pandas~=1.1.5",
        "django",
    ],
)
