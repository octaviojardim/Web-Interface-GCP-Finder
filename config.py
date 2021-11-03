class Config(object):
    DEBUG = False
    TESTING = False
    IMAGES_PATH = "/Users/octaviojardim/Documents/gcp_finder/app/images_unzip/"
    GCP_FILE_PATH = "/Users/octaviojardim/Documents/gcp_finder/app/gcp_files/"


class ProductionConfig(Config):
    pass

class DevelopmentConfig(Config):
    DEBUG = True
    