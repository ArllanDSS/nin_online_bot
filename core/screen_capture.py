import cv2
import numpy as np
import win32gui
import win32ui
import win32con
import time
import threading

class ScreenCapture:
    def __init__(self, window_title):
        self.window_title = window_title
        self.running = True
        self.frame = None
        self.fps = 0
        self.last_time = time.time()
        self.frames_counted = 0

    def get_window_handle(self):
        return win32gui.FindWindow(None, self.window_title)

    def resize_window(self, width, height):
        hwnd = self.get_window_handle()
        if hwnd:
            # Redimensiona a janela
            win32gui.MoveWindow(hwnd, 0, 0, width, height, True)
            print(f'Janela "{self.window_title}" redimensionada para {width}x{height}.')
            time.sleep(1)  # Aguarda meio segundo para garantir que a janela seja redimensionada
        else:
            print(f'Janela "{self.window_title}" não encontrada!')

    def window_capture(self):
        hwnd = self.get_window_handle()
        if not hwnd:
            print(f'Janela "{self.window_title}" não encontrada!')
            return None

        # Coordenadas da janela
        left, top, right, bot = win32gui.GetClientRect(hwnd)
        left, top = win32gui.ClientToScreen(hwnd, (left, top))
        right, bot = win32gui.ClientToScreen(hwnd, (right, bot))
        width = right - left
        height = bot - top

        # Captura da janela
        hwnd_dc = win32gui.GetWindowDC(hwnd)
        mfc_dc = win32ui.CreateDCFromHandle(hwnd_dc)
        save_dc = mfc_dc.CreateCompatibleDC()
        save_bitmap = win32ui.CreateBitmap()
        save_bitmap.CreateCompatibleBitmap(mfc_dc, width, height)
        save_dc.SelectObject(save_bitmap)
        save_dc.BitBlt((0, 0), (width, height), mfc_dc, (0, 0), win32con.SRCCOPY)

        # Conversão da imagem
        bmpstr = save_bitmap.GetBitmapBits(True)
        img = np.frombuffer(bmpstr, dtype='uint8').reshape((height, width, 4))  # BGRA

        # Liberação de recursos
        win32gui.DeleteObject(save_bitmap.GetHandle())
        save_dc.DeleteDC()
        mfc_dc.DeleteDC()
        win32gui.ReleaseDC(hwnd, hwnd_dc)

        return img  # Retorna a imagem capturada

    def capture_loop(self):
        while self.running:
            self.frame = self.window_capture()
            if self.frame is not None:
                self.frames_counted += 1
                current_time = time.time()
                if current_time - self.last_time >= 1:  # Atualiza FPS
                    self.fps = self.frames_counted
                    self.frames_counted = 0
                    self.last_time = current_time
            time.sleep(1 / 90)  # Captura a 60 FPS

    def start(self):
        threading.Thread(target=self.capture_loop, daemon=True).start()

    def stop(self):
        self.running = False
