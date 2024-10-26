from core.screen_capture import ScreenCapture
from core.utils import desenhar_fps
import cv2

if __name__ == "__main__":
    window_title = "Nin Online"  # Título da janela
    screen_capture = ScreenCapture(window_title)

    # Redimensiona a janela antes de começar a captura
    screen_capture.resize_window(450, 450)
    screen_capture.start()

    try:
        while True:
            if screen_capture.frame is not None:
                # Cria uma cópia do frame
                frame_copia = screen_capture.frame.copy()

                # Chama a função desenhar_fps com a cópia do frame
                desenhar_fps(frame_copia, screen_capture.fps)

                # Exibe a cópia do frame com o FPS desenhado
                cv2.imshow("Captura de Janela", frame_copia)  

                if cv2.waitKey(1) & 0xFF == ord("q"):
                    break
    finally:
        screen_capture.stop()
        cv2.destroyAllWindows()