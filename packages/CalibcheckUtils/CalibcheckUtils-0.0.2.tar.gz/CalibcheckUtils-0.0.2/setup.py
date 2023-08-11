from setuptools import setup
from setuptools import find_packages


VERSION = '0.0.2'
with open("README.rst", "r") as f:
  long_description = f.read()
setup(
    name='CalibcheckUtils',  # package name
    version=VERSION,  # package version
    keywords = ["pip", "CalibcheckUtils"],
    description='The config is used for calib check',  # package description
    long_description=long_description,
    packages=find_packages(),
    zip_safe=False,
    license = "Apache Licence 2.0",		# 许可证

    url = "https://github.com/ChenXuhuaX/autolabelpipline.git",     #项目相关文件地址，一般是github项目地址即可
    author = "xuhua.chen",			# 作者
    author_email = "xuhua_chen@qq.com",
    include_package_data = True,
    platforms = "any",
    install_requires = ["numpy"]  ,
    classifiers=[
          'Intended Audience :: Developers',
          'Operating System :: OS Independent',
          'Natural Language :: Chinese (Simplified)',
          'Programming Language :: Python',
          'Programming Language :: Python :: 3',
          'Programming Language :: Python :: 3.5',
          'Programming Language :: Python :: 3.6',
          'Programming Language :: Python :: 3.7',
          'Programming Language :: Python :: 3.8',
          'Programming Language :: Python :: 3.9',
          'Topic :: Software Development :: Libraries'
      ],
)