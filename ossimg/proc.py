from PIL import Image, ImageFilter, ImageEnhance, ImageDraw, ImageFont
import os

def grayscale(img_path, output_path):
    """이미지를 흑백으로 변환"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert('RGB') # RGB 강제 변환
        gray_img = img.convert('L')
        gray_img.save(output_path)
        print(f"[Success] 흑백 변환 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None

def sepia(img_path, output_path):
    """세피아 톤 필터"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert('RGB') # RGB 강제 변환
        gray = img.convert('L')
        sepia_img = Image.merge('RGB', (
            gray.point(lambda x: x * 240 / 255),
            gray.point(lambda x: x * 200 / 255),
            gray.point(lambda x: x * 145 / 255)
        ))
        sepia_img.save(output_path)
        print(f"[Success] 세피아 변환 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None

def resize(img_path, output_path, width, height):
    """크기 조절"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert('RGB') # RGB 강제 변환
        resized_img = img.resize((width, height), Image.Resampling.LANCZOS)
        resized_img.save(output_path)
        print(f"[Success] 크기 조절 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None

def mosaic(img_path, output_path, pixel_size=10):
    """모자이크 처리"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert('RGB') # RGB 강제 변환
        small = img.resize((img.width // pixel_size, img.height // pixel_size), Image.Resampling.NEAREST)
        mosaic = small.resize(img.size, Image.Resampling.NEAREST)
        mosaic.save(output_path)
        print(f"[Success] 모자이크 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None

def sketch(img_path, output_path):
    """스케치 효과"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert('RGB') # RGB 강제 변환
        gray = img.convert('L')
        sketch_img = gray.filter(ImageFilter.CONTOUR)
        sketch_img.save(output_path)
        print(f"[Success] 스케치 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None

def enhance_image(img_path, output_path, brightness=1.0, contrast=1.0):
    """밝기/대비 조절"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert('RGB') # RGB 강제 변환 (이게 없어서 에러 났었음)
        if brightness != 1.0:
            img = ImageEnhance.Brightness(img).enhance(brightness)
        if contrast != 1.0:
            img = ImageEnhance.Contrast(img).enhance(contrast)
        img.save(output_path)
        print(f"[Success] 증강 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None

def watermark(img_path, output_path, text="OSS", opacity=128):
    """워터마크"""
    try:
        if not os.path.exists(img_path): return None
        img = Image.open(img_path).convert("RGBA") # 여긴 RGBA 필수
        txt_layer = Image.new("RGBA", img.size, (255, 255, 255, 0))
        draw = ImageDraw.Draw(txt_layer)
        try:
            font = ImageFont.truetype("arial.ttf", int(img.width/20))
        except:
            font = ImageFont.load_default()
        
        # 텍스트 위치 계산 (버전 호환성 위해 getbbox 사용)
        try:
            bbox = draw.textbbox((0, 0), text, font=font)
            w, h = bbox[2], bbox[3]
        except:
            w, h = draw.textsize(text, font=font)
            
        x, y = img.width - w - 20, img.height - h - 20
        draw.text((x, y), text, fill=(255, 255, 255, opacity), font=font)
        
        result = Image.alpha_composite(img, txt_layer)
        result.convert("RGB").save(output_path)
        print(f"[Success] 워터마크 완료: {output_path}")
        return output_path
    except Exception as e:
        print(f"[Error] 오류 발생: {e}")
        return None
        
    def rotate(img_path, output_path, angle):
        """이미지를 각도로 회전"""
        try:
            if not os.path.exists(img_path): 
                return None
            img = Image.open(img_path).convert('RGB')
            rotated = img.rotate(angle, expand=True)
            rotated.save(output_path)
            print(f"[Success] 회전 완료: {output_path}")
            return output_path
        except Exception as e:
            print(f"[Error] 오류 발생: {e}")
            return None
