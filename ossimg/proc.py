from PIL import Image, ImageFilter
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
    

def resize(img_path, output_path, width, height):
    """
    이미지 크기를 조절하여 저장하는 함수
    :param width: 변경할 가로 길이 (px)
    :param height: 변경할 세로 길이 (px)
    """
    try:
        if not os.path.exists(img_path):
            print(f"[Error] 파일을 찾을 수 없습니다: {img_path}")
            return None

        img = Image.open(img_path)
        
        # 크기 조절 (Resampling.LANCZOS가 화질이 좋습니다)
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        
        resized_img.save(output_path)
        print(f"[Success] 크기 조절 완료 ({width}x{height}): {output_path}")
        return output_path
        
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None
    


def mosaic(img_path, output_path, pixel_size=10):
    """
    이미지에 모자이크 효과를 적용하는 함수 (개인정보 보호용)
    :param pixel_size: 모자이크 입자의 크기 (클수록 뭉개짐)
    """
    try:
        if not os.path.exists(img_path):
            print(f"[Error] 파일을 찾을 수 없습니다: {img_path}")
            return None

        img = Image.open(img_path)
        
        # 1. 이미지를 아주 작게 축소 (정보 손실 유도)
        small_img = img.resize(
            (img.width // pixel_size, img.height // pixel_size), 
            Image.Resampling.NEAREST
        )
        
        # 2. 다시 원래 크기로 확대 (픽셀이 깨져 보이게 함)
        mosaic_img = small_img.resize(
            (img.width, img.height), 
            Image.Resampling.NEAREST
        )
        
        mosaic_img.save(output_path)
        print(f"[Success] 모자이크 처리 완료: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None
    


def sketch(img_path, output_path):
    """
    이미지의 윤곽선을 추출하여 스케치 효과를 주는 함수
    """
    try:
        if not os.path.exists(img_path):
            print(f"[Error] 파일을 찾을 수 없습니다: {img_path}")
            return None

        img = Image.open(img_path)
        
        # 1. 흑백 변환 (스케치 느낌을 위해)
        gray_img = img.convert('L')
        
        # 2. 윤곽선 필터 적용 (CONTOUR)
        sketch_img = gray_img.filter(ImageFilter.CONTOUR)
        
        sketch_img.save(output_path)
        print(f"[Success] 스케치 효과 적용 완료: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None