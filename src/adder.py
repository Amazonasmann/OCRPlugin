from pluggy import Hookimpl

class OCRlugin:
    @Hookimpl
    def add(self, a, b):
        return a + b