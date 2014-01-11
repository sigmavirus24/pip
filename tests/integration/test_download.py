from betamax import Betamax
from pip.download import PipSession, get_file_content, unpack_http_url
from pip.index import Link

import os


def test_get_file_content():
    """
    Test that given a URL, :func:`get_file_content` will download it.

    More specifically, test that given an http URL and not a file URI that
    this uses requests to successfully retrieve the text of the file.
    """
    session = PipSession()
    with Betamax(session).use_cassette('get_file_content'):
        url, text = get_file_content('https://httpbin.org/get',
                                     session=session)
        assert url == 'https://httpbin.org/get'
        assert text is not None


def test_unpack_http_url():
    """
    Test that given a URL, :func:`unpack_http_url` will properly unpack it.

    More specifically, test that when there isn't a cached copy, it will
    downlaod the URL.
    """
    session = PipSession()
    url = ('https://pypi.python.org/packages/2.7/g/github3.py/github3.py-0.8.0'
           '-py2.py3-none-any.whl')
    with Betamax(session).use_cassette('unpack_http_url'):
        unpack_http_url(Link(url), './temp.whl', None,
                        session=session)
        assert os.path.exists('./temp.whl')
    os.unlink('./temp.whl')
