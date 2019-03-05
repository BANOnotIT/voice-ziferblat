from os import path

from pocketsphinx import LiveSpeech

dirname = path.join(path.dirname(__file__), '../recognition_data')

config = {
    'verbose': False,
    'no_search': False,
    'full_utt': False,
    'hmm': path.join(dirname, 'zero_ru.cd_cont_4000'),
    'lm': False,
    'jsgf': path.join(dirname, 'commands.jsgf'),
    'dict': path.join(dirname, 'dict_res.dic')
}


def get_words_stream():
    return LiveSpeech(**config)
