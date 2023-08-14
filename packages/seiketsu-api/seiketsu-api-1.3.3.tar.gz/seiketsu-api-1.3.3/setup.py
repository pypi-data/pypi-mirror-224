from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name='seiketsu-api',
    long_description=long_description,
    long_description_content_type="text/markdown",
    version='1.3.3',
    description='A Python library to interact with a chat API',
    author='LoLip_p',
    author_email='mr.timon51@gmail.com',
    url='https://github.com/yourusername/my-json-package',
    packages=find_packages(),
    include_package_data=True,
    package_data={
        "api_seiketsu": ["data/*.json"],
    },
    install_requires=[
        # Add any dependencies required for your package here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
