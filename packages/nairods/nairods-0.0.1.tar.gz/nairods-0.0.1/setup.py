import setuptools

with open('README.md', 'r',encoding='utf-8') as f:
    long_description = f.read()

setuptools.setup(
    name='nairods',
    version='0.0.1',
    author='nairods',
    author_email='1069461929@qq.com',
    description='py3 tools',
    long_description=long_description,
    long_description_content_type="text/markdown",
    url='https://gitee.com/wuhaohaohao/nairods.git',
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)
