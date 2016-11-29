class Log:
    def __init__(self, method_to_log):
        self.method_to_log = method_to_log
    def __call__(self, log_method):
        def new_method(*args, **kwargs):
            returned = self.method_to_log(*args, **kwargs)
            args = list(args) or []
            args.append(returned)
            log_method(*args, **kwargs)
            return returned
        new_method.__name__ = self.method_to_log.__name__
        setattr(self.method_to_log.im_class, self.method_to_log.__name__, new_method)
