#동영상 : mp4, mkv, avi, webm, gif
#사진 : png, jpeg, jpg, tiff
##목표 파일 target 결과파일 result폴더에 있음.
##오류가 파일경로 한글 있어서 일수도있다하니 혹시 자동화할때 참고.

import cv2, os
vidoe_file_name = 'hi.mp4'
result_extension ='jpg'

#프레임을 저장할 디렉토리를 생성
try:
    if not os.path.exists("./result/pic/"+vidoe_file_name):
        os.makedirs("./result/pic/"+vidoe_file_name)
except OSError:
    print ('Error: Creating directory. ' +  filepath[:-4])

#Frame 쪼개기 시작
vidcap = cv2.VideoCapture('./target/'+vidoe_file_name)
success,image = vidcap.read()

count = 1
#success = True

while success:
  success,image = vidcap.read()
  prime_path = "./result/pic/"+vidoe_file_name
  count_name = "/%06d." % count
  path = prime_path + count_name+ '.'+ result_extension
  cv2.imwrite(path, image)
  print("saved image %d.jpg" % count)
  count += 1

video.release()
print("FINFINFINFIN")
