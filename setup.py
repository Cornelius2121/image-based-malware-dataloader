from setuptools import setup, find_packages

VERSION = '0.0.3'
DESCRIPTION = 'Image-based Malware Dataloader'
LONG_DESCRIPTION = 'Data loader framework for image-based malware datasets'

# Setting up
setup(
    # the name must match the folder name 'image-based-malware-dataloader'
    name="image-based-malware-dataloader",
    version=VERSION,
    author="Cornelius Paardekooper",
    author_email="cornelius.paardekooper@uon.edu.au",
    description=DESCRIPTION,
    url='https://github.com/Cornelius2121/image-based-malware-dataloader',
    long_description=LONG_DESCRIPTION,
    packages=find_packages(),
    install_requires=[
        'numpy',
        'torch',
        'scikit-learn',
        'pillow'
    ],

    keywords=['python', 'dataloader', 'image-based malware'],
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Science/Research",
        "Programming Language :: Python :: 2",
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)