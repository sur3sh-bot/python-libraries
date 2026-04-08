from textual.app import App #pip install textual
from textual.widgets import Button

class MyApp(App):
    def compose(self):
        yield Button("Click Me!")

MyApp().run()