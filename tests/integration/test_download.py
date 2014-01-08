from betamax import Betamax
from pip.download import get_file_content, PipSession


def test_get_file_content():
    session = PipSession()
    with Betamax(session).use_cassette('get_file_content',
                                       cassette_library_dir='tests/cassettes'):
        url, text = get_file_content('https://httpbin.org/get',
                                     session=session)
        assert url == 'https://httpbin.org/get'
        assert text is not None
