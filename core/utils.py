import win32gui
import win32con
import time
import cv2

def get_window_handle(window_title):
    return win32gui.FindWindow(None, window_title)

# Mapeamento de teclas
TECLA_MAPA = {
    'f2': win32con.VK_F2,
    'space': win32con.VK_SPACE,
    # Adicione outras teclas conforme necessário
}

def apertar_tecla(window_title, tecla):
    hwnd = get_window_handle(window_title)
    if not hwnd:
        print(f'Janela "{window_title}" não encontrada!')
        return

    if tecla in TECLA_MAPA:
        tecla = TECLA_MAPA[tecla]
    else:
        print(f'Tecla "{tecla}" não mapeada!')
        return

    win32gui.SendMessage(hwnd, win32con.WM_ACTIVATE, win32con.WA_CLICKACTIVE, 0)
    time.sleep(0.1)
    win32gui.SendMessage(hwnd, win32con.WM_KEYDOWN, tecla, 0)
    win32gui.SendMessage(hwnd, win32con.WM_KEYUP, tecla, 0)  # Corrigido aqui


def desenhar_fps(frame, fps):
    """Desenha o valor do FPS na imagem.

    Args:
      frame: A imagem onde o FPS será desenhado.
      fps: O valor do FPS a ser desenhado.
    """
    cv2.putText(frame, f'FPS: {fps}', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)