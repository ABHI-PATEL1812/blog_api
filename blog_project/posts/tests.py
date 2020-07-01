from django.contrib.auth.models import User
from django.test import TestCase

# Create your tests here.
from .models import Post


class PostTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testuser1', password='abc123'
        )
        testuser1.save()

        testpost = Post.objects.create(
            author=testuser1 , title='test title', body='this is test post body'
        )
        testpost.save()

        def test_post_content(self):
            post = Post.objects.get(id=1)
            expected_author = f'{post.author}'
            expected_title = f'{post.title}'
            expected_body = f'{post.body}'
            self.assuretEqual(expected_author, 'testuser1')
            self.assuretEqual(expected_title, 'test title')
            self.assuretEqual(expected_body, 'this is test post body')

















