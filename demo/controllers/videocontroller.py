from flask_restful import Resource, reqparse, abort, fields, marshal_with
from ..helpers.apphelper import AppHelper
from ..models.videomodel import VideoModel


video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, required=True,
                            help="Name of the Video is required")
video_put_args.add_argument("views", type=int, required=True,
                            help="Views of the Video is required")
video_put_args.add_argument("likes", type=int, required=True,
                            help="Likes on the Video is required")

video_patch_args = reqparse.RequestParser()
video_patch_args.add_argument("name", type=str,
                              help="Name of the Video is required")
video_patch_args.add_argument("views", type=int,
                              help="Views of the Video is required")
video_patch_args.add_argument("likes", type=int,
                              help="Likes on the Video is required")

resource_fields = {
    "id": fields.Integer,
    "name": fields.String,
    "views": fields.Integer,
    "likes": fields.Integer
}


class VideoController(Resource):

    database = AppHelper.get_instance().database

    def __check_if_video_exists(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if result:
            return True
        return False

    @marshal_with(resource_fields)
    def get(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message=f"Unable to find Video with id: {video_id}")
        return result

    @marshal_with(resource_fields)
    def put(self, video_id):
        if self.__check_if_video_exists(video_id):
            abort(409, message="Video Id already exists")

        args = video_put_args.parse_args()
        video = VideoModel(id=video_id, name=args["name"],
                           views=args["views"], likes=args["likes"])

        VideoController.database.session.add(video)
        VideoController.database.session.commit()

        return video, 201

    @marshal_with(resource_fields)
    def patch(self, video_id):
        video = VideoModel.query.filter_by(id=video_id).first()
        if not video:
            abort(404, message=f"Unable to find Video with id: {video_id}")

        args = video_patch_args.parse_args()

        if args['name']:
            video.name = args['name']
        if args['views']:
            video.views = args['views']
        if args['likes']:
            video.likes = args['likes']

        VideoController.database.session.commit()

        return video

    def delete(self, video_id):
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message=f"Unable to find Video with id: {video_id}")
        VideoController.database.session.delete(result)
        VideoController.database.session.commit()
        return "", 204
