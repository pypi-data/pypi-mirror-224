from colort import colorize, ForegroundColor


class TestColort:
    def test_core(self):
        src = "Hello World"
        colorized = colorize(src, ForegroundColor.BLUE)

        assert src != colorized
