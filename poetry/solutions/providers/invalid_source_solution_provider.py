from typing import List
from typing import cast

from crashtest.contracts.has_solutions_for_exception import HasSolutionsForException
from crashtest.contracts.solution import Solution


class InvalidSourceSolutionProvider(HasSolutionsForException):
    def can_solve(self, exception: Exception) -> bool:
        from poetry.exceptions import InvalidSource

        return isinstance(exception, InvalidSource)

    def get_solutions(self, exception: Exception) -> List[Solution]:
        from poetry.exceptions import InvalidSource

        from ..solutions.invalid_source_solution import InvalidSourceSolution

        return [InvalidSourceSolution(cast(InvalidSource, exception))]
