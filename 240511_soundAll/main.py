import librosa
import matplotlib.pyplot as plt
import numpy as np
from music21 import stream, note
from pydub import AudioSegment

# m4a 파일을 읽어와서 wav로 저장
audio = AudioSegment.from_file("/Users/jey25/Desktop/music.m4a")
audio.export("music.wav", format="wav")

# def audio_to_score(audio_file, output_file):
#     # Step 1: 오디오 파일 불러오기
#     y, sr = librosa.load(audio_file)

#     # Step 2: 오디오 신호 처리 (스펙트로그램 생성)
#     D = librosa.stft(y)

#     # Step 3: 음악 악보로 변환
#     pitches, magnitudes = librosa.magphase(D)
#     pitches = librosa.amplitude_to_db(pitches)

#     # 가장 높은 음과 가장 낮은 음 찾기
#     min_pitch = librosa.hz_to_midi(librosa.note_to_hz('C1'))  # C1
#     max_pitch = librosa.hz_to_midi(librosa.note_to_hz('C8'))  # C8

#     # Step 4: 악보 출력
#     music_score = stream.Stream()
#     for t in range(pitches.shape[1]):
#         freqs_at_t = pitches[:, t]
#         notes = np.argwhere(freqs_at_t > -60).flatten()  # 특정 임계값 이상의 주파수 인덱스 찾기

#         for note_idx in notes:
#             pitch = librosa.hz_to_midi(librosa.fft_frequencies(sr=sr)[note_idx])
#             if min_pitch <= pitch <= max_pitch:  # 허용된 음의 범위 내에 있는 경우
#                 n = note.Note()
#                 n.pitch.midi = int(round(pitch))
#                 n.offset = t / sr  # 시간 정보
#                 n.duration.quarterLength = 0.1  # 음 길이
#                 music_score.append(n)

#     music_score.write('midi', output_file)

#     # 악보 시각화
#     plt.figure(figsize=(12, 4))
#     music_score.plot()
#     plt.show()

# # 사용 예시
# audio_file = "music.m4a"  # 음악 파일 경로
# output_file = "output_score.mid"  # 출력 MIDI 파일 경로

# audio_to_score(audio_file, output_file)