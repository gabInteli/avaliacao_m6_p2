#Import da biblioteca co opencd
import cv2

# Abre o arquivo de video
input_video = cv2.VideoCapture('../assets/fire-video.mp4')

#Outros casos de teste
#input_video = cv2.VideoCapture('../assets/arsene.mp4')


#Identifica o modelo de classificação com base em uma biblioteca pré-pronta - Cascade
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Checa se foi possivel abrir o arquivo
if not input_video.isOpened():
    print("Error opening video file")
    exit(1)
    
# Como foi possível abrir o video de entrada, vamos agora utilizar 
# essa captura para definir o tamanho do video de saida
width  = int(input_video.get(cv2.CAP_PROP_FRAME_WIDTH))  
height = int(input_video.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Cria a estrutura do video de saida
# Com formato e local do arquivo de saida
# Codec utilizado
# FPS do video e
# Tamanho do video
output_video = cv2.VideoWriter( './saida/out.avi',cv2.VideoWriter_fourcc(*'DIVX'), 24, (width, height))

# Loop de leitura frame por frame
while True:
    # Le um frame do video e, guarda o resultado da leitura
    # Se nao houver mais frames disponiveis, ret sera falso
    ret, frame = input_video.read()
    
    #Converte a coloração do vídeo para permitir uma melhor analise
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 

    # Utiliza a biblioteca de detecção de rostos
    faces = face_cascade.detectMultiScale(gray, 1.1, 22)
    
    # Desenha um retangulo com base na identificação de rostos
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x+w, y+h), (0,0,255), 2)    

    # Se nao conseguiu ler o frame, para o laco
    if not ret:
        break

    # Exibe o frame
    cv2.imshow('Video Playback', frame)
    
    # Escreve o frame no output
    output_video.write(frame)

    # Se o usuario apertar q, encerra o playback
    # O valor utilizado no waiKey define o fps do playback
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

    
# Fecha tudo
output_video.release()
input_video.release()
cv2.destroyAllWindows()