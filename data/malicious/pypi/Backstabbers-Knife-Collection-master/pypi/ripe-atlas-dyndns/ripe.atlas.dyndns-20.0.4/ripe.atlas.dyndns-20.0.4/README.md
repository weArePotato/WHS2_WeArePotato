# AnupamAS01

Creating A Server

```python
from vidstream import StreamingServer

server = StreamingServer('127.0.0.1', 9999)
server.start_server()

# Other Code

# When You Are Done
server.stop_server()
```

Creating A Client
```python
from vidstream import CameraClient
from vidstream import VideoClient
from vidstream import ScreenShareClient

# Choose One
client1 = CameraClient('127.0.0.1', 9999)
client2 = VideoClient('127.0.0.1', 9999, 'video.mp4')
client3 = ScreenShareClient('127.0.0.1', 9999)

client1.start_stream()
client2.start_stream()
client3.start_stream()
```

