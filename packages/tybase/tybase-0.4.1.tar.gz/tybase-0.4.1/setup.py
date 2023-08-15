from setuptools import setup, find_packages

setup(
    name='tybase',
    version='0.4.1',
    include_package_data=True,
    description='synthesize_video 修改了这个方法,加了几个参数,可以尝试用-crf=23的方式来对比最终的生成质量',
    long_description=open('README.md', 'r', encoding='utf-8').read(),
    long_description_content_type='text/markdown',  # 版本描述
    author='Tuya',
    author_email='353335447@qq.com',
    url='https://github.com/yourusername/your_package',
    packages=find_packages(),
    install_requires=[
        'setuptools',
        "opencv-python",
        "loguru",
        "openpyxl",
        'requests',
        "python-dotenv",
        "retrying",
        "pymysql",
        "mysql-connector-python",
        "sqlalchemy",
        "pandas",
        "langchain",
        "openai",
        'python-dotenv',
        "oss2"
        ""

        # List your package dependencies here
    ],
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.10',
    ],
)
