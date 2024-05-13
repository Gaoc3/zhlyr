import requests
from requests import Request
from typing import Union, Optional

class ZhLyr(Request):
    '''
    `getter` lyrics class.
    '''
    method = 'GET'
    path: list = ['/lyrics/GetLyrics','/lyrics/GetLyrPrecisily']
    param: list = ['?q','?t','&a','&duration','&srt']
    Proofreading_Marks: list = ['ture','false']
    api:str = 'https://mtskyhazoki.pythonanywhere.com'
    send_request: requests.Session = requests.Session()
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    @classmethod
    def GetByTitle(cls, title:str,srt=None) -> dict:
        '''
        :param: `title`: title of the music to get lyrics from it.
        
        :param: `srt`: proofreading marks , if `true` he will return time as `srt` format.
        '''
        if srt == None:
            srt = cls.Proofreading_Marks[1]
            prepared_request = cls(
                url=fr'{cls.api}/{cls.path[0]}{cls.param[0]}={title}{cls.param[4]}={srt}',
                method=cls.method
            )
            prepped = cls.send_request.prepare_request(prepared_request)
            r = cls.send_request.send(prepped)
            return r.json()['lyrics']

    @classmethod
    def GetByDetails(cls, title:str,artist:str,duration:Optional[Union[str,int]]=None,srt=None) -> dict:
        '''
        :param `title`: title of the music to get lyrics from it.

        :param `artist`: artist of the music to get lyrics from it.

        :param `duration`: duration of the music to get lyrics from it.

        :param `srt`: proofreading marks , if `true` he will return time as `srt` format.
        '''
        if srt == None:
            srt = cls.Proofreading_Marks[1]
        if duration == None:
            duration = duration
        prepared_request = cls(
            url=fr'{cls.api}/{cls.path[1]}{cls.param[1]}={title}{cls.param[3]}={artist}{cls.param[3]}={duration}{cls.param[4]}={srt}',
            method=cls.method
        )
        prepped = cls.send_request.prepare_request(prepared_request)
        r = cls.send_request.send(prepped)
        return r.json()['lyrics']
    
