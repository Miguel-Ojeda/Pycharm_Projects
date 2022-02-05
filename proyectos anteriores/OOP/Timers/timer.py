# Clase Timer...
# Esto ya está realmente en el módulo pyghelpers, pero lo haremos nosotros!!!
import time

class Timer:
    def __init__(self, seconds, nick_name=None, callback=None):
        self.timer_seconds = seconds
        self.start_time = None
        self.running = False
        self.nick_name = nick_name
        self.elapsed_seconds = 0
        self.callback = callback

    def start(self, new_timer_seconds=None):
        if new_timer_seconds:
            self.timer_seconds = new_timer_seconds
        self.running = True
        self.start_time = time.time()


    def ha_finalizado(self):
        if not self.running:
            return False
        self.elapsed_seconds = time.time() - self.start_time
        if self.elapsed_seconds < self.timer_seconds:
            return False # todavía no ha terminado el timer!!!
        else:
            self.running = False # terminamos el timer...
            if self.callback:
                self.callback(self.nick_name)   # llamamos a la función, diciéndole qué timer ha expirado!!!

            return True

    def get_time(self):
        if self.running:
            self.elapsed_seconds = time.time() - self.start_time
            return self.elapsed_seconds
        else:
            return False

    def stop(self):
        self.get_time()   # actualiza el tiempo que ha transcurrido...
        self.running = False   # detenemos el timer...

    def pause(self):
        if self.running:
            self.elapsed_seconds = time.time() - self.start_time
            self.running = False



    def is_running(self):
        return self.running
