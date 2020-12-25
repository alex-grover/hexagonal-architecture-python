import inject

from hex.domain.post import Post
from hex.domain.repositories.posts_repository import PostsRepositoryInterface


class GetPost:
    @inject.autoparams()
    def __init__(self, database: PostsRepositoryInterface):
        self.__database = database

    def execute(self, post_id: int) -> Post:
        post: Post = self.__database.get_post(post_id)
        if not post:
            raise PostNotFound(post_id)
        else:
            return post


class PostNotFound(Exception):
    def __init__(self, post_id: int):
        super().__init__("A post with the id {} does not exist".format(post_id))
