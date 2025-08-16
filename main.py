from kivy.app import App
from kivy.properties import StringProperty

class DemoApp(App):
    text_index = 0
    words = ["Python", "Java", "C", "C++", "C#"]

    current_text = StringProperty(words[0])   # 绑定到 KV

    def cycle_text(self):
        self.text_index = (self.text_index + 1) % len(self.words)
        self.current_text = self.words[self.text_index]

if __name__ == '__main__':
    DemoApp().run()
