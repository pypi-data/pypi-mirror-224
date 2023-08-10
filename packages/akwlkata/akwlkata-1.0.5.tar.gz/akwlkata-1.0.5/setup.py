# coding=utf-8

"""
    @header setup.py
    @abstract   
    
    @MyBlog: http://www.kuture.com.cn
    @author  Created by Kuture on 2020/9/22
    @version 0.1.2 2020/9/22 Creation()
    @e-mail austinkuture@126.com
    
    @Copyright © 2020年 Mr.Li All rights reserved
"""

from setuptools import setup, find_packages

setup(
    name="akwlkata",
    version="1.0.5",
    keywords=("pip", "akwlkata", "wlkata", "wlkatarobot", "kuture", "robot"),
    description="wlkata robot driver",
    long_description="开塔机械臂驱动，兼容ubuntu与mac OS，优化控制流程",
    license="MIT Licence",

    url="",
    author="Kuture",
    author_email="kuture@163.com",

    packages=find_packages(),
    include_package_data=False,
    platforms="any",
    install_requires=['pyserial']
)
