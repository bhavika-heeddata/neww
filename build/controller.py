class ResourceUpdateByPoolsAsyncController(BaseAsyncControllerWrapper):
    def _get_controller_class(self):
        return ResourceUpdateController