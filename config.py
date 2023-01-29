class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = "this-is-a-super-secret-key"

config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}

## Enter your Open API Key here
OPENAI_API_KEY = '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'
REPLICATE_API_KEY = '5dc132c06194fec45120752c48adc1b09bf270b2'
