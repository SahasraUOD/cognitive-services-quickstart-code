# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------
"""
DESCRIPTION:
    This sample demonstrates how to generate a human-readable sentence that describes the content
    of a publicly accessible image URL, using a synchronous client.

    By default the caption may contain gender terms such as "man", "woman", or "boy", "girl".
    You have the option to request gender-neutral terms such as "person" or "child" by setting
    `gender_neutral_caption = True` when calling `analyze`, as shown in this example.

    The synchronous (blocking) `analyze` method call returns an `ImageAnalysisResult` object.
    Its `caption` property (a `CaptionResult` object) contains:
    - The text of the caption. Captions are only supported in English at the moment. 
    - A confidence score in the range [0, 1], with higher values indicating greater confidences in
      the caption.

USAGE:
    python sample_caption_image_url.py

    Set these two environment variables before running the sample:
    1) VISION_ENDPOINT - Your endpoint URL, in the form https://your-resource-name.cognitiveservices.azure.com
                         where `your-resource-name` is your unique Azure Computer Vision resource name.
    2) VISION_KEY - Your Computer Vision key (a 32-character Hexadecimal number)
"""

def sample_caption_image_url():
    # <snippet_single>
    import os
    from azure.ai.vision.imageanalysis import ImageAnalysisClient
    from azure.ai.vision.imageanalysis.models import VisualFeatures
    from azure.core.credentials import AzureKeyCredential

    # Set the values of your computer vision endpoint and computer vision key
    # as environment variables:
    try:
        endpoint = os.environ["VISION_ENDPOINT"]
        key = os.environ["VISION_KEY"]
    except KeyError:
        print("Missing environment variable 'VISION_ENDPOINT' or 'VISION_KEY'")
        print("Set them before running this sample.")
        exit()

    # Create an Image Analysis client
    client = ImageAnalysisClient(
        endpoint=endpoint,
        credential=AzureKeyCredential(key)
    )

    # Get a caption for the image. This will be a synchronously (blocking) call.
    result = client.analyze(
        image_url="https://learn.microsoft.com/azure/ai-services/computer-vision/media/quickstarts/presentation.png",
        visual_features=[VisualFeatures.CAPTION, VisualFeatures.READ],
        gender_neutral_caption=True,  # Optional (default is False)
    )

    print("Image analysis results:")
    # Print caption results to the console
    print(" Caption:")
    if result.caption is not None:
        print(f"   '{result.caption.text}', Confidence {result.caption.confidence:.4f}")
    
    # Print text (OCR) analysis results to the console
    print(" Read:")
    if result.read is not None:
        for line in result.read.blocks[0].lines:
            print(f"   Line: '{line.text}', Bounding box {line.bounding_polygon}")
            for word in line.words:
                print(f"     Word: '{word.text}', Bounding polygon {word.bounding_polygon}, Confidence {word.confidence:.4f}")
    # </snippet_single>

if __name__ == "__main__":
    sample_caption_image_url()
