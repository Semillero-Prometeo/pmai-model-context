

def run_inference(obj: GlobalObjectForContext, model, processor, use_prompt=True):
    image = base64_to_image(obj.image_base64)
    
    plt.imshow(image)
    plt.axis("off")
    plt.show()

    start_time = time.time()

    if use_prompt:
        inputs = processor(images=image, text=build_prompt(obj), return_tensors="pt").to(DEVICE)
    else:
        inputs = processor(images=image, return_tensors="pt").to(DEVICE)

    output = model.generate(**inputs)

    end_time = time.time()

    caption = processor.batch_decode(output, skip_special_tokens=True)[0]

    print(caption)

    return {
        "id_global": obj.id_global,
        "caption": caption,
        "latency": end_time - start_time,
        "memory": measure_memory()
    }