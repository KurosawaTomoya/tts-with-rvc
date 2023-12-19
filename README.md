# **TTS-with-RVC**

***TTS-with-RVC** (Text-to-Speech with RVC)* is an package designed to enhance the capabilities of *text-to-speech (TTS)* systems by introducing a *RVC* module. The package enables users to not only convert text into speech but also personalize and customize the voice output according to their preferences with RVC support.

Pytorch with CUDA or MPS is required to get TTS-with-RVC work.

**It may contain bugs. Report an issue in case of error.**
## **Installation**
1) Install pytorch **with CUDA or MPS support** here: https://pytorch.org/get-started/locally/

2) Then, install TTS-with-RVC using pip install:
```
pip install -e git+https://github.com/SunSual/tts-with-rvc.git#egg=tts-with-rvc
```
3) After, install rvc:
```
pip install -e git+https://github.com/JarodMica/rvc.git#egg=rvc
```
4) And finally, install the [fixed](https://github.com/SunSual/rvc-tts-pipeline-fix) version of rvc-tts-pipeline:
```
pip install -e git+https://github.com/SunSual/rvc-tts-pipeline-fix.git#egg=rvc_tts_pipe
```

## How it Works
1. **Text-to-Speech (TTS):** Users enter text into the TTS module, which then processes it and generates the corresponding speech as a file saved in the entered input directory
2. **RVC:** With .pth file provided, RVC module reads the generated audio file, processes it and generates an new audio saved in *output* directory with voice replaced.

## Usage

TTS-with-RVC has a class called `TTS_RVC`. There are a few parameters that are required:

`rvc_path` - path to your installed *rvc* directory (Usually in the venv/src folder) 

`input_directory` - path to your input directory (Temp direcotry for saving TTS output)

`model_path` - path to yout .pth model

And optional parameters:

`voice` - voice from edge-tts list *(default is "ru-RU-DmitryNeural")*

To get voice list, firstly, make instance of TTS_RVC:

```python
from inference import TTS_RVC

tts = TTS_RVC(rvc_path="src\\rvc", model_path="models\\YourModel.pth", input_directory="input\\")
```

Next step is calling `tts.get_voices()` and setting voice:

```python
voices = tts.get_voices()
print(voices)
tts.set_voice(voices[0])
```

This code will print all voices available and then you choose with any method you want (For example, `voices[0]`)
This is necessary if you are using other languages for voiceovers!

And final step is calling `tts` to replace voice:

```python 
path = tts(text="Привет, мир!", pitch=6)
```

Parameters:

`text` - text for TTS (required)
`pitch` - pitch for RVC (optional, default is 0)

## Example of usage
A simple example for voicing generated text:

```python
from inference import TTS_RVC
from playsound import playsound

tts = TTS_RVC(rvc_path="src\\rvc", model_path="models\\DenVot.pth", input_directory="input\\")
tts.set_voice("ru-RU-DmitryNeural")
path = tts(text="Привет, мир!", pitch=6)

playsound(path)
```
## License
No license

## Authors
[SunSual](https://github.com/SunSual) (Artem Dikarev)


