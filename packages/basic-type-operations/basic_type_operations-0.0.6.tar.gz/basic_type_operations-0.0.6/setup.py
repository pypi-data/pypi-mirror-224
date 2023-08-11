from setuptools import setup, find_packages

version = '0.0.6'  # Any format you want
DESCRIPTION = 'Easily cut the basic type by basic_type_operations'

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    # 要显示的唯一标识（用于pip install xxx）
    name='basic_type_operations',
    # 使用find_packages()自动发现项目中的所有包,如果不想使用所有的包，那么可以手动指定例如：packages=[‘package1’, ‘package2’, ‘package3’]
    packages=find_packages(),
    version=version,  # 版本号
    description='Short description',  # '简单描述'
    long_description_content_type="text/markdown",  # 长描述内容的类型设置为markdown
    long_description=long_description,  ## 长描述设置为README.md的内容
    author="SkyOceanChen",  # 作者
    author_email="skyoceanchen@foxmail.com",  # 作者的电子邮件
    url='https://gitee.com/SkyOceanchen/basic_type_operations.git',
    keywords=['basic_type', 'python', "str", "list", "numpy", "number", "datetime", "time", 'calendar'],
    # 许可协议
    license='MIT',
    # 要安装的依赖包
    install_requires=[
        # All external pip packages you are importing
        'numpy',
        'munch',
        'fuzzywuzzy',
        'python-Levenshtein',
        'pinyin',
        'djangorestframework',
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'Operating System :: OS Independent',
        'Topic :: Software Development :: Build Tools',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.10',
    ],
)
"""
python setup.py bdist_wheel sdist
twine upload dist/*
SkyOceanChen/CHENziqing527#
"""
