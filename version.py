import os
import toml

class VersionUtil:

    @staticmethod
    def find_toml_file():
        for file in os.listdir('.'):
            if file.endswith('.toml'):
                return file
        return None

    @staticmethod
    def get_version():
        toml_file = VersionUtil.find_toml_file()
        if not toml_file:
            return "unknown"
        try:
            data = toml.load(toml_file)
            return data['project']['version']
        except Exception:
            return "unknown"

if __name__ == "__main__":
    version = VersionUtil.get_version()
    print(f"Extracted version: {version}")