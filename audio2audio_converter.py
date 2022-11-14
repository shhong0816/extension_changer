#음악 : mp3, ogg, wav


from pydub import AudioSegment

# files
src = "target_audio.mp3"
goal_extension = "wav"

print()

# convert wav to mp3
audSeg = AudioSegment.from_mp3('./target/'+src)
audSeg.export('./result/'+src[:-4]+'.'+goal_extension, format=goal_extension)


print("FINFINFINFIN")
