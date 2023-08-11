import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="todolist-JIANG.CHENG",
    version="0.0.1",
    author="jiang.cheng",
    author_email="jiangcheng1806@gmail.com",
    description="a simple project to save to do stuff",
    long_description_content_type="markdown",
    url="https://github.com/skyjiangcheng/todolist-JIANG",
    include_package_data=True,
    package_data={'todo_pkg': ['template/*.tpl','data/todo.db']},
    packages=setuptools.find_packages(),
    classifiers=["Programming Language :: Python :: 3",
                 "License :: OSI Approved :: MIT License",
                 "Operating System :: OS Independent",],
    python_requires='>3.6'
)