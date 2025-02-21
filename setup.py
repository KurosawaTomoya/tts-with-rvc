from setuptools import setup, find_packages

setup(
    name='tts_with_rvc',
    version='0.1.5',
    description='TTS with RVC pipeline',
    author='Atm4x',
    packages=find_packages(),  # Update find_packages to look in 'src' director
    install_requires=[
        "huggingface_hub",
        "torch",
        "torchaudio",
        "edge-tts"
    ],
    Scripts=['tts_with_rvc/inference.py', 'tts_with_rvc/infer.py', 'tts_with_rvc/vc_infer_pipeline.py']
)
