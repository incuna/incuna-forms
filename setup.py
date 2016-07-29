from setuptools import find_packages, setup


setup(
    version='0.1.0',
    name='incuna-forms',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'django-crispy-forms==1.6.0',
    ],
    description='TODO',
    author='Incuna Ltd',
    author_email='admin@incuna.com',
    url='https://github.com/incuna/incuna-forms',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Programming Language :: Python :: 3.5',
        'Topic :: Software Development',
        'Topic :: Utilities',
    ],
)
