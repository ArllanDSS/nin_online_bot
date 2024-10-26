# from utils import apertar_tecla
# from captura_tela import capture_window
# import cv2

# def inicia_minigame(window_title):
#     jogar_isca = True
#     fisgar_peixe = True
    
#     while True:
#         frame = capture_window(window_title)
#         if frame is not None:
#             # Inicia a pescaria lançando a isca e esperando o peixe morder...
#             # if jogar_isca == True:
#             #     apertar_tecla(window_title, 'f2')
#             #     print('Pesca iniciada!')
#             #     jogar_isca = False
#             #     if localizar_template(frame, 'image.png', 0.5):
#             #         apertar_tecla(window_title, 'space')
#             #         print('Lançando isca...')
                    
            
#             # if fisgar_peixe == True:
#             #     if localizar_template(frame, 'alerta.png', 0.7):
#             #         apertar_tecla(window_title, 'space')
#             #         print('Pescando...')
#             #         fisgar_peixe = False
                
#             # Exibe a janela do jogo
#             cv2.imshow('Janela do Nin Online', frame)
#             if cv2.waitKey(25) & 0xFF == ord("q"):
#                 cv2.destroyAllWindows()
#                 break