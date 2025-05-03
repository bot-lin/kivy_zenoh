from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.boxlayout import BoxLayout
from kivy.clock import Clock
import zenoh

class ZenohKivyApp(App):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.session = zenoh.open(zenoh.Config())
        self.label_text = "Waiting for Zenoh messages..."

    def build(self):
        layout = BoxLayout(orientation='vertical')
        self.label = Label(text=self.label_text)
        layout.add_widget(self.label)
        self.session.declare_subscriber('demo/example', self.on_zenoh_message)
        return layout

    def on_zenoh_message(self, sample):
        # 修复：将 ZBytes 转换为标准 bytes 对象后再解码
        self.label_text = f"Received: {bytes(sample.payload).decode('utf-8')}"
        Clock.schedule_once(self.update_label)

    def update_label(self, dt):
        self.label.text = self.label_text

    def on_stop(self):
        self.session.close()

if __name__ == '__main__':
    ZenohKivyApp().run()