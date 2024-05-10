from typing import Union, Optional
from shazamio import Shazam as RecoSnizer
import json
from pathlib import Path
RecoSnizer_ = RecoSnizer()
class RecoSnize(RecoSnizer):
    '''
    :param `data`: `bytes` | `bytearray` or `str path` | `Path` object 
    to get info from it.
    :param `proxy`: `str` | `None` to set `proxy` for your `request`
    '''
    def __init__(self, data: Union[str, bytes, bytearray , Path], proxy: Optional[str] = None,*args,**kwargs):
        super().__init__(*args, **kwargs)
        self.data = data
        self.proxy = proxy
        with open(self.data, 'rb') as f:
            self.data_bytes = f.read()
        self.recognizer = self.recognize(self.data_bytes, self.proxy)

    async def json(self, **kwargs) -> dict:
        '''
        Returns a json object of the recognizer.
        '''
        respstr_ = json.dumps(await self.recognizer , **kwargs)
        resp_ = json.loads(respstr_, **kwargs)
        return resp_

    @property
    async def text(self):
        '''
        Returns a string of the recognizer.
        '''
        return str(await self.recognizer)



# async def main():
#     data_path = r'C:\Users\Mtsky\Downloads\Telegram Desktop\mzaf_17549133339911745381.plus.aac.ep (2).m4a'
#     result = await RecoSnize(data_path).json()
#     print(Serializer(result).track.title)

# loop = asyncio.new_event_loop()
# loop.run_until_complete(main())
