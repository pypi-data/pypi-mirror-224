from setuptools import setup, find_packages

setup(
    name='shwj',
    version='0.2.2',
    author='shwj',
    author_email='2591091196@email.com',
    description='a simple package for convenience',
    long_description='Please refer to README.md for details.',
    long_description_content_type='text/markdown',
    url='https://space.bilibili.com/175512552',
    packages=find_packages(),
    install_requires=[
        'numpy>=1.18.0',
        # Your package dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        # Add more classifiers as needed
    ],
)
