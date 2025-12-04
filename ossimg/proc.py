from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
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
    

def enhance_image(img_path, output_path, brightness=1.0, contrast=1.0):
    """
    이미지의 밝기와 대비를 조절하는 함수 (AI 데이터 증강용)
    :param brightness: 1.0이 원본, 0.5는 어둡게, 1.5는 밝게
    :param contrast: 1.0이 원본, 0.5는 흐리게, 1.5는 뚜렷하게
    """
    try:
        if not os.path.exists(img_path):
            print(f"[Error] 파일을 찾을 수 없습니다: {img_path}")
            return None

        img = Image.open(img_path)
        
        # 1. 밝기 조절
        if brightness != 1.0:
            enhancer = ImageEnhance.Brightness(img)
            img = enhancer.enhance(brightness)
            
        # 2. 대비 조절
        if contrast != 1.0:
            enhancer = ImageEnhance.Contrast(img)
            img = enhancer.enhance(contrast)
            
        img.save(output_path)
        print(f"[Success] 밝기/대비 조절 완료: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None


def watermark(img_path, output_path, text="OSS Project", opacity=128):
    """
    이미지 우측 하단에 텍스트 워터마크를 넣는 함수
    :param text: 넣을 글자
    :param opacity: 투명도 (0~255)
    """
    try:
        if not os.path.exists(img_path):
            print(f"[Error] 파일을 찾을 수 없습니다: {img_path}")
            return None

        img = Image.open(img_path).convert("RGBA")
        
        # 투명한 레이어 생성
        txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        
        # 폰트 설정 (기본 폰트 사용)
        try:
            font = ImageFont.truetype("arial.ttf", size=int(img.width / 20))
        except:
            font = ImageFont.load_default() # 폰트 없으면 기본값

        # 글자 크기 계산 (textbbox 사용 - 최신 Pillow 기준)
        bbox = draw.textbbox((0, 0), text, font=font)
        text_width = bbox[2] - bbox[0]
        text_height = bbox[3] - bbox[1]
        
        # 우측 하단 좌표 계산
        x = img.width - text_width - 20
        y = img.height - text_height - 20
        
        # 글자 쓰기 (흰색, 반투명)
        draw.text((x, y), text, fill=(255, 255, 255, opacity), font=font)
        
        # 원본과 합치기
        watermarked = Image.alpha_composite(img, txt_layer)
        
        # 다시 JPG로 저장하려면 RGB로 변환 필요
        watermarked.convert("RGB").save(output_path)
        
        print(f"[Success] 워터마크 추가 완료: {output_path}")
        return output_path
        
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None