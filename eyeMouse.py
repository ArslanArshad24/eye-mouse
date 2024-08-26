import cv2
import mediapipe as mp
import pyautogui

cap = cv2.VideoCapture(0)
face_mash = mp.solutions.face_mesh.FaceMesh(refine_landmarks=True)
screen_w , screen_h = pyautogui.size()

while True:
    ret , frame = cap.read()
    frame = cv2.flip(frame,1)
    rgb_frame =  cv2.cvtColor(frame , cv2.COLOR_BGR2RGB)
    output = face_mash.process(rgb_frame)
    landmark_points = output.multi_face_landmarks
    # print(landmark_points)
    frame_h , frame_w , _ = frame.shape
    
    if landmark_points:
        landmarsks = landmark_points[0].landmark
        for id,landmark in enumerate(landmarsks[474:478]):
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h )
            # print(x,y)
            cv2.circle(frame,(x,y), 3 , (0,255,0))
            if id == 1:
                scren_x = screen_w / frame_w * x
                screen_y = screen_h / frame_w * y
                pyautogui.moveTo(scren_x,screen_y)
        
        left  = [landmarsks[145] , landmarsks[159]]
        for landmark in left:
            x = int(landmark.x * frame_w)
            y = int(landmark.y * frame_h )
            # print(x,y)
            cv2.circle(frame,(x,y), 3 , (0,255,255))
            if left[0].y -  left[1].y < 0.009:
                pyautogui.click()
                pyautogui.sleep(1)
            
    cv2.imshow('Eye Controlled Mouse',frame)
    cv2.waitKey(1)