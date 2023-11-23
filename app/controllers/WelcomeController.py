"""A WelcomeController Module."""
from masonite.views import View
from masonite.controllers import Controller


class WelcomeController(Controller):
    """WelcomeController Controller Class."""

    @staticmethod
    def show(view: View):
        """Show the welcome page."""
        return view.render("welcome")
