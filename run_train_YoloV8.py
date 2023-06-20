from ultralytics import YOLO

model = YOLO("yolov8n-seg.pt")

results = model.train(
    batch=8,
    device="cuda",  # Configura para utilizar a GPU
    data="data.yaml",
    epochs=7,
    imgsz=120,
)