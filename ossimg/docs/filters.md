# Image Filter API Documentation

이 문서는 이미지 필터 라이브러리의 각 함수와 사용 방법을 설명합니다.

---

## 1. grayscale(input, output)

### 설명  
이미지를 흑백(grayscale)으로 변환합니다.

### Args
- `input (str | PIL.Image)` : 입력 이미지 경로 또는 PIL 이미지 객체  
- `output (str)` : 저장할 파일 경로

### Returns
- 없음 (결과는 파일로 저장)

### Example
```python
from ossimg.proc import grayscale

grayscale("cat.jpg", "result_gray.jpg")
```

---

## 2. sepia(input, output)

### 설명  
이미지에 세피아 필터를 적용합니다.

### Args
- `input (str | PIL.Image)`
- `output (str)`

### Returns
- 없음 (파일 저장)

### Example
```python
from ossimg.proc import sepia

sepia("cat.jpg", "result_sepia.jpg")
```

---

## 3. resize(input, output, width, height)

### 설명  
이미지를 지정한 크기로 리사이즈합니다.

### Args
- `input (str | PIL.Image)`
- `output (str)`
- `width (int)` : 가로 픽셀 수
- `height (int)` : 세로 픽셀 수

### Returns
- 없음 (파일 저장)

### Example
```python
from ossimg.proc import resize

resize("cat.jpg", "result_resize.jpg", 10, 10)
```

---

## 4. mosaic(input, output, ratio)

### 설명  
이미지의 픽셀들을 덩어리 단위로 합쳐 모자이크 효과를 만듭니다.

### Args
- `input (str | PIL.Image)`
- `output (str)`
- `ratio (float)` : 모자이크 블록 크기 비율 (0.1 추천)

### Returns
- 없음

### Example
```python
from ossimg.proc import mosaic

mosaic("cat.jpg", "result_mosaic.jpg", ratio=0.1)
```

---

## 5. sketch(input, output)

### 설명  
이미지를 연필 스케치 스타일로 변환합니다.

### Args
- `input (str | PIL.Image)`
- `output (str)`

### Returns
- 없음

### Example
```python
from ossimg.proc import sketch

sketch("cat.jpg", "result_sketch.jpg")
```

---

## 6. enhance_image(input, output, brightness, contrast)

### 설명  
이미지의 밝기와 대비를 조절합니다.

### Args
- `input (str | PIL.Image)`
- `output (str)`
- `brightness (float)` : 기본값 1.0 (1보다 크면 밝아짐)
- `contrast (float)` : 기본값 1.0 (1보다 크면 대비 증가)

### Returns
- 없음

### Example
```python
from ossimg.proc import enhance_image

enhance_image("cat.jpg", "result_enhanced.jpg", brightness=1.5, contrast=1.5)
```

---

## 7. watermark(input, output, text, opacity)

### 설명  
이미지에 투명한 워터마크 텍스트를 추가합니다.

### Args
- `input (str | PIL.Image)`
- `output (str)`
- `text (str)` : 워터마크 내용
- `opacity (int)` : 투명도(0~255)

### Returns
- 없음

### Example
```python
from ossimg.proc import watermark

watermark("cat.jpg", "result_watermark.jpg", text="OSS", opacity=128)
```

---

# 테스트

모든 함수는 unittest로 테스트되었습니다.  
테스트에서는 결과 파일 존재 여부 및 이미지 크기를 검증합니다.

```
self.assertTrue(os.path.exists("result_*.jpg"))
```

---

# Author

Documentation & QA: **임서연**

