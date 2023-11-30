from setuptools import setup, find_packages

VERSION = '1.1.1'
DESCRIPTION = 'Image-based Malware Dataloader'
LONG_DESCRIPTION = 'A PyTorch dataloader implementation for various image-based malware datasets.'

# Setting up
setup(
    # the name must match the folder name 'image_based_malware_dataloader'
    name="image_based_malware_dataloader",
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
        "Programming Language :: Python :: 3",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: Microsoft :: Windows",
    ]
)