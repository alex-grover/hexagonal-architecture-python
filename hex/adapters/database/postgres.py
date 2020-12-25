from typing import Optional, List, Union

from sqlalchemy import (
    create_engine, MetaData, Table, Column, Integer, Text, DateTime, func, select
)

from hex.domain.post import Post
from hex.domain.repositories.posts_repository import PostsRepositoryInterface

metadata = MetaData()


posts = Table('posts', metadata,
              Column('id', Integer, primary_key=True),
              Column('author_name', Text, nullable=False),
              Column('title', Text, nullable=False),
              Column('body', Text, nullable=False),
              Column('created_at', DateTime, nullable=False, server_default=func.now()),
              Column('updated_at', DateTime, nullable=False, server_default=func.now(),
                     onupdate=func.now()))


class PostsRepository(PostsRepositoryInterface):
    def __init__(self, database_uri: str) -> None:
        engine = create_engine(database_uri)
        self.__connection = engine.connect()

    def get_post(self, post_id: int) -> Union[Post, None]:
        query = posts.select().where(posts.c.id == post_id)
        cursor = self.__connection.execute(query)
        row = cursor.fetchone()
        if not row:
            return None
        return Post(**row)

    def search_posts(self, start_after: Optional[int] = None,
                     end_before: Optional[int] = None) -> List[Post]:
        query = posts.select()

        if start_after:
            query = query.where(posts.c.id > start_after)

        if end_before:
            query = query.where(posts.c.id < end_before)

        cursor = self.__connection.execute(query)
        rows = cursor.fetchall()
        return [Post(**row) for row in rows]

    def count_posts(self) -> int:
        query = select([func.count()]).select_from(posts)
        cursor = self.__connection.execute(query)
        result = cursor.fetchone()
        return result[0]
