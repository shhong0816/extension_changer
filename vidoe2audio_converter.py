#numpy 1.22 필요
##,fps= 으로 설정가능 오디오도 가능
##목표 파일 target 결과파일 result폴더에 있음.

#동영상 : mp4, mkv, avi, webm, gif
#음악 : mp3, ogg, wav


start_file = 'hi.mkv'   ##동영상
final_extension = 'mp3'   ##오디오

import moviepy.editor as mp
def v2a(path, start_file, final):
    clip = mp.VideoFileClip('./target/' + start_file)
    clip.audio.write_audiofile('./result/'+start_file[:-4]+ "." + final)


v2a(path, start_file, final_extension)


print("FIN")
