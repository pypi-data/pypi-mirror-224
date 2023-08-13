from setuptools import setup, find_packages

classifiers = [
    'Development Status :: 5 - Production/Stable',
    'Intended Audience :: Education',
    'Operating System :: POSIX :: Linux',
    'License :: OSI Approved :: MIT License',
    'Programming Language :: Python :: 3'
]

setup(
    name = 'stylish_vk_api',
    version = '0.0.1',
    description = 'Emulation of user actions in Vk',
    long_description = open('README.txt').read() + '\n\n' + open('CHANGELOG.txt').read(),
    url = '',
    author = 'Vadim',
    author_email = 'fancybear@internet.ru',
    license = 'MIT',
    classifiers = classifiers,
    keywords = 'vk',
    packages = find_packages(),
    install_requires = ['requests', 'vk_api', 'dotenv']
)
