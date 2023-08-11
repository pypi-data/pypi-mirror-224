from setuptools import setup, find_packages

setup(
    name="hangpt_cpp",
    version="0.1",  
    packages=find_packages(),
    install_requires=[
        "uuid",
        "ctranslate2",
        "sentencepiece",
        "urlextract",
        "diskcache",
        "numpy",
        "pandas",
        "sqlalchemy",
        "finetuner",
        "anyio",
        "starlette",
        "fastapi",
        "pydantic",
        "sse_starlette",
        "uvicorn"
    ],
    author="Your Name",  # 여기에는 귀하의 이름을 입력하세요.
    author_email="your.email@example.com",  # 여기에는 귀하의 이메일 주소를 입력하세요.
    description="A brief description of hangpt_cpp",  # 귀하의 라이브러리에 대한 간단한 설명을 입력하세요.
    url="https://github.com/yourusername/hangpt_cpp",  # 귀하의 라이브러리 GitHub URL을 입력하세요.
    classifiers=[
        "License :: OSI Approved :: MIT License",  # 귀하의 라이센스에 맞게 변경하세요.
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
    ],
)
