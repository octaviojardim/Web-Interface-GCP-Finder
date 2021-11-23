import os

class Config(object):
    DEBUG = False
    TESTING = False
    IMAGES_PATH = "app/images_unzip/"
    GCP_FILE_PATH = os.path.abspath("app/gcp_files")
    IMAGES_FOLDER_PATH = ""

#alterar path de cima para relative path

class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    