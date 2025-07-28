- ## What is zhlyr?
- **A python library aimed at music enthusiasts, providing tools for managing and discovering music, fetching song lyrics, and utilizing machine learning algorithms to predict the name of a song from a short audio snippet.**

- ## Code Area :

  <details> 
  <summary>
  <i>⏬Install Zhlyr</i>
  </summary>
    
  ```python3
  ~💲pip install zhlyr
  ```
  ------
  </details>
  
  <details>
    <summary>
    <i>🎵 Recognize track</i>
    </summary>
    <br>Recognize a track based on a file</br>
  
    ```python3
    # Get full track json response object info
  
    import asynico
    from zhlyr import Reconize
    data = '/root/user/dir/simple.mp3'
    async def get_info():
      reco = await Reconize(data)
      print(reco.json())
    loop = asynico.new_event_loop()
    loop.run_until_complete(get_info)
  
    # You can get respnose info as string response 
    reco = Reconize(data)
    print(reco.text)
    ```
  ------
  
  </details>
  
  <details>
    <summary>
    <i>🔍🎼 Get the lyrics of the track </i>
    </summary>
    <br>
    
    Get lyrics from title of the track
    </br>
    
    ```python3
    from zhlyr import ZhLyr
    lyrics = ZhLyr.GetByTitle(title='save your trears',srt=false)
    # :GetByTitle: `title`: str : title of the track to get trrack from it.
    # :GetByTitle: `srt`: bool : if `true` he will return time as `srt` format.
    # :GetByTitle: return json object
    
    for time , lyric in lyrics.items():
      print(f'time {time} >>> lyric : {lyric}')
    ```
    
    <br>
    
    Get lyrics from details of track
    </br>
    ```python3
    lyrics = ZhLyr.GetByDetails(title='save your trears',artist='the weeknd',duration='3:35',srt=false)
    # :GetByDetails: `title`: str : title of the track to get trrack from it.
    # :GetByDetails: `artist`: str : artist of the track to get lyrics from it.
    # :GetByDetails: `duration` : Optional[str]=None : duration of the track to get lyrics from it.
    # :GetByDetails: `srt`: bool : if `true` he will return time as `srt` format.
    # :GetByDetails: return json object
    
    for time , lyric in lyrics.items():
      print(f'time {time} >>> lyric : {lyric}')
    ```
  ------
  </details>
  
  <details>
    
  
  
    <summary>
      <i>ℹ️ How to use data serialization </i>
    </summary>
    <br>
    
    Serialized data from response.
    </br>
    
    ```python3
    from zhlyr import Serializer
    data = your_json_data
    serialize = Serializer(data)
    print(serialize)
    ```
    <br>
    
    Get vlue from key with serialized data.
    </br>
  
    ```python3
    data = {'key1':'hello world!'}
    serialize = Serializer(data)
    print(serialize.key1)
    ```
  ------
  
  </details>


## My Accounts
- [GitHub](https://github.com/Gaoc3/) [<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="20" height="20">](https://github.com/)
- [Instagram](https://www.instagram.com/mtsky.sensei/) [<img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" width="20" height="20">](https://www.instagram.com/)
- [Telegram](https://t.me/Art_async) [<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" alt="Telegram" width="20" height="20">](https://web.telegram.org/)
  
------

