import setuptools
import discat

setuptools.setup(
	name="discat",
	version=discat.__version__,
	author="RixTheTyrunt",
	author_email=discat.__author__,
	description=discat.__description__,
	packages=["discat"],
	python_requires=">=3",
	long_description=open("README.md").read(),
	long_description_content_type="text/markdown",
	install_requires=["websocket-client"]
)