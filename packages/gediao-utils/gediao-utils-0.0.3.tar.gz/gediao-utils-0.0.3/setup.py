from setuptools import setup
from setuptools import find_packages
import os
# import gediaoutils
# https://zhuanlan.zhihu.com/p/115302375
VERSION = '0.0.3'
##清空之前的包
build_path = './dist'
# if os.path.exists(build_path):
#     files = os.listdir(build_path)
#     for file in files:
#         os.remove(build_path+'/'+file)
#     os.removedirs(build_path)

with open('readme.md',encoding='utf-8') as f:
    LONG_DESCRIPTION = f.read()

setup(
    name='gediao-utils',  # package name
    version=VERSION,  # package version
    description='xuxy utils package',  # package description
    packages=find_packages(),
    author="色调呀",
    author_email="1059738716@qq.com",
    url="https://gitee.com/ukihi/gediao-open-python-utils",
    long_description=LONG_DESCRIPTION,
    long_description_content_type='text/markdown',
    zip_safe=False,
    package_data={
        # 引入任何包下面的 *.txt、*.rst 文件
        "": ["*.txt", "*.rst"],
        # 引入 hello 包下面的 *.msg 文件
        # "hello": ["*.msg"],
    },
    # install_requires=[
    #     "Werkzeug>=0.15",
    #     "Jinja2>=2.10.1",
    #     "itsdangerous>=0.24",
    #     "click>=5.1",
    # ],
)

