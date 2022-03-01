# import tensorflow as tf

# import yaml
# import numpy as np
# import soundfile as sf

# from tensorflow_tts.inference import TFAutoModel
# from tensorflow_tts.inference import AutoConfig
# from tensorflow_tts.inference import AutoProcessor

# tacotron2 = TFAutoModel.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en", name="tacotron2")
# melgan = TFAutoModel.from_pretrained("tensorspeech/tts-melgan-ljspeech-en", name="melgan")
# processor = AutoProcessor.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en")

# print("Imports done...")

# tacotron2 = TFAutoModel.from_pretrained("tensorspeech/tts-tacotron2-ljspeech-en", name="tacotron2")
# melgan = TFAutoModel.from_pretrained("tensorspeech/tts-melgan-ljspeech-en", name="melgan")



# def do_synthesis(input_text, text2mel_model, vocoder_model, text2mel_name, vocoder_name):
# 	input_ids = processor.text_to_sequence(input_text)

# 	_, mel_outputs, stop_token_prediction, alignment_history = text2mel_model.inference(
#         tf.expand_dims(tf.convert_to_tensor(input_ids, dtype=tf.int32), 0),
#         tf.convert_to_tensor([len(input_ids)], tf.int32),
#         tf.convert_to_tensor([0], dtype=tf.int32)
#     )

# 	audio = vocoder_model(mel_outputs)[0, :, 0]

# 	return mel_outputs.numpy(), alignment_history.numpy(), audio.numpy()


# while True:
# 	input_text = input(">> ")

# 	mels, alignment_history, audios = do_synthesis(input_text, tacotron2, melgan, "TACOTRON", "MELGAN")
# 	sf.write('./audio.wav', audios, 22050, "PCM_16")
# 	print("Audio Saved!!")

import os
print(os.getcwd())

from tensorflow_tts.bin import preprocess

# arguments must be present in args
# --rootdir ./ljspeech --outdir ./dump_ljspeech --config preprocess/ljspeech_preprocess.yaml --dataset ljspeech
preprocess.preprocess()
preprocess.normalize()
