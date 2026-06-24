동영상 파일의 메타정보를 추출하기 위해 `moviepy`와 `pymediainfo` 라이브러리를 사용할 수 있습니다. 아래는 이 두 라이브러리를 사용하여 동영상 파일의 메타정보를 추출하는 Python 코드입니다.

먼저, 필요한 라이브러리를 설치해야 합니다. 다음 명령어를 사용하여 설치할 수 있습니다:

```bash
pip install moviepy pymediainfo
```

이제 아래의 코드를 사용하여 동영상 파일의 메타정보를 추출할 수 있습니다:

```python
from pymediainfo import MediaInfo
import os

def extract_video_metadata(file_path):
    if not os.path.isfile(file_path):
        print("파일이 존재하지 않습니다.")
        return

    # pymediainfo를 사용하여 메타정보 추출
    media_info = MediaInfo.parse(file_path)
    
    for track in media_info.tracks:
        if track.track_type == "Video":
            print(f"비디오 트랙 정보:")
            print(f"  포맷: {track.format}")
            print(f"  해상도: {track.width}x{track.height}")
            print(f"  프레임 레이트: {track.frame_rate} fps")
            print(f"  비트레이트: {track.bit_rate} bps")
        elif track.track_type == "Audio":
            print(f"오디오 트랙 정보:")
            print(f"  포맷: {track.format}")
            print(f"  샘플 레이트: {track.sample_rate} Hz")
            print(f"  비트레이트: {track.bit_rate} bps")
        elif track.track_type == "General":
            print(f"일반 정보:")
            print(f"  파일명: {track.file_name}")
            print(f"  지속 시간: {track.duration} ms")
            print(f"  크기: {track.file_size} bytes")
            print(f"  비트레이트: {track.overall_bit_rate} bps")

if __name__ == "__main__":
    video_file_path = input("동영상 파일 경로를 입력하세요: ")
    extract_video_metadata(video_file_path)
```

### 코드 설명
1. **pymediainfo**: 이 라이브러리를 사용하여 동영상 파일의 메타정보를 추출합니다.
2. **extract_video_metadata**: 주어진 파일 경로에서 메타정보를 추출하는 함수입니다.
3. **파일 존재 여부 확인**: 입력된 파일 경로가 유효한지 확인합니다.
4. **메타정보 출력**: 비디오, 오디오, 일반 정보를 출력합니다.

### 사용 방법
1. 위 코드를 Python 파일로 저장합니다 (예: `extract_metadata.py`).
2. 터미널에서 해당 파일을 실행하고 동영상 파일의 경로를 입력합니다.

이 코드를 사용하면 동영상 파일의 다양한 메타정보를 쉽게 추출할 수 있습니다.