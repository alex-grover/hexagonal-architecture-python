import pytest
from sqlalchemy import literal_column
from sqlalchemy.engine import Connection

from hex.adapters.database.postgres import posts, PostsRepository
from hex.domain.post import Post


@pytest.fixture
def database(database_uri: str) -> PostsRepository:
    return PostsRepository(database_uri)


@pytest.fixture
def post(database_connection: Connection) -> Post:
    insert = posts.insert().values(author_name='name',
                                   title='title',
                                   body='body'
                                   ).returning(literal_column('*'))
    cursor = database_connection.execute(insert)
    result = cursor.fetchone()
    return Post(**result)


class TestPostsRepository:
    def test_get_post(self, database: PostsRepository, post: Post) -> None:
        fetched_post = database.get_post(post.id)
        assert post == fetched_post

    def test_search_posts_returns_all_posts(self, database: PostsRepository, post: Post) -> None:
        fetched_posts = database.search_posts()
        assert fetched_posts == [post]

    def test_search_posts_filters_posts(self, database: PostsRepository, post: Post) -> None:
        fetched_posts = database.search_posts(end_before=post.id)
        assert fetched_posts == []

        fetched_posts = database.search_posts(start_after=post.id)
        assert fetched_posts == []

    def test_count_posts(self, database: PostsRepository, post: Post) -> None:
        assert database.count_posts() == 1
