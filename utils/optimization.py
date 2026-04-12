import torch

DEVICE = "cpu" 

def optimize_model(model):
    """
    Optimiza el modelo para ejecución en CPU.
    """
    model.eval()
    for param in model.parameters():
        param.requires_grad = False
    model.to(DEVICE)
    return model

