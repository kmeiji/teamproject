# 🎨 OSSIMG: Image Preprocessing Library

![Python](https://img.shields.io/badge/Python-3.8%2B-blue?style=flat-square&logo=python)
![License](https://img.shields.io/badge/License-MIT-green?style=flat-square)
![Version](https://img.shields.io/badge/Version-1.0.0-orange?style=flat-square)
![PRs](https://img.shields.io/badge/PRs-Welcome-brightgreen?style=flat-square)

> **2025 AI Practice (OSS) Final Project** > 데이터 전처리(Image Preprocessing)를 위한 오픈소스 파이썬 라이브러리입니다. 복잡한 OpenCV 코드를 몰라도, 단 한 줄의 코드로 이미지를 변환할 수 있습니다.

---

## ✨ Features (주요 기능)

이 라이브러리는 이미지 처리를 위한 7가지 핵심 기능을 제공합니다.

| 기능 (Function) | 설명 (Description) | 비고 |
| :--- | :--- | :--- |
| **Grayscale** | 이미지를 흑백(Grayscale)으로 변환합니다. | 데이터 경량화 |
| **Sepia** | 빈티지한 감성의 세피아 톤 필터를 적용합니다. | 필터 효과 |
| **Resize** | 이미지 화질 저하를 최소화하며 크기를 조절합니다. | LANCZOS 알고리즘 |
| **Mosaic** | 개인정보 보호를 위해 이미지를 모자이크 처리합니다. | Privacy 보호 |
| **Sketch** | 이미지의 윤곽선을 추출하여 스케치 효과를 냅니다. | Edge Detection |
| **Enhance_image** | 이미지의 밝기와 대비를 조절해 더 선명하게 보정합니다. | Brightness & Contrast Adjustment |
| **Watermark** | 이미지 위에 텍스트를 반투명하게 삽입합니다. | 저작권 보호 / Branding |
| **Rotate** | 이미지를 원하는 각도로 회전합니다. | Image Rotation |

---

## 🚀 Installation (설치 방법)

이 프로젝트를 로컬 환경에서 실행하려면 아래 명령어를 순서대로 입력하세요.

```bash
# 1. 저장소 복제 (Clone Repository)
git clone [https://github.com/kmeiji/teamproject.git](https://github.com/kmeiji/teamproject.git)

# 2. 프로젝트 폴더로 이동
cd teamproject

# 3. 필수 라이브러리 설치 (Pillow)
pip install -r requirements.txt


💻 Usage (사용법)
OSSIMG는 매우 직관적인 API를 제공합니다. import 후 바로 함수를 호출하여 사용할 수 있습니다.

1. 기본 필터 사용 (Basic Filters)
from ossimg import grayscale, sepia, sketch

# 1. 흑백 변환 (Grayscale)
# 사용법: grayscale(원본경로, 저장경로)
grayscale("cat.jpg", "cat_gray.jpg")

# 2. 세피아 필터 (Sepia)
sepia("cat.jpg", "cat_sepia.jpg")

# 3. 스케치 효과 (Sketch)
sketch("cat.jpg", "cat_sketch.jpg")


2. 고급 기능 사용 (Advanced Features)
from ossimg import resize, mosaic

# 4. 크기 조절 (Resize)
# 사용법: resize(원본경로, 저장경로, 가로px, 세로px)
resize("dog.jpg", "dog_small.jpg", 300, 300)

# 5. 모자이크 (Mosaic)
# 사용법: mosaic(원본경로, 저장경로, 픽셀크기)
# pixel_size가 클수록 모자이크가 굵게 처리됩니다 (기본값: 10)
mosaic("face.jpg", "face_hidden.jpg", pixel_size=20)



✔️ 사용 예
from ossimg.proc import sepia
img = sepia("cat.jpg")
img.save("out1.jpg")

from ossimg.proc import rotate
img = rotate("cat.jpg", 45)
img.save("out2.jpg")




📂 Project Structure (폴더 구조)
오픈소스 표준 구조를 준수합니다.

project-root/
├── ossimg/              # Source Code Package
│   ├── __init__.py      # Package Initialization (Easy Import)
│   └── proc.py          # Core Logic Implementation
├── .gitignore           # Git Ignore Configuration
├── README.md            # Project Documentation
└── requirements.txt     # Dependency List


🤝 Contribution (협업 방식)
이 프로젝트는 Gitflow Workflow를 따릅니다. 기여를 원하시는 분은 아래 절차를 준수해주세요.

1.Issue 생성: 구현할 기능이나 버그를 이슈 탭에 등록합니다.

2.Branch 생성: feature/기능명 브랜치를 생성합니다. (ex: feature/add-mosaic)

3.Develop: 코드를 작성하고 커밋합니다.

4.Pull Request: main 브랜치로 PR을 보냅니다.

5.Code Review: 팀원의 리뷰 후 Merge 합니다.


📜 License
This project is licensed under the MIT License. Copyright (c) 2025 Hanyang Univ. ERICA OSS Team.
