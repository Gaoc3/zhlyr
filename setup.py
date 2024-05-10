from setuptools import setup , find_packages

setup(
    name = 'zhlyr',
    version = '3.5',
    packages = find_packages(),
    requires = ['requests','shazamio','shazam'],
    long_description ='**A python package to get lyrics from music , serialize data from json response and recognize data from musics**',
    long_description_content_type='text/markdown',
    description = 'Python library for music handling',
    author = 'Mtsky',
    author_email = 'secon2636@gmail.com',
    url = 'https://github.com/Gaoc3/zhlyr',
    license = 'MIT',
    classifiers=[
        "Development Status :: 1 - Planning",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3",
        "Operating System :: Unix",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ],
    keywords= ['lyrics','music','shazam','serialize','serializer','recognize'],
    python_requires=">=3.9"
)