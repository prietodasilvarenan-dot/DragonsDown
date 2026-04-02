from textual.app import App
from textual.widgets import Button, Static
from textual.containers import Vertical

class MenuApp(App):

    def compose(self):
        yield Vertical(
            Static("Menu de Teste", id="title"),
            Button("Opção 1", id="opt1"),
            Button("Opção 2", id="opt2"),
            Button("Sair", id="exit"),
        )

    def on_button_pressed(self, event: Button.Pressed):
        if event.button.id == "exit":
            self.exit()
        else:
            self.notify(f"Você escolheu: {event.button.label}")

if __name__ == "__main__":
    MenuApp().run()
