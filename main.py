"""Demo script showing how to use the configuration module."""

from src.config import ConfigLoader, Keys, Sections


def main():
    print("Hello World!")
    print()

    # Load configuration with dev environment
    config = ConfigLoader(env="dev")

    # Access values using string keys
    print("=== Using string keys ===")
    db_host = config.get("database", "host")
    db_port = config.get_int("database", "port")
    print(f"Database: {db_host}:{db_port}")

    # Access values using constants (type-safe)
    print()
    print("=== Using constants ===")
    server_host = config.get(Sections.SERVER, Keys.Server.HOST)
    server_port = config.get_int(Sections.SERVER, Keys.Server.PORT)
    debug_mode = config.get_bool(Sections.SERVER, Keys.Server.DEBUG)
    print(f"Server: {server_host}:{server_port} (debug={debug_mode})")

    # Show logging config
    print()
    print("=== Logging configuration ===")
    log_level = config.get(Sections.LOGGING, Keys.Logging.LEVEL)
    print(f"Log level: {log_level}")

    # List all available sections
    print()
    print("=== Available sections ===")
    for section in config.sections():
        print(f"  - {section}")


if __name__ == "__main__":
    main()
