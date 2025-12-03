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
    


def sepia(img_path, output_path):
    """
    이미지를 세피아 톤으로 변환하여 저장하는 함수
    """
    try:
        if not os.path.exists(img_path):
            print(f"[Error] 파일을 찾을 수 없습니다: {img_path}")
            return None

        img = Image.open(img_path)
        
        # 흑백으로 먼저 변환
        gray = img.convert('L')
        
        # 세피아 톤 적용 (RGB 채널별 값을 조절하여 옛날 사진 느낌 내기)
        sepia_img = Image.merge('RGB', (
            gray.point(lambda x: x * 240 / 255), # Red 채널 강조
            gray.point(lambda x: x * 200 / 255), # Green 채널 조금 강조
            gray.point(lambda x: x * 145 / 255)  # Blue 채널 약하게
        ))
        
        sepia_img.save(output_path)
        print(f"[Success] 세피아 변환 완료: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None