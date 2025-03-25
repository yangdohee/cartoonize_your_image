# Cartoonize Your Image!!!
## Functionality of 'cartoonized_your_image' Program

## 개요
`cartoonize_your_image.py`는 OpenCV를 활용하여 이미지를 만화 스타일로 변환하는 Python 프로그램입니다. 이 프로그램은 입력된 이미지를 처리하여 윤곽선을 강조하고 색상을 부드럽게 변환하여 만화 같은 효과를 제공합니다.

## 설치 및 실행 방법
### 1. 필수 라이브러리 설치
이 프로그램을 실행하려면 `OpenCV` 및 `NumPy` 라이브러리가 필요합니다. 다음 명령어를 사용하여 설치할 수 있습니다.
```sh
pip install opencv-python numpy
```

### 2. 실행 방법
Python 스크립트를 실행하려면 터미널(또는 명령 프롬프트)에서 다음과 같이 실행합니다.
```sh
python cartoonize_your_image.py
```
기본적으로 `C:\Users\dideh\OneDrive\사진\img.jpeg` 경로의 이미지를 변환하며, 결과는 `C:\Users\dideh\OneDrive\사진\cartoon_output.jpg`로 저장됩니다.

## 코드 설명

### 1. 라이브러리 불러오기
```python
import cv2
import numpy as np
```
- `cv2`: OpenCV 라이브러리로 이미지 처리 기능 제공
- `numpy`: 행렬 연산을 위한 라이브러리

### 2. `cartoonize_image` 함수 정의
```python
def cartoonize_image(image_path, output_path):
```
이 함수는 입력된 이미지를 만화 스타일로 변환하여 저장하는 기능을 합니다.

#### 2.1 이미지 불러오기
```python
img = cv2.imread(image_path)
if img is None:
    print(f"이미지를 불러올 수 없습니다. 경로를 확인하세요.")
    return
```
- `cv2.imread(image_path)`: 지정된 경로의 이미지를 불러옵니다.
- `if img is None`: 이미지가 올바르게 불러와지지 않으면 오류 메시지를 출력하고 종료합니다.

#### 2.2 그레이스케일 변환
```python
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
```
- 컬러 이미지를 흑백으로 변환하여 윤곽선을 추출하기 쉽게 만듭니다.

#### 2.3 노이즈 제거 블러 처리
```python
gray_blur = cv2.medianBlur(gray, 3)
```
- `cv2.medianBlur(gray, 3)`: 미디언 블러를 적용하여 노이즈를 줄입니다.

#### 2.4 윤곽선 검출
```python
edges = cv2.adaptiveThreshold(gray_blur, 255,
                              cv2.ADAPTIVE_THRESH_MEAN_C,
                              cv2.THRESH_BINARY, 7, 3)
```
- `cv2.adaptiveThreshold()`: 이미지의 밝기에 따라 적응형 임계값을 적용하여 윤곽선을 추출합니다.

#### 2.5 색상 부드럽게 만들기
```python
color = cv2.bilateralFilter(img, 9, 300, 300)
```
- `cv2.bilateralFilter()`: 경계를 유지하면서 색상을 부드럽게 합니다.

#### 2.6 윤곽선과 색상을 결합
```python
cartoon = cv2.bitwise_and(color, color, mask=edges)
```
- `cv2.bitwise_and()`: 윤곽선과 부드러운 색상을 결합하여 만화 효과를 생성합니다.

#### 2.7 결과 저장 및 출력
```python
cv2.imwrite(output_path, cartoon)
cv2.imshow("Cartoon Image", cartoon)
cv2.waitKey(0)
cv2.destroyAllWindows()
```
- `cv2.imwrite(output_path, cartoon)`: 변환된 이미지를 저장합니다.
- `cv2.imshow()`: 변환된 이미지를 화면에 출력합니다.

## 커스텀 입력 경로 사용하기
기본 이미지 경로 대신 다른 이미지를 변환하고 싶다면 `cartoonize_image` 함수 호출 시 직접 경로를 지정하면 됩니다.
```python
cartoonize_image("path_to_your_image.jpg", "output_cartoon.jpg")
```

## 결론
이 프로그램은 OpenCV의 다양한 필터링 및 임계값 변환 기법을 사용하여 이미지를 만화 스타일로 변환합니다. 사용자는 원하는 이미지를 입력하여 간단하게 변환할 수 있으며, 기본적으로 제공된 코드를 확장하여 추가적인 효과를 적용할 수도 있습니다




# Demos and limitations
## 만화 같은 느낌이 잘 표현되는 이미지 데모 
- 선명한 윤곽선이 있는 이미지 (예: 애니메이션 캐릭터, 만화 스타일 그림)
- 배경이 단순하고 색상의 대비가 뚜렷한 이미지
- 고화질의 사진
**예시:**
![잘 표현된 예시](demo_good.jpg)

## 만화 같은 느낌이 잘 표현되지 않는 이미지데모
- 너무 어둡거나 대비가 낮은 이미지
- 너무 많은 노이즈가 포함된 이미지
- 윤곽선이 약한 부드러운 이미지 (예: 안개 낀 풍경, 흐릿한 사진)
**예시:**
![잘 표현된 예시](demo_bad.jpg)

## 내가 만든 프로그램 알고리즘의 한계점

- **복잡한 배경**: 배경이 복잡한 경우 경계 검출이 정확하지 않을 수 있습니다.
- **디테일 손실**: Bilateral 필터를 적용하면서 세부적인 디테일이 손실될 가능성이 있습니다.
- **이미지 해상도 문제**: 너무 낮은 해상도의 이미지는 변환 결과가 부자연스러울 수 있습니다.
- **일반적인 적용 한계**: 특정 스타일의 이미지에 적합하게 설계되었으며, 모든 사진에서 최적의 결과를 보장하지 않습니다.




