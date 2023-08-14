from pyloom import CanInitThread, CanMutateThread, Thread


class EventProcessorException(Exception):
    pass


class EventProcessor:
    """
    Event processor stores context of the processing, e.g. whether it's in replay mode or not.
    """

    def __init__(self, thread: Thread):
        self.thread = thread
        self.pre_hooks = []
        self.post_hooks = []

    def process_event(self, event, return_response=True):
        for hook in self.pre_hooks:
            event = hook(event)
        response = self._process_event(event, return_response)
        for hook in self.post_hooks:
            response = hook(response)
        return response

    def _process_event(self, event, return_response=True):
        if isinstance(event, CanInitThread):
            return event.mutate(self)
        elif isinstance(event, CanMutateThread):
            return event.process(self, return_response)
        else:
            raise EventProcessorException("Unsupported event type")
