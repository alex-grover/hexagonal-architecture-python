from abc import ABC, abstractmethod
from typing import Optional, List

from hex.domain.post import Post


class DatabaseInterface(ABC):
    @abstractmethod
    def get_post(self, post_id: int) -> Post:
        pass

    @abstractmethod
    def search_posts(self, start_after: Optional[int] = None,
                     end_before: Optional[int] = None) -> List[Post]:
        pass

    @abstractmethod
    def count_posts(self) -> int:
        pass
