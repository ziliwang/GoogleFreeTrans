from GoogleFreeTrans import Translator
from pytest import raises


def test_translation():
    en = 'china'
    fr = 'chine'
    translator = Translator.translator(src='en', dest='fr')
    out = translator.translate(en)
    assert out.lower() == fr


def test_mutil_sent_trans():
    en = 'hello. china.'
    translator = Translator.translator(src='en', dest='fr')
    rep = translator.translate('hello. china.', multi=True)
    assert rep[0][0][0].lower() == 'bonjour. '
    assert rep[0][1][0].lower() == 'chine.'


def test_unicode():
    translator = Translator.translator(src='ko', dest='ja')
    result = translator.translate('안녕하세요.')
    assert result == 'こんにちは。'


def test_special_chars():
    text = u"©×《》"
    translator = Translator.translator(src='en', dest='en')
    rep = translator.translate(text)
    assert rep == text
