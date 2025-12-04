from setuptools import setup, find_packages

setup(
    name='ossimg',               # 라이브러리 이름 (import 할 때 쓰는 이름 아님, 설치 이름임)
    version='1.0.0',             # 버전
    description='Image Preprocessing Library',
    author='OSS Team',           # 팀 이름
    packages=find_packages(),    # 폴더들(ossimg)을 자동으로 찾아서 포함시킴
    install_requires=[           # 이 라이브러리를 깔 때 같이 깔아야 할 것들
        'Pillow',
    ],
    python_requires='>=3.6',
)