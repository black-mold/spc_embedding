# deeplearning_framework_pl


## Introduction


## Getting Started

### 0. feature extraction
```
# Context representation - wav2vec2 base
python pre_extract_feats.py iemocap /home/nas4/DB/IEMOCAP /home/nas4/DB/IEMOCAP/IEMOCAP None None _feat_1_12

# Context representation - wav2vec2 xlsr
CUDA_VISIBLE_DEVICES=0 python pre_extract_feats.py iemocap /home/nas4/DB/IEMOCAP /home/nas4/DB/IEMOCAP/IEMOCAP None None xlsr_feat_1_12


# IC - train
python pre_extract_feats.py fluentspeechcommand /home/nas4/DB/fluent_speech_commands /home/nas4/DB/fluent_speech_commands/fluent_speech_commands_dataset None train _feat_1_12

# IC -valid
python pre_extract_feats.py fluentspeechcommand /home/nas4/DB/fluent_speech_commands /home/nas4/DB/fluent_speech_commands/fluent_speech_commands_dataset None valid _feat_1_12

# IC - test
python pre_extract_feats.py fluentspeechcommand /home/nas4/DB/fluent_speech_commands /home/nas4/DB/fluent_speech_commands/fluent_speech_commands_dataset None test _feat_1_12

```


### 1. train
```
# EMOTION RECOGNITION
CUDA_VISIBLE_DEVICES=0 python main.py --config ./configs/er_avg.yaml --mode train
```


### 2. test
```
CUDA_VISIBLE_DEVICES=0 python main.py --config ./configs/esc_50.yaml --mode test
```
