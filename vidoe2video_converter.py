#동영상 : mp4, mkv, wmv, avi, webm, gif

import cv2



vidoe_file_name = 'hi.mkv'
goal_extension = 'wmv'
Codex = 'MP43'
#avi ---- DIVX
#wmv ---- MP43
#mp4 ---- mp4v
#mkv ---- MJPG


cap = cv2.VideoCapture('./target/'+vidoe_file_name)
#재생할 파일의 넓이와 높이
width = cap.get(cv2.CAP_PROP_FRAME_WIDTH)
height = cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
fourcc = cv2.VideoWriter_fourcc(*Codex)##코덱
frame = 30.0
Output_path = './result/' + vidoe_file_name[:-4] +'.'+ goal_extension
out = cv2.VideoWriter(Output_path, fourcc, frame, (int(width), int(height)))
print('변환시작')

while(cap.isOpened()):
    ret, frame = cap.read()
    if ret == False:
        break;
    #cv2.imshow('frame',frame)
    out.write(frame)
    #if cv2.waitKey(1) & 0xFF == ord('q'):
        #break

cap.release()
out.release()
#cv2.destroyAllWindows()
print("FINFINFINFIN")
