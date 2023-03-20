import setuptools

setuptools.setup(
    name="circle_packing_chart",
    version="0.0.2",
    author="shubhra",
    author_email="",
    description="Generate interactive nested circle packing chart",
    long_description="",
    long_description_content_type="text/plain",
    url="",
    packages=setuptools.find_packages(),
    include_package_data=True,
    classifiers=[],
    python_requires=">=3.6",
    install_requires=[
        # By definition, a Custom Component depends on Streamlit.
        # If your component has other Python dependencies, list
        # them here.
        "streamlit >= 0.63",
    ],
)
