from setuptools import setup, find_packages

setup(
    name='easy_twitter_interactors',
    version='1.0.00',
    packages=find_packages(),
    license='MIT',
    author='hanxinkong',
    author_email='xinkonghan@gmail.com',
    description='简易、好用的推特点赞，刷阅读量程序',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        # List your package's dependencies here
        "easy_spider_tool>=1.0.7",
        "loguru>=0.7.0",
        "requests>=2.27.1",
        "urllib3>=1.26.15",
    ],
)
