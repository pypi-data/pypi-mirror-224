# from setuptools import setup, find_packages
# import os

# VERSION = '0.0.1'
# DESCRIPTION = "wenzd's 2nd version."

# setup(
#     name="roleft",
#     version=VERSION,
#     author="wenzd",
#     author_email="october731@163.com",
#     description=DESCRIPTION,
#     long_description_content_type="text/markdown",
#     long_description=open('README.md',encoding="UTF8").read(),
#     packages=find_packages(),
#     install_requires=['moviepy'],
#     keywords=['roleft', 'utility'],


#     data_files=[('cut_video', ['cut_video/clip_to_erase.json'])],
#     entry_points={
#     'console_scripts': [
#         'cut_video = cut_video.main:main'
#     ]
#     },
#     license="MIT",
#     url="https://roleft.com",
#     scripts=['cut_video/cut_video.py'],
#     classifiers= [
#         "Development Status :: 3 - Alpha",
#         "Intended Audience :: Developers",
#         "Programming Language :: Python :: 3",
#         "Operating System :: Microsoft :: Windows"
#     ]
# )