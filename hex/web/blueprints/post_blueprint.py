import inject
from flask import Blueprint, jsonify, Response, request

from hex.domain.actions.get_post import GetPost, PostNotFound
from hex.domain.actions.search_posts import SearchPosts
from hex.web.responses import ErrorResponse


@inject.autoparams()
def create_post_blueprint(search_posts: SearchPosts, get_post: GetPost) -> Blueprint:
    post_blueprint = Blueprint('post', __name__)

    @post_blueprint.route('/posts')
    def post_list() -> Response:
        start_after = request.args.get('start_after')
        start_after = int(start_after) if start_after else None
        end_before = request.args.get('end_before')
        end_before = int(end_before) if end_before else None

        posts, count = search_posts.execute(start_after=start_after, end_before=end_before)

        return jsonify({
            'results': [post.to_dict() for post in posts],
            'count': count
        })

    @post_blueprint.route('/posts/<int:post_id>')
    def post_detail(post_id: int) -> Response:
        post = get_post.execute(post_id=post_id)
        return jsonify(post.to_dict())

    @post_blueprint.errorhandler(PostNotFound)
    def post_not_found(error: PostNotFound):
        status = 404
        title = "Post Not Found"
        response = ErrorResponse(status, title, str(error), request.path)
        return jsonify(response.to_dict()), status

    return post_blueprint
