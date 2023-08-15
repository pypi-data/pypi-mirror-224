from setuptools import setup

with open('README.md') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='show_gpu_usage',
    version='0.2',
    description='A library to show GPU usage in a terminal',
    url='https://github.com/your-username/your-library-name',
    author='StudyingLover',
    author_email='studyinglover1@gmail.com',
    license='MIT',
    packages=['show_gpu_usage'],
    install_requires=[
        'asciichartpy==1.5.25'
    ],
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
    ],
)