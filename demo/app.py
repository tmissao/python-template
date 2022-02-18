from .commons.fibonacci import Fibonacci
from .controllers.videocontroller import VideoController
from .helpers.apphelper import AppHelper


def run():
    fibonacci = Fibonacci()
    print('Hello from python!')
    print(fibonacci.get_random_fibonacci())
    print(fibonacci.get_multiple_random_fibonacci())
    return fibonacci.get_fibonacci(8)


def start():
    app_instance = AppHelper.get_instance()
    app_instance.api.add_resource(VideoController, "/video/<int:video_id>")
    app_instance.create_database()
    # change to env file
    app_instance.app.run(debug=True)
