# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this file,
# You can obtain one at http://mozilla.org/MPL/2.0/.
"""Module containing fixtures to use within pytest tests."""

from typing import Any, Generator

import pytest
from pytest import Config, FixtureRequest
from selenium.webdriver import Firefox
from selenium.webdriver.remote.webdriver import WebDriver

from foxpuppet import FoxPuppet


@pytest.fixture
def firefox(selenium: WebDriver) -> FoxPuppet:
    """Return initialized foxpuppet object."""
    yield FoxPuppet(selenium)


@pytest.fixture
def notifications() -> Any:
    """Provide access to the different types of firefox notifications."""
    from foxpuppet.windows.browser.notifications.addons import NOTIFICATIONS

    for item in NOTIFICATIONS.values():
        setattr(notifications, item.__name__, item)
    return notifications


@pytest.fixture
def selenium(
        pytestconfig: Config,
        request: FixtureRequest) -> Generator[WebDriver, None, None]:
    """Yield selenium object if user has not already created one."""
    if pytestconfig.pluginmanager.hasplugin('selenium'):
        yield request.getfixturevalue('selenium')
    else:
        driver = Firefox()
        yield driver
        driver.quit()
