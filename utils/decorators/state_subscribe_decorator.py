from core.app_state_service import AppStateService


def state_model_subscribe(cls):
    original_init = cls.__init__

    def new_init(self, *args, **kwargs):
        original_init(self, *args, **kwargs)

        if hasattr(self, "model"):
            for field in vars(self.model).keys():
                AppStateService().subscribe(field, self)

    cls.__init__ = new_init
    return cls
