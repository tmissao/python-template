import os.path
from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy


class AppHelper:
    __instance = None
    __database_file_path = f'{os.getcwd()}/database.db'

    @staticmethod
    def get_instance():
        if AppHelper.__instance is None:
            AppHelper()
        return AppHelper.__instance

    def __init__(self):
        if AppHelper.__instance is not None:
            raise Exception("This class is a singleton")
        AppHelper.__instance = self

        self.app = Flask(__name__)
        self.api = Api(self.app)
        self.database = self.__setup_database()

    def __setup_database(self):
        # create a config here
        print(self.__database_file_path)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = (
         f'sqlite:///{self.__database_file_path}'
        )
        database = SQLAlchemy(self.app)
        return database

    def create_database(self):
        if not os.path.exists(self.__database_file_path):
            print('>>>>>> creating database')
            self.database.create_all()
