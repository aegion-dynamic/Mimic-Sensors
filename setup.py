from setuptools import setup, find_packages

setup(
    name="mimic-sensors",
    version="1.0.0",
    packages=find_packages(),
    install_requires=[
        "mimic-fw",
    ],
    author="Antigravity",
    description="Sensor simulation modules for the Mimic Framework",
    python_requires='>=3.6',
)
