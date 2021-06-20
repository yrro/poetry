from typing import TYPE_CHECKING
from typing import List

from crashtest.contracts.solution import Solution


if TYPE_CHECKING:
    from poetry.exceptions import InvalidSource


class InvalidSourceSolution(Solution):
    def __init__(self, exception: "InvalidSource") -> None:
        from poetry.exceptions import MissingSourceURL

        self._error = exception

        self._title = "Ensure your sources are properly configured."

        description = (
            "Refer to the documentation to see how to configure "
            "<fg=default;options=bold>repositories</> "
            "and <fg=default;options=bold>sources</>"
        )

        if isinstance(exception, MissingSourceURL):
            description = (
                "A source <fg=default;options=bold>must</> have a URL, either "
                "<fg=default;options=bold>specified directly</> in the pyproject.toml file "
                "or <fg=default;options=bold>configured globally</> via the config command."
            )

        description += "\n"

        self._description = description

    @property
    def solution_title(self) -> str:
        return self._title

    @property
    def solution_description(self) -> str:
        return self._description

    @property
    def documentation_links(self) -> List[str]:
        from poetry.exceptions import MissingSourceURL

        if isinstance(self._error, MissingSourceURL):
            return [
                "https://python-poetry.org/docs/repositories/#install-dependencies-from-a-private-repository",
                "https://python-poetry.org/docs/repositories/#adding-a-repository",
            ]

        return [
            "https://python-poetry.org/docs/repositories/#install-dependencies-from-a-private-repository",
        ]
