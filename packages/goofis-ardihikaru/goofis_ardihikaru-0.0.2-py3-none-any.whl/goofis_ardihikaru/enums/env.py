from enum import Enum


class Env(Enum):
    """ Environment enums """

    DEV = "development"
    TESTING = "testing"
    STAG = "staging"
    PROD = "production"
