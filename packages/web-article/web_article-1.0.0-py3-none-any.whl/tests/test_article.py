import unittest
from web_article import Article  # 导入你的Article类，确保路径正确


class TestArticle(unittest.TestCase):

    def setUp(self):
        # 用于设置测试的初始化操作，例如，可以在此处定义要测试的URL
        self.sample_url = 'https://zhuanlan.zhihu.com/p/631360711'
        self.article = Article(self.sample_url)

    def test_soup_property(self):
        # 测试soup属性
        soup = self.article.soup
        self.assertIsNotNone(soup)  # 验证soup是否为非None

    def test_selector_property(self):
        # 测试selector属性
        selector = self.article.selector
        self.assertIn('title', selector)
        self.assertIn('article', selector)

    def test_title_property(self):
        # 测试title属性
        title = self.article.title
        self.assertIsInstance(title, str)

    def test_text_property(self):
        # 测试text属性
        text = list(self.article.text)  # 因为text是生成器，我们转换为list处理
        self.assertTrue(all(isinstance(t, str) for t in text))

    def test_full_text_property(self):
        # 测试full_text属性
        full_text = self.article.full_text
        self.assertIsInstance(full_text, str)

    def test_repr_method(self):
        representation = repr(self.article)
        self.assertTrue(representation.startswith("Article"))


if __name__ == "__main__":
    unittest.main()
