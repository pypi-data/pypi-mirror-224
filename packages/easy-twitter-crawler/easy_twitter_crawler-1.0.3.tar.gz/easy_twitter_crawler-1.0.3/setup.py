from setuptools import setup, find_packages

setup(
    name='easy_twitter_crawler',
    version='1.0.03',
    packages=find_packages(),
    license='MIT',
    author='hanxinkong',
    author_email='xinkonghan@gmail.com',
    description='简易、强大的推特（Twitter）采集程序,支持用户,发文,评论等采集',
    long_description=open('README.md', encoding='utf-8').read(),
    long_description_content_type="text/markdown",
    install_requires=[
        # List your package's dependencies here
        "easy_spider_tool>=1.0.7",
        "loguru>=0.7.0",
        "my_fake_useragent>=0.2.1",
        "requests>=2.27.1",
        "requests_html>=0.10.0",
        "urllib3>=1.26.15"
    ],
)
