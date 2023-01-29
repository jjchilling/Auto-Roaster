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
