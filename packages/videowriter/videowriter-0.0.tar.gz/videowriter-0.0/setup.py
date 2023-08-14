from setuptools import setup, find_packages


with open('/home/alien/Cvwriter/Readme.md', 'r', encoding='utf-8') as f:
    long_description = f.read()
setup(
    name='videowriter',
    version='0.0',
    packages=find_packages(),
    install_requires=[
        'opencv-python'
    ],
    long_description=long_description,
    long_description_content_type='text/markdown',  # Specify the content type as Markdown
)
