from setuptools import setup, find_packages

setup(
    name="hcaptcha-solver",
    version="0.2.8",
    packages=find_packages(),
    include_package_data=True,
    package_data={"hcaptcha_solver": ["models/*"]},
    # ... other setup configurations
)
