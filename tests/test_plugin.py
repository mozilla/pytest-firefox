# This Source Code Form is subject to the terms of the Mozilla Public
# License, v. 2.0. If a copy of the MPL was not distributed with this
# file, You can obtain one at http://mozilla.org/MPL/2.0/.
"""Contains tests for the main pytest-firefox fixture."""
from pytest import Testdir


def test_fixture(testdir: Testdir) -> None:
    """Test for firefox fixture."""
    testdir.makepyfile("""
        import pytest
        @pytest.fixture(scope='session')
        def firefox():
            return 'foo'
        def test_fixture(firefox):
            assert firefox == 'foo'
    """)
    result = testdir.runpytest()
    assert result.ret == 0


def test_notification(testdir: Testdir) -> None:
    """Test for notifications fixture atrribute setting."""
    testdir.makepyfile("""
        import pytest
        from foxpuppet.windows.browser.notifications.addons import \
            NOTIFICATIONS
        def test_notifications(notifications):
            for item in NOTIFICATIONS.values():
                assert getattr(notifications, item.__name__) == item
    """)
    result = testdir.runpytest()
    assert result.ret == 0
