from setuptools import setup, find_packages

setup(
    name='django-mimicry',
    version='1.6',
    packages=find_packages(exclude=['djangoMimicryProject']),
    include_package_data=True,
    license='MIT License',
    description='A Django app to simulate user sessions.',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/YidiSprei/djangoMimicry.git',
    author='Yidi Sprei',
    author_email='yidi.sprei@infuzu.com',
    classifiers=[
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3',
        'Topic :: Internet :: WWW/HTTP',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    ],
)
