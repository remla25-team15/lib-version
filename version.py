import toml
from pathlib import Path

class VersionUtil:

    @staticmethod
    def find_toml_file(start_dir='.'):
        current_path = Path(start_dir).resolve()
        root_path = Path(current_path.root)

        while current_path != root_path:
            candidate = current_path / 'pyproject.toml'
            if candidate.exists():
                return str(candidate)
            current_path = current_path.parent

        # Final check at filesystem root
        if (root_path / 'pyproject.toml').exists():
            return str(root_path / 'pyproject.toml')

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

