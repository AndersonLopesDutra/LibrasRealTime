import cv2
import mediapipe as mp
import time
import subprocess
import re


class HandTracker:
    def __init__(self, mode=False, max_hands=1, model_complexity=1, detection_con=0.5, track_con=0.5):
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
        img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(img_rgb)

        if self.results.multi_hand_landmarks:
            for hand_lms in self.results.multi_hand_landmarks:
                if draw:
                    self.mp_draw.draw_landmarks(
                        img,
                        hand_lms,
                        self.mp_hands.HAND_CONNECTIONS,
                        self.mp_drawing_styles.get_default_hand_landmarks_style(),
                        self.mp_drawing_styles.get_default_hand_connections_style()
                    )
        return img

    def find_position(self, img, hand_no=0):
        lm_list = []
        if self.results.multi_hand_landmarks:
            my_hand = self.results.multi_hand_landmarks[hand_no]
            print("--- NOVA DETECÇÃO ---")
            for id, lm in enumerate(my_hand.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                lm_list.append([id, cx, cy])
                print(f"  Landmark {id}: (x={cx}, y={cy})")
        return lm_list


def detectar_camera_prioritaria():
    """
    Detecta o nome real das câmeras (via Media Foundation no Windows)
    e dá prioridade à DroidCam. Se não encontrar, usa a câmera padrão.
    """
    print("🔍 Buscando câmeras disponíveis (com nomes)...")

    try:
        cmd = [
            "powershell", "-Command",
            "Get-PnpDevice -Class Camera | Select-Object -ExpandProperty FriendlyName"
        ]
        result = subprocess.run(cmd, capture_output=True, text=True, shell=True)
        cameras = [c.strip() for c in result.stdout.splitlines() if c.strip()]

        if not cameras:
            print("❌ Nenhuma câmera encontrada no sistema.")
            return None

        for i, nome in enumerate(cameras):
            print(f"📷 [{i}] {nome}")

        for i, nome in enumerate(cameras):
            if re.search(r"droidcam", nome, re.IGNORECASE):
                print(f"📱 Câmera DroidCam detectada: '{nome}' (índice {i})")
                return i

        print(f"💻 Usando câmera padrão: '{cameras[0]}' (índice 0)")
        return 0

    except Exception as e:
        print(f"⚠️ Erro ao listar câmeras: {e}")
        print("Tentando fallback via OpenCV...")

        for i in range(5):
            cap = cv2.VideoCapture(i)
            if cap.isOpened():
                print(f"🎥 Usando câmera do índice {i}")
                cap.release()
                return i

        print("❌ Nenhuma câmera detectada nem pelo OpenCV.")
        return None


def main():
    """
    Função principal para rodar o rastreamento de mão.
    """
    p_time = 0
    c_time = 0

    camera_index = detectar_camera_prioritaria()
    if camera_index is None:
        print("⚠️ Nenhuma câmera disponível. Encerrando.")
        return

    cap = cv2.VideoCapture(camera_index)
    detector = HandTracker()

    while True:
        success, img = cap.read()
        if not success:
            print("❌ Falha ao capturar imagem da câmera.")
            break

        img = detector.find_hands(img)
        lm_list = detector.find_position(img)

        if len(lm_list) != 0:
            x_dedo, y_dedo = lm_list[8][1], lm_list[8][2]
            cv2.circle(img, (x_dedo, y_dedo), 10, (255, 0, 255), cv2.FILLED)
            cv2.putText(img, f"Indicador: ({x_dedo}, {y_dedo})",
                        (x_dedo + 10, y_dedo - 10),
                        cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 255), 2)

        c_time = time.time()
        fps = 1 / (c_time - p_time)
        p_time = c_time

        cv2.putText(img, f"FPS: {int(fps)}", (10, 40),
                    cv2.FONT_HERSHEY_PLAIN, 2, (0, 255, 0), 3)

        cv2.imshow("Rastreamento de Mão", cv2.flip(img, 1))

        if cv2.waitKey(1) & 0xFF == 27:  # ESC para sair
            break

    cap.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
