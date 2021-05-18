from django.test import TestCase, Client
from bs4 import BeautifulSoup
from .models import Post

class TestView(TestCase):
    def setUp(self):
        self.client = Client()

    def test_post_list(self):
        #1.1. 포스트 목록 페이지 가져옴
        response = self.client.get('/blog')
        # 1.2 정상적으로 페이지가 로드 됨
        self.assertEqual(response.status_code, 200)
        # 1.3 페이지 타이틀은 'blog'이다
        soup = BeautifulSoup(response.content, 'html.parser')
        self.arrsertEqual(soup.title.text, 'Blog')
        # 1.4 내이게이션 바가 있다.
        navbar = soup.nav
        # 1.5 blog, about me라는 내비게이션 바에 있다.
        self.assertIn('Blog', navbar.text)
        self.asertIn('About Me', navbar.text)
        # 2.1포스트가 하나도 없다면
        self.assertEqual(Post.objects.count(), 0)
        # 2.2main area에 아직 게시물이 없습니다. 라는 문구가 나타난다
