from setuptools import setup, find_packages

setup(
    name='onnxeditor',
    version='0.0.1',
    packages=find_packages(),
    install_requires=[
        'numpy',
        'pyside6',
        'grandalf',
    ],
    python_requires='>=3.6',
    author='oPluss',
    author_email='opluss@qq.com',
    description='A Qt base onnx editor',
    long_description='A Qt base onnx editor',
    url='https://github.com/OYCN/OnnxEditorV3',
)
