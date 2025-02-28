def validate(model, dataloader, criterion, device):
    model.eval()
    running_loss = 0.0
    running_iou = 0.0

    with torch.no_grad():
        for images, masks in dataloader:
            images = images.to(device)
            masks = masks.to(device)

            # Forward pass
            outputs = model(images)
            loss = criterion(outputs, torch.argmax(masks, dim=1))  # Используем индексы классов

            # Вычисление метрик
            iou = calculate_iou(outputs, masks)
            running_loss += loss.item()
            running_iou += iou.item()

    epoch_loss = running_loss / len(dataloader)
    epoch_iou = running_iou / len(dataloader)
    return epoch_loss, epoch_iou
