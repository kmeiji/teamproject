from PIL import Image
import os

def grayscale(img_path, output_path):
    """
    이미지를 흑백으로 변환하는 함수
    """
    try:
        # 1. 파일 확인
        if not os.path.exists(img_path):
            print(f"Error: {img_path} not found.")
            return None
            
        # 2. 이미지 열기
        img = Image.open(img_path)
        
        # 3. 흑백 변환 (mode 'L')
        gray_img = img.convert('L')
        
        # 4. 저장
        gray_img.save(output_path)
        print(f"Success: Saved to {output_path}")
        return output_path
        
    except Exception as e:
        print(f"Error: {e}")
        return None