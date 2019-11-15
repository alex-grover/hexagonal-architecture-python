import inject
import pytest
from flask.testing import FlaskClient
from sqlalchemy import literal_column
from sqlalchemy.engine import Connection

from hex.adapters.database.postgres import posts
from hex.application import create_application
from hex.domain.post import Post
from tests.utils.dates import datetime_to_rfc822_string


@pytest.fixture
def client() -> FlaskClient:
    inject.clear()
    application = create_application()
    application.testing = True
    return application.test_client()


@pytest.fixture
def post(database_connection: Connection) -> Post:
    insert = posts.insert().values(author_name='aaa',
                                   title='bbb',
                                   body='ccc'
                                   ).returning(literal_column('*'))
    cursor = database_connection.execute(insert)
    result = cursor.fetchone()
    return Post(**result)


class TestPosts:
    def test_post_search_searches_posts(self, client: FlaskClient, post: Post) -> None:
        response = client.get('/api/posts')

        assert response.json['count'] == 1
        assert len(response.json['results']) == 1
        post_response = response.json['results'][0]
        assert post_response['id'] == post.id
        assert post_response['authorName'] == 'aaa'
        assert post_response['title'] == 'bbb'
        assert post_response['body'] == 'ccc'
        assert post_response['createdAt'] == datetime_to_rfc822_string(post.created_at)
        assert post_response['updatedAt'] == datetime_to_rfc822_string(post.updated_at)

    def test_post_detail(self, client: FlaskClient, post: Post) -> None:
        response = client.get(f'/api/posts/{post.id}')
        assert response.json['id'] == post.id
        assert response.json['authorName'] == 'aaa'
        assert response.json['title'] == 'bbb'
        assert response.json['body'] == 'ccc'
        assert response.json['createdAt'] == datetime_to_rfc822_string(post.created_at)
        assert response.json['updatedAt'] == datetime_to_rfc822_string(post.updated_at)
