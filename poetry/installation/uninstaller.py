import csv

from io import StringIO
from pathlib import Path
from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from poetry.core.packages.package import Package
    from poetry.repositories.installed_repository import InstalledRepository
    from poetry.utils.env import Env


class Uninstaller:
    def __init__(self, env: "Env") -> None:
        self._env = env
        self._installed_repository = None

    @property
    def installed_repository(self) -> "InstalledRepository":
        if self._installed_repository is not None:
            return self._installed_repository

        from poetry.repositories.installed_repository import InstalledRepository

        self._installed_repository = InstalledRepository.load(self._env)

        return self._installed_repository

    def uninstall(self, package: "Package") -> None:
        distribution = self.installed_repository.distribution(package.name)

        if distribution is None:
            return

        reader = csv.reader(StringIO(distribution.read_text("RECORD")))
        for entry in reader:
            path = Path(entry[0])
            if not path.is_absolute():
                path = Path(str(distribution._path)).parent.joinpath(path)

            path.unlink(missing_ok=True)
