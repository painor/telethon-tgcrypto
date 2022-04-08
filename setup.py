import setuptools

setuptools.setup(
    name='telethon-cryptg',
    version='0.0.4',
    description='telethon bindings for the tgcrypto module',
    long_description=open('README.rst').read().strip(),
    author='Painor',
    author_email='pi.oussama@gmail.com',
    url='https://github.com/painor/telethon-tgcrypto',
    packages=setuptools.find_packages(),
    install_requires=['tgcrypto'],
    license='MIT License',
    keywords='telethon tgcrypto',
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
    ],
    python_requires='>=3.7',
)
