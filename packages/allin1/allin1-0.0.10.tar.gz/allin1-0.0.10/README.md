# All-In-One Music Structure Analysis Model

[![PyPI - Version](https://img.shields.io/pypi/v/allin1.svg)](https://pypi.org/project/haha)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/allin1.svg)](https://pypi.org/project/allin1)

-----

> NOTE: This is a work in progress

**Table of Contents**

- [Installation](#installation)
- [Usage](#usage)
- [Available Models](#available-models)
- [Speed](#speed)
- [Advanced Usage for Research](#advanced-usage-for-research)
- [Concerning MP3 Files](#concerning-mp3-files)
- [Citation](#citation)

## Installation

### 1. Install PyTorch

Visit [PyTorch](https://pytorch.org/) and install the appropriate version for your system.

### 2. Install NATTEN (For Linux and Windows only, not required for macOS)

#### Linux
Visit [NATTEN website](https://www.shi-labs.com/natten/) and download the appropriate version for your system.

#### macOS
No need to install NATTEN, it will be installed automatically when installing `allin1`.

#### Windows
Build NATTEN from source:
```shell
pip install ninja # Recommended, not required
git clone https://github.com/SHI-Labs/NATTEN
cd NATTEN
make
```

### 3. Install the package

```shell
pip install git+https://github.com/CPJKU/madmom  # install the latest madmom directly from GitHub
pip install allin1  # install this package
```

### 4. (Optional) Install FFmpeg for MP3 support

For ubuntu:

```shell
sudo apt install ffmpeg
```

For macOS:

```shell
brew install ffmpeg
```

## Usage

### CLI

```shell
allin1 your_audio_file1.wav your_audio_file2.mp3
```
The result will be saved in `./structures:
```shell
./structures
└── your_audio_file1.json
└── your_audio_file2.json
```
And a JSON analysis result has:
```json
{
  "beats": [ 0.33, 0.75, 1.14, ... ],
  "downbeats": [ 0.33, 1.94, 3.53, ... ],
  "beat_positions": [ 1, 2, 3, 4, 1, 2, 3, 4, 1, ... ],
  "segments": [
    {
      "start": 0.0,
      "end": 0.33,
      "label": "start"
    },
    {
      "start": 0.33,
      "end": 13.13,
      "label": "intro"
    },
    {
      "start": 13.13,
      "end": 37.53,
      "label": "chorus"
    },
    {
      "start": 37.53,
      "end": 51.53,
      "label": "verse"
    },
    ...
  ]
}
```

### Python

```python
import allinone

# You can analyze a single file:
result = allinone.analyze('your_audio_file.wav')

# Or multiple files:
results = allinone.analyze(['your_audio_file1.wav', 'your_audio_file2.mp3'])
```
A result is a dataclass instance containing:
```python
AnalysisResult(
  beats=[0.33, 0.75, 1.14, ...],
  beat_positions=[1, 2, 3, 4, 1, 2, 3, 4, 1, ...],
  downbeats=[0.33, 1.94, 3.53, ...], 
  segments=[
    Segment(start=0.0, end=0.33, label='start'), 
    Segment(start=0.33, end=13.13, label='intro'), 
    Segment(start=13.13, end=37.53, label='chorus'), 
    Segment(start=37.53, end=51.53, label='verse'), 
    Segment(start=51.53, end=64.34, label='verse'), 
    Segment(start=64.34, end=89.93, label='chorus'), 
    Segment(start=89.93, end=105.93, label='bridge'), 
    Segment(start=105.93, end=134.74, label='chorus'), 
    Segment(start=134.74, end=153.95, label='chorus'), 
    Segment(start=153.95, end=154.67, label='end'),
  ]),
```

## Available Models
* `harmonix-all`: An ensemble model averaging the predictions of 8 models trained on each fold.
* `harmonix-foldN`: A model trained on fold N (0~7). For example, `harmonix-fold0` is trained on fold 0.

By default, the `harmonix-all` model is used. To use a different model, use the `--model` option:
```shell
allin1 --model harmonix-fold0 your_audio_file.wav
```


## Speed
Using the `harmonix-all` ensemble model, which includes 8 models trained on each fold,
10 songs (totalling 33 minutes) were processed in 73 seconds.
The hardware utilized was an RTX 4090 GPU and an Intel i9-10940X CPU (14 cores, 28 threads, 3.30 GHz).

## Advanced Usage for Research

TODO

If you run the analysis with `--embed` option and `harmonix-all` ensemble model,
the embeddings will be stacked and saved (shape: `[stems=4, time_steps, embedding_size=24, models=8]`)
`--embed` is not available for the ensemble model `harmonix-all`


## Concerning MP3 Files
Depending on decoders, MP3 files may have a slight different offsets.
I recommend first converting your audio files to WAV format using FFmpeg (as shown below)
and run the analysis on the WAV files.
```shell
ffmpeg -i your_audio_file.mp3 your_audio_file.wav
```
In more technical details, this package relies on [demucs](https://github.com/facebookresearch/demucs)
for reading audio files. As far as I know, demucs first converts MP3 files to WAV format using FFmpeg
and then reads the WAV files. However, if you use a different MP3 decoder, the offsets may be different.
I observed it can vary about 20~40ms, which is not acceptable for tasks requiring precise timing such
as beat tracking. Conventionally when evaluating beat tracking performances, the tolerance window size is 70ms. 
Therefore, I recommend you to unify input formats to WAV for all your data processing pipelines,
which doesn't require complex decoding.

## Citation

```bibtex
@inproceedings{taejun2023allinone,
  title={All-In-One Metrical And Functional Structure Analysis With Neighborhood Attentions on Demixed Audio},
  author={Kim, Taejun and Nam, Juhan},
  booktitle={IEEE Workshop on Applications of Signal Processing to Audio and Acoustics (WASPAA)},
  year={2023}
}
```