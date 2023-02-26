from setuptools import setup, find_packages

setup(
    name='task_manager',
    version='1.0.0',
    packages=find_packages(exclude=['tests*']),
    license='MIT',
    description='Task Manager App',
    long_description=open("README.md").read(),
    url='https://github.com/CoderSthe/task-manager',
    author='Sithembiso Mdhluli',
    author_email='mdhluli269@gmail.com'
)