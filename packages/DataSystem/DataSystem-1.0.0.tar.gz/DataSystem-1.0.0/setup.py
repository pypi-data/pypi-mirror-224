from setuptools import setup

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name='DataSystem',
    version='1.0.0',
    author='Sepehr0Day',
    description='A package to retrieve system information',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=['DataSystem'],
    install_requires=[
        'psutil',
        'py-cpuinfo',
        'python-dateutil',
        'GPUtil',
    ],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)
