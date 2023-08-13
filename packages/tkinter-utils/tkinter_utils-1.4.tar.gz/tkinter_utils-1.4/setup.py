import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
	long_description = fh.read()

setuptools.setup(
	name="tkinter_utils",
	version="1.4",
	description="简单的tkinter包装库，可以快速地创建小型桌面应用。",
	long_description=long_description,
	long_description_content_type="text/markdown",
	packages=setuptools.find_packages(),
	license="MIT Licence"
)
