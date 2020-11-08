import kivy
from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.uix.button import Button
import os
from update import windows_update
import record_microphone as rm
import play
# kivy.config.Config.set('graphics', 'resizable', False)
kivy.config.Config.set('graphics', 'width', '850')
kivy.config.Config.set('graphics', 'height', '500')

Window.clearcolor = (.93, 0.906, 0.859, 1)


class Layout(FloatLayout):
    kljucna_beseda = ObjectProperty(None)
    btn_snemaj = ObjectProperty(None)
    img_rec = ObjectProperty(None)
    img_play = ObjectProperty(None)
    idx_rec = 1
    idx_play = 1
    
    #recording
#    frame = []
    def __init__(self):
        self.record = rm.Record_voice()
        self.play = play.Play_voice()
        

    def btn_rec(self):
        # TODO - ko se pritisne gumb za snemanje, se sproži ta funkcija
        if self.idx_rec == 1:
            # začel je snemanje
            self.img_rec.source = "res/recording.png"
            self.idx_rec = 0
            # lahko se da tudi tukaj timer, ki traja 10 sekund in se potem source postavi nazaj na record in self.idx_rec na 1
            self.record.start_recording()
        else:
            # ustavil je snemanje
            self.img_rec.source = "res/record.png"
            self.idx_rec = 1
            self.record.stop_recording()

    def btn_play(self):
        # TODO - ko se pritisne ta gumb, je play/pause predvajati fake posnetek
        if self.idx_play == 1:
            # začel je snemanje
            self.img_play.source = "res/play.png"
            self.idx_play = 0
            self.play.play_sound()
            # če pride do konca, daj self.idx_play na 1 (kot da bi kliknil STOP)
        else:
            # ustavil je snemanje
            self.img_play.source = "res/pause.png"
            self.idx_play = 1
            self.play.pause_sound()

    def btn_stop(self):
        # TODO - ustavi predvajanje posnetka in naj gre na začetek
        self.play.stop_sound()
        pass

    def fake_work(self, keyword):
        # TODO - tukaj pride klic funkcije, ki jo pripravi Nika
        pass

    def win_configurate(self):
        # TODO - tukaj se kliče predvajanje Windows update videa
        windows_update()
        pass


class FejkITtilyumejkIT(App):

    def build(self):
        return Layout()


if __name__ == '__main__':
    FejkITtilyumejkIT().run()
