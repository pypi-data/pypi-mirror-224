from setuptools import find_packages, setup

setup(
    name="umar-py",
    version="0.0.4",
    description="Helper library.",
    url="https://github.com/umarriqbal/umar-py",
    author="Umar",
    author_email="umarrdev@gmail.com",
    classifiers=[
        "Development Status :: 1 - Planning",
        "Programming Language :: Python :: 3.10",
    ],
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    zip_safe=False,
    python_requires=">=3.10"
)
