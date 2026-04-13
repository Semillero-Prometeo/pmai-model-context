from transformers import AutoProcessor, BlipForConditionalGeneration


def import_Blip_model():
    """
    
    """
    processor = AutoProcessor.from_pretrained("Salesforce/blip-image-captioning-base")
    model = BlipForConditionalGeneration.from_pretrained("Salesforce/blip-image-captioning-base")
    return processor, model
    
    