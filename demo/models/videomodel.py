from ..helpers.apphelper import AppHelper


database = AppHelper.get_instance().database


class VideoModel(database.Model):
    id = database.Column(database.Integer, primary_key=True)
    name = database.Column(database.String(100), nullable=False)
    views = database.Column(database.Integer, nullable=False)
    likes = database.Column(database.Integer, nullable=False)

    def __repr__(self) -> str:
        return (f"Video(name={self.name}, views={self.views},"
                f"likes={self.likes})")
