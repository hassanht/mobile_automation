import pytest


@pytest.mark.flaky(reruns=5)
@pytest.mark.usefixtures("log_on_failure","driver")
class BaseTest:
    pass
