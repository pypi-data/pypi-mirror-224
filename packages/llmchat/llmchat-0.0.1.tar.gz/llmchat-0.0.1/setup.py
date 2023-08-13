from setuptools import setup, find_packages 
import codecs
import os 

name='llmchat'

def read(*parts):
    here = os.path.abspath(os.path.dirname(__file__))
    return codecs.open(os.path.join(here, *parts), "r",encoding='utf-8').read()


def get_version(): 
    version_file = name + '/version.py'
    with open(version_file, 'r', encoding='utf-8') as f:
        exec(compile(f.read(), version_file, 'exec'))
    return locals()['__version__']
    '''
    return '0.0.1'
    '''

setup(
    name=name,
    version=get_version(),
    description="大语言模型仿openai接口实现",
    author='zhys513',#作者
    packages=find_packages(),
    author_email="254851907@qq.com",
    url="https://gitee.com/zhys513/llmchat",
    python_requires='>=3.6', 
    install_requires=['torch','transformers','asyncio','dataclasses','pydantic','loguru'],
)

