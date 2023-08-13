from setuptools import setup

with open("README.md",'r') as f:
    readme=f.read()

setup(
    name='taskHandler',
    version='0.1.1',
    description='taskHandker pakage will distribute all file present in give directory',
    long_description_content_type='text/markdown', 
    long_description=readme,
    url='https://github.com/vardhannegi/taskHandler',
    author='vardhan negi',
    author_email='vardhan.negi@gmail.com',
    license='MIT ',
    packages=['taskHandler'],
    install_requires=['os','pwd'],
    classifiers=[
        'Intended Audience :: Science/Research',
        'License :: OSI Approved :: MIT License',  
        'Operating System :: POSIX :: Linux'
    ],
    python_requires='>=3.5'
)
