import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="qiskit_quantier",
    version="0.6.0",
    description="A quantum provider for Qiskit",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=["qiskit_quantier"],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        "qiskit",
        "qiskit-aer"
    ],
    python_requires='>=3.6',
    include_package_data=True,
)