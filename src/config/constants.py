"""Constants for configuration section and key names."""


class Sections:
    """Configuration section names."""

    DATABASE = "database"
    SERVER = "server"
    LOGGING = "logging"


class Keys:
    """Configuration key names organized by section."""

    class Database:
        HOST = "host"
        PORT = "port"
        NAME = "name"
        USER = "user"
        PASSWORD = "password"

    class Server:
        HOST = "host"
        PORT = "port"
        DEBUG = "debug"

    class Logging:
        LEVEL = "level"
        FORMAT = "format"
