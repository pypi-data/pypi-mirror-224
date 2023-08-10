from setuptools import setup
import sys

if sys.version_info[:2] < (3, 9):
    raise RuntimeError("Python versão >= 3.9 obrigatória.")
# Leitura do arquivo README.md
with open("README.md", "r", encoding="utf-8") as file:
    long_description = file.read()

# Configuração do pacote
setup(
    name='progbr',
    version='0.3.3',
    license='MIT',
    author=['Bidjory'],
    author_email='anybosoft@gmail.com',
    maintainer='Samuel Bidjory',
    description='Uma biblioteca para facilitar sua jornada em matemática',
    long_description=long_description,
    long_description_content_type='text/markdown',
    packages=[''],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'scipy',
        'numpy',
        'sympy',
        'mpmath',
        'matplotlib',
        'cryptography',
        'pyotp',
        'opencv-python',
    ],
    python_requires='>=3.6',
    
)
