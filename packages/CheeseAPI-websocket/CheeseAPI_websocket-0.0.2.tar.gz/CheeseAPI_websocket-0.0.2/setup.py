import setuptools

with open('./README.md', 'r', encoding = 'utf-8') as f:
    longDescription = f.read()

setuptools.setup(
    name = 'CheeseAPI_websocket',
    version = '0.0.2',
    author = 'Cheese Unknown',
    author_email = 'cheese@cheese.ren',
    description = '基于CheeseAPI的升级版websocket',
    long_description = longDescription,
    long_description_content_type = 'text/markdown',
    url = 'https://github.com/CheeseUnknown/CheeseAPI_websocket',
    license = 'MIT',
    classifiers = [
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.11'
    ],
    keywords = 'CheeseAPI websocket redis',
    python_requires = '>=3.11',
    install_requires = [
        'CheeseAPI',
        'redis',
        'CheeseType',
        'CheeseLog'
    ],
    packages = setuptools.find_packages()
)
