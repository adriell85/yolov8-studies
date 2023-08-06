from ultralytics import YOLO
import torchvision.transforms as T

my_model = YOLO('runs/segment/train15/weights/best.pt') # alimenta a Yolo com o peso
results = list(my_model('datasets/test/images/img_1.jpg', conf=0.128)) # aplica em cima de uma nova imagem
result = results[0] # visualização de resultados

# result.masks.segments # Isso retorna o polígono delimitador do objeto, semelhante ao formato que passamos para os dados rotulados.

# result.masks.masks # Isso retorna um tensor com uma forma (1, 128, 128) que representa todos os pixels da imagem. Os pixels que fazem parte do objeto recebem 1 e os pixels de fundo recebem 0.
T.ToPILImage()(result.masks.masks).show()


print('Resultados:::',result)