from typing import Optional, List, Tuple

import inject

from hex.domain.post import Post
from hex.domain.repositories.posts_repository import PostsRepositoryInterface


class SearchPosts:
    @inject.autoparams()
    def __init__(self, database: PostsRepositoryInterface):
        self.__database = database

    def execute(self, start_after: Optional[int],
                end_before: Optional[int]) -> Tuple[List[Post], int]:
        results = self.__database.search_posts(start_after=start_after, end_before=end_before)
        count = self.__database.count_posts()

        return results, count
