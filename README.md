## What is zhlyr?
  - **A platform aimed at music enthusiasts, providing tools for managing and discovering music, fetching song lyrics, and utilizing machine learning algorithms to predict the name of a song from a short audio snippet.**

## Code Area :

<details> 
<summary>
<i>🔎 Install Zhlyr</i>
</summary>
  
  ```python3
💲pip install zhlyr
  ```
------
<details>
<summary>
  <i>🔎🎵 Recognize track</i>
</summary>
Recognize a track based on a file<br>
  
```python3
# Get full track json response object info

from zhlyr import Reconize
data = '/root/user/dir/simple.mp3'
reco = Reconize(data)
print(reco.json())

# You can get respnose info as string response 
reco = Reconize(data)
print(reco.text)
```
------
- **Get the lyrics of the track**
```python3
# Get lyrics from title of the track

from zhlyr import ZhLyr
lyrics = ZhLyr.GetByTitle(title='save your trears',srt=false)
# :GetByTitle: `title`: str : title of the music to get trrack from it.
# :GetByTitle: `srt`: bool : if `true` he will return time as `srt` format.
# :GetByTitle: return json object

for time , lyric in lyrics.items():
  print(f'time {time} >>> lyric : {lyric}')


# Get lyrics from deatails of track

lyrics = ZhLyr.GetByDetails(title='save your trears',srt=false)
# :GetByDetails: `title`: str : title of the music to get trrack from it.
# :GetByDetails: `artist`: str : artist of the music to get lyrics from it.
# :GetByDetails: `duration` : Optional[Union[str,int]]=None : duration of the music to get lyrics from it.
# :GetByDetails: `srt`: bool : if `true` he will return time as `srt` format.
# :GetByDetails: return json object

for time , lyric in lyrics.items():
  print(f'time {time} >>> lyric : {lyric}')
```

## My Social Media Links Accounts
- [GitHub](https://github.com/) [<img src="https://cdn-icons-png.flaticon.com/512/25/25231.png" alt="GitHub" width="20" height="20">](https://github.com/)
- [Instagram](https://www.instagram.com/) [<img src="https://cdn-icons-png.flaticon.com/512/2111/2111463.png" alt="Instagram" width="20" height="20">](https://www.instagram.com/)
- [Telegram](https://web.telegram.org/) [<img src="https://cdn-icons-png.flaticon.com/512/2111/2111646.png" alt="Telegram" width="20" height="20">](https://web.telegram.org/)


<span style="color: red;">بحب طيز السيسي</span>

