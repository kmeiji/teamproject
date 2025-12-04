import unittest
import os
from ossimg import grayscale, sepia, resize
from PIL import Image

class TestImageProc(unittest.TestCase):
    def setUp(self):
        # 테스트 전용 가짜 이미지 만들기 (10x10 빨간색)
        self.test_img_name = "test_dummy.jpg"
        img = Image.new('RGB', (10, 10), color='red')
        img.save(self.test_img_name)

    def tearDown(self):
        # 테스트 끝나면 파일 삭제 (청소)
        if os.path.exists(self.test_img_name):
            os.remove(self.test_img_name)
        # 생성된 결과물들도 삭제
        if os.path.exists("result_gray.jpg"):
            os.remove("result_gray.jpg")

    def test_grayscale(self):
        # 흑백 변환이 에러 없이 되는지 테스트
        result = grayscale(self.test_img_name, "result_gray.jpg")
        self.assertTrue(os.path.exists(result)) # 파일이 생겼는지 확인

    def test_resize(self):
        # 리사이즈가 정확한 크기로 됐는지 테스트
        resize(self.test_img_name, "result_resize.jpg", 5, 5)
        img = Image.open("result_resize.jpg")
        self.assertEqual(img.size, (5, 5)) # 크기가 5x5인지 확인
        img.close()
        os.remove("result_resize.jpg")

if __name__ == '__main__':
    unittest.main()