from setuptools import setup, find_packages
setup(
    name='django-dc-iplogger',  # Update with your package name
   version='0.3.0',  # Update with the appropriate version
    packages=find_packages(),
    install_requires=[
        'Django',
    ],
    classifiers=[
        # ... (other classifiers)
        "License :: OSI Approved :: MIT License",
    ],
    python_requires='>=3.6',
    long_description=open('README.md').read(),  # Include README content
    license='MIT',  # Specify the license
)
