import torch

DEVICE = "cpu" 

def optimize_model(model):
    model_quantized = torch.quantization.quantize_dynamic(
        model.cpu(), {torch.nn.Linear}, dtype=torch.qint8
    )
    return model_quantized;
