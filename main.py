"""Demo script showing how to use the configuration module."""

from src.config import ConfigLoader, Keys, Sections

def main():
    print("Config Demo")
    print()

    config = ConfigLoader()

    # Access values using constants (type-safe)
    print()
    print("=== Using constants ===")
    server_host = config.get(Sections.SERVER, Keys.HOST)
    server_port = config.get_int(Sections.SERVER, Keys.PORT)
    print(f"Server: {server_host}:{server_port}")

if __name__ == "__main__":
    main()
