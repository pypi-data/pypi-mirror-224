import setuptools

with open('README.md', 'r', encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='djangolin',
    author='Hydra',
    author_email='navidsoleymani@ymail.com',
    description='A logger to log everything that starts with a request and ends with a response.',
    keywords='logger, django',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/navidsoleymani/pangolin.git',
    project_urls={
        'Documentation': 'https://github.com/navidsoleymani/pangolin.git',
        'Bug Reports':
            'https://github.com/navidsoleymani/pangolin.git/issues',
        'Source Code': 'https://github.com/navidsoleymani/pangolin.git',
    },
    package_dir={'': 'src'},
    packages=setuptools.find_packages(where='src'),
    classifiers=[
        'Framework :: Django :: 4.2',
        'Development Status :: 5 - Production/Stable',

        'Intended Audience :: Developers',
        'Topic :: Software Development :: Build Tools',

        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3 :: Only',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.8',
    install_requires=[
        'Django',
        'django-user-agents',
        'djangorestframework',
        'python-dotenv',
        'scrapeasy',
    ],
)
