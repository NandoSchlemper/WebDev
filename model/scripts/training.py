from ultralytics import YOLOv10

# Loading YOLO Model
model = YOLOv10()

# Trainign Model
model.train(data='coco.yaml', epocs=500, batch=256, imgsz=640)

# Salvando o modelo treinado
model.save('../version')
