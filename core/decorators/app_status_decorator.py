from core.app_state_service import AppStateService
from config.constants import AppStateConstants, AppStatusConstants

from functools import wraps


def with_app_status_change(func):
    @wraps(func)
    def wrapper(self, command, *args, **kwargs):
        AppStateService().set_state(AppStateConstants.APP_STATUS.value, AppStatusConstants.BUSY.value)

        try:
            return func(self, command, *args, **kwargs)
        finally:
            AppStateService().set_state(AppStateConstants.APP_STATUS.value, AppStatusConstants.IDLE.value)

    return wrapper
