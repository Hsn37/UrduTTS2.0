# Urdu TTS

An Urdu Text to Speech System that synthesizes Urdu text in the voices of [Dr. Agha Ali Raza](http://aghaaliraza.com/) and [Zia Mohyeddin](https://en.wikipedia.org/wiki/Zia_Mohyeddin) Sb. 

**Audio Samples:** Synthesized samples are available [here](http://bit.ly/audio-samples)

## Getting Started

These instructions will help you get started  with this project for training and testing purposes.

### Prerequisites

You will require

* Ubuntu 16.04 or greater
* python 3.6
* pip3
* virtualenv

### Installation

Execute the following commands to setup the required directories and python virtual environments.

1. Clone this repository.

	```
	git clone https://github.com/Usama0121/UrduTTS.git
	cd UrduTTS
	```

2. Setup PronouncUR: This will clone PronouncUR, install its dependencies and create its python virtual environment named pvenv.

	```
	bash Install_PronouncUR.sh
	```

3. Setup tacotron: This will clone tacotron, install its dependencies and create its python virtual environment named tvenv.

	```
	bash Install_tacotron.sh
	```

	After Installation your tree should look like this

	```
	UrduTTS
	    |- tacotron
	    |- PronouncUR
	    |- pvenv
	    |- tvenv
	```

## Running UrduTTS

1. Open a terminal in UrduTTS directory and start PronouncUR. This is used to transliterate Urdu text to CISAMPA.

	```
	bash Run_PronouncUR.sh
	```

2. Open another terminal in UrduTTS directory and activate tecotron's virtual enviorment.

	```
	source tvenv/bin/activate
	cd tacotron
	```

### Using the pretrained Urdu model

1. Download pretrained [Urdu Model](http://bit.ly/urdu-tacotron-model1), extract it and place it inside tacotron directory.

2. Run the TTS Server

	2.1 In Dr. Agha's voice.

	```
	python demo_server.py --checkpoint urdu-model/model.ckpt-488000 --hparams "sample_rate=16000"
	```
	
	2.2 In Zia Mohyeddin's voice.

	```
	python demo_server.py --checkpoint urdu-model/model.ckpt-542000
	```

4. (optional)
By default server runs on port 9000 which can be changed by --port argument.

	**_Note: that port 8080 is used by PronouncUR._**

	```
	python demo_server.py --checkpoint urdu-model/model.ckpt-488000 --hparams "sample_rate=16000" --port 9010
	```

5. Access the server by navigating to the address in the browser

	```
	http://127.0.0.1:9000
	```

### Training your own Urdu model

1. Prepare speech dataset
	* Download and extract [Phonetically Rich Urdu Corpus](http://csalt.itu.edu.pk/PRUSCorpus/index.html).
	* You can also use your own dataset

2. Create a directory named Urdu/wavs inside tacotron directory and place all audios in it.
3. Now create a metadata.csv in the below format and place it inside Urdu directory.
	```
	<filename>|<transcription>
	```
	 
	**Example:** for audio1.wav with transcription خدا and audio2.wav with transcriptions حافظ the format should be
	```
	audio1|خدا
	audio2|حافظ
	```
	
4. Your tree should look like this
	```
	UrduTTS
	    |- tacotron
	        |- Urdu
	            |- metadata.csv
	            |- wavs
	                |- audio1.wav
	                |- audio2.wav
	                .
	                .
	                .
	``` 

5. Preprocess the data

	```
	python preprocess.py --dataset urdu --base_dir ./
	```

6. Start training
	

	6.1 Train from checkpoint (_if you have less then 10 hours of data then use the pretrained model and fine-tune it on your own data_)
	
	* Download [pretrained model](http://bit.ly/lj-speech-tecotron-model)
	* Extract and place the model files inside tacotron/logs-tacotron directory
	* Your tree should look like this
	
		```
		UrduTTS
		    |- tacotron
		        |- logs-tacotron
		            |- model.ckpt-441000.data-00000-of-00001
		            |- model.ckpt-441000.index
		```
	
	* Train model
		
		```
		python train.py --restore_step 441000 --base_dir ./
		```
	
	6.2 Train from scratch
	
	**_Note: Follow this step if your dataset is more than 10 hours._**
	
	```
	python train.py --base_dir ./
	```

## References

* [tacotron](https://github.com/keithito/tacotron) - A tensorflow implementation of [Google's end to end speech synthesis](https://arxiv.org/pdf/1703.10135.pdf) which directly learns to synthesize speech from (text, audio) pairs.
* [PronouncUR](https://github.com/harisbinzia/PronouncUR) - An Urdu [Lexicon Generator](http://csalt.itu.edu.pk/publications/2018--LREC--PronouncUR_An_Urdu_Pronunciation_Lexicon_Generator.pdf) that converts Urdu text to CISAMPA format.
