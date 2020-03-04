import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pysics-solidsmoke", # Replace with your own username
    version="0.01",
    author="Solid Smoke Software",
    author_email="solid.smoke.software@gmail.com",
    description="A simple 2D physics system",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/solidsmokesoftware/pysics",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.8',
)