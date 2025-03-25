import cv2
import numpy as np

def cartoonize_image(image_path, output_path=r"C:\Users\dideh\OneDrive\사진\cartoon_output.jpg"):
    # 이미지를 만화 스타일로 변환하는 함수

    #이미지 불러오기
    img = cv2.imread(image_path)
    if img is None:
        print(f"이미지를 불러올 수 없습니다. 경로를 확인하세요.")
        return
    print("이미지 불러오기 성공하였습니다.")
    
    #그레이스케일 변환
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    #노이즈 제거 블러처리 
    gray_blur = cv2.medianBlur(gray, 3)

    #윤곽선 
    edges = cv2.adaptiveThreshold(gray_blur, 255, 
                                  cv2.ADAPTIVE_THRESH_MEAN_C, 
                                  cv2.THRESH_BINARY, 7, 3)

    #색상 부드럽게 만들기 
    color = cv2.bilateralFilter(img, 9, 300, 300)

    #윤곽선과 색상을 결합하여 만화 효과 생성
    cartoon = cv2.bitwise_and(color, color, mask=edges)

    #결과 저장 및 출력
    cv2.imwrite(output_path, cartoon)
    print(f"만화 스타일 이미지가 저장되었습니다: {output_path}")

    cv2.imshow("Cartoon Image", cartoon)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# 실행
if __name__ == "__main__":
    cartoonize_image(r"C:\Users\dideh\OneDrive\사진\img.jpeg")
