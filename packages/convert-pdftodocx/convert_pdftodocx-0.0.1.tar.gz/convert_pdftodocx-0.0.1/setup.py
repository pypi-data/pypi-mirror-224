import setuptools

with open("README.md", "r") as fh:
	description = fh.read()

setuptools.setup(
	name="convert_pdftodocx",
	version="0.0.1",
	author="Volody Product Pvt Ltd",
	author_email="sd12@consultlane.com",
	packages=["convert_pdftodocx"],
	description="It will convert PDF to Docx format using pywin32 & comtypes library. Also it will extract the text & table text from docx file",
	long_description=description,
	long_description_content_type="text/markdown",
	url="https://bitbucket.org/mayurborkar1/pdf-to-docx-package/src/master/",
	license='MIT',
	python_requires='>=3.7',
	install_requires=[]
)
