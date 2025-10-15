# app/hand_tracker.py

import cv2
import mediapipe as mp
import time  # Importamos a biblioteca time para calcular o FPS


class HandTracker:
    def __init__(self, mode=False, max_hands=1, model_complexity=1, detection_con=0.5, track_con=0.5):
        """
        Inicializa o detector de mãos.
        """
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=mode,
            max_num_hands=max_hands,
            model_complexity=model_complexity,
            min_detection_confidence=detection_con,
            min_tracking_confidence=track_con
        )
        self.mp_draw = mp.solutions.drawing_utils
        self.mp_drawing_styles = mp.solutions.drawing_styles

    def find_hands(self, img, draw=True):
        """
        Encontra as mãos em uma imagem e as desenha.
        """
        # Converte a imagem para RGB, pois o MediaPipe espera esse formato
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    # Desenha os landmarks e conexões na imagem original (BGR)
                    self.mp_draw.draw_landmarks(
                        img,
                        hand_lms,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style()
                    )
        return img

    def find_position(self, img, hand_no=0):
        """
        Extrai e retorna as coordenadas (landmarks) de uma mão específica.
        Imprime os dados no console para feedback.
        """
        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            print("--- NOVA DETECÇÃO ---")
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])

                # Imprime no console a posição de cada ponto (landmark)
                print(f"  Landmark {id}: (x={cx}, y={cy})")
        return lm_list


def main():
    """
    Função principal para testar o módulo diretamente.
    """
    p_time = 0  # Previous time
    c_time = 0  # Current time
    cap = cv2.VideoCapture(0)
    detector = HandTracker()

    while True:
        success, img = cap.read()
        if not success:
            break

        img = detector.find_hands(img)
        lm_list = detector.find_position(img)

        # Lógica para mostrar os dados de um landmark específico na tela
        if len(lm_list) != 0:
            # Exemplo: Pega a posição da ponta do dedo indicador (landmark 8)
            x_dedo, y_dedo = lm_list[8][1], lm_list[8][2]
            cv2.circle(img, (x_dedo, y_dedo), 10, (255, 0, 255), cv2.FILLED)
            cv2.putText(img, f"Indicador: ({x_dedo}, {y_dedo})", (x_dedo + 10, y_dedo - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

        # Cálculo e exibição do FPS
        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time

        # Coloca o texto do FPS na imagem
        cv2.putText(img, f"FPS: {int(fps)}", (10, 40), cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        # Inverte a imagem para efeito de espelho e exibe
        cv2.imshow("Rastreamento de Mao", cv2.flip(img, 1))

        # Condição de saída (pressionar 'ESC')
        if cv2.waitKey(1) & 0xFF == 27:
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()