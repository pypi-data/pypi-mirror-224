from setuptools import setup, find_packages

setup(
    name='fork-django-streaming',
    packages=find_packages(exclude=['tests*']),
    include_package_data=True,
    version='0.2.0',
    license='GNU',
    description='video streaming based on Django',
    author='Jed',
    author_email='adijed3@gmail.com',
    url='https://github.com/J3dd4/fork-django-streaming',
    download_url='https://github.com/sageteam-org/django-sage-streaming/archive/refs/tags/0.1.0.tar.gz',
    keywords=['django', 'python', 'streaming', 'video streaming'],
    install_requires=[
        'Django',
        'djangorestframework'
    ],
    setup_requires=['wheel']
)
