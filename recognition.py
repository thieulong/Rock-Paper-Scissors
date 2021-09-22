import cv2
import mediapipe
import math
import csv


def distance(a, b):

    return math.sqrt(math.pow((b[0]-a[0]),2)+math.pow(b[1]-a[1],2))


def search_point(pts_list, cord, target):

    if cord == "x":
        for i in range(len(pts_list)):
            if pts_list[i][0] == target:
                return pts_list[i]
    elif cord == "y":
        for i in range(len(pts_list)):
            if pts_list[i][1] == target:
                return pts_list[i]
    else:
        return


def landmark_recognition():

    camera_id = 1

    capture = cv2.VideoCapture(camera_id)

    drawingModule = mediapipe.solutions.drawing_utils
    handsModule = mediapipe.solutions.hands

    frameWidth = capture.get(cv2.CAP_PROP_FRAME_WIDTH)
    frameHeight = capture.get(cv2.CAP_PROP_FRAME_HEIGHT)


    result = ""

    with handsModule.Hands(static_image_mode=False, min_detection_confidence=0.7, min_tracking_confidence=0.7, max_num_hands=1) as hands:
    
        while True:
    
            ret, frame = capture.read()
    
            results = hands.process(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
    
            if results.multi_hand_landmarks != None:

                for handLandmarks in results.multi_hand_landmarks:

                    # Wrist (O)
                    wrist = 0
                    wrist_normalizedLandmark = handLandmarks.landmark[wrist]
                    wrist_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(wrist_normalizedLandmark.x, wrist_normalizedLandmark.y, frameWidth, frameHeight)

                    # cv2.circle(frame, wrist_pixelCoordinatesLandmark, 5, (255, 255, 0), -1)

                    # Thumb tip (A)
                    thumbtip = 4
                    thumbtip_normalizedLandmark = handLandmarks.landmark[thumbtip]
                    thumbtip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(thumbtip_normalizedLandmark.x, thumbtip_normalizedLandmark.y, frameWidth, frameHeight)

                    # cv2.circle(frame, thumbtip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

                    # Index finger tip (B)
                    index_fingertip = 8
                    index_fingertip_normalizedLandmark = handLandmarks.landmark[index_fingertip]
                    index_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(index_fingertip_normalizedLandmark.x, index_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

                    # cv2.circle(frame, index_fingertip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

                    # Middle finger tip (C)
                    mid_fingertip = 12
                    mid_fingertip_normalizedLandmark = handLandmarks.landmark[mid_fingertip]
                    mid_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(mid_fingertip_normalizedLandmark.x, mid_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

                    # cv2.circle(frame, mid_fingertip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

                    # Ring finger tip (D)
                    ring_fingertip = 16
                    ring_fingertip_normalizedLandmark = handLandmarks.landmark[ring_fingertip]
                    ring_fingertip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(ring_fingertip_normalizedLandmark.x, ring_fingertip_normalizedLandmark.y, frameWidth, frameHeight)

                    # cv2.circle(frame, ring_fingertip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

                    # Pinky tip (E)
                    pinkytip = 20
                    pinkytip_normalizedLandmark = handLandmarks.landmark[pinkytip]
                    pinkytip_pixelCoordinatesLandmark = drawingModule._normalized_to_pixel_coordinates(pinkytip_normalizedLandmark.x, pinkytip_normalizedLandmark.y, frameWidth, frameHeight)

                    # cv2.circle(frame, pinkytip_pixelCoordinatesLandmark, 5, (0, 255, 0), -1)

                    # cv2.line(frame, wrist_pixelCoordinatesLandmark, thumbtip_pixelCoordinatesLandmark, (255, 102, 255), 2)
                    # cv2.line(frame, wrist_pixelCoordinatesLandmark, index_fingertip_pixelCoordinatesLandmark, (255, 102, 255), 2)
                    # cv2.line(frame, wrist_pixelCoordinatesLandmark, mid_fingertip_pixelCoordinatesLandmark, (255, 102, 255), 2)
                    # cv2.line(frame, wrist_pixelCoordinatesLandmark, ring_fingertip_pixelCoordinatesLandmark, (255, 102, 255), 2)
                    # cv2.line(frame, wrist_pixelCoordinatesLandmark, pinkytip_pixelCoordinatesLandmark, (255, 102, 255), 2)

                    if wrist_pixelCoordinatesLandmark and index_fingertip_pixelCoordinatesLandmark and mid_fingertip_pixelCoordinatesLandmark and ring_fingertip_pixelCoordinatesLandmark and pinkytip_pixelCoordinatesLandmark:

                        dist_OA = distance(a=wrist_pixelCoordinatesLandmark, b=thumbtip_pixelCoordinatesLandmark)
                        dist_OB = distance(a=wrist_pixelCoordinatesLandmark, b=index_fingertip_pixelCoordinatesLandmark)
                        dist_OC = distance(a=wrist_pixelCoordinatesLandmark, b=mid_fingertip_pixelCoordinatesLandmark)
                        dist_OD = distance(a=wrist_pixelCoordinatesLandmark, b=ring_fingertip_pixelCoordinatesLandmark)
                        dist_OE = distance(a=wrist_pixelCoordinatesLandmark, b=pinkytip_pixelCoordinatesLandmark)

                        # print("Distance OA: {}".format(dist_OA))
                        # print("Distance OB: {}".format(dist_OB))
                        # print("Distance OC: {}".format(dist_OC))
                        # print("Distance OD: {}".format(dist_OD))
                        # print("Distance OE: {}".format(dist_OE))

                        right_most = max([wrist_pixelCoordinatesLandmark[0], thumbtip_pixelCoordinatesLandmark[0], index_fingertip_pixelCoordinatesLandmark[0], mid_fingertip_pixelCoordinatesLandmark[0], ring_fingertip_pixelCoordinatesLandmark[0], pinkytip_pixelCoordinatesLandmark[0]])
                        left_most = min([wrist_pixelCoordinatesLandmark[0], thumbtip_pixelCoordinatesLandmark[0], index_fingertip_pixelCoordinatesLandmark[0], mid_fingertip_pixelCoordinatesLandmark[0], ring_fingertip_pixelCoordinatesLandmark[0], pinkytip_pixelCoordinatesLandmark[0]])
                        upper_most = min([wrist_pixelCoordinatesLandmark[1], thumbtip_pixelCoordinatesLandmark[1], index_fingertip_pixelCoordinatesLandmark[1], mid_fingertip_pixelCoordinatesLandmark[1], ring_fingertip_pixelCoordinatesLandmark[1], pinkytip_pixelCoordinatesLandmark[1]])
                        lower_most = max([wrist_pixelCoordinatesLandmark[1], thumbtip_pixelCoordinatesLandmark[1], index_fingertip_pixelCoordinatesLandmark[1], mid_fingertip_pixelCoordinatesLandmark[1], ring_fingertip_pixelCoordinatesLandmark[1], pinkytip_pixelCoordinatesLandmark[1]])
                        
                        up_join_pt = search_point(pts_list=[wrist_pixelCoordinatesLandmark, thumbtip_pixelCoordinatesLandmark, index_fingertip_pixelCoordinatesLandmark, mid_fingertip_pixelCoordinatesLandmark, ring_fingertip_pixelCoordinatesLandmark, pinkytip_pixelCoordinatesLandmark], cord="y", target=upper_most)
                        left_join_pt = search_point(pts_list=[wrist_pixelCoordinatesLandmark, thumbtip_pixelCoordinatesLandmark, index_fingertip_pixelCoordinatesLandmark, mid_fingertip_pixelCoordinatesLandmark, ring_fingertip_pixelCoordinatesLandmark, pinkytip_pixelCoordinatesLandmark], cord="x", target=left_most)
                        low_join_pt = search_point(pts_list=[wrist_pixelCoordinatesLandmark, thumbtip_pixelCoordinatesLandmark, index_fingertip_pixelCoordinatesLandmark, mid_fingertip_pixelCoordinatesLandmark, ring_fingertip_pixelCoordinatesLandmark, pinkytip_pixelCoordinatesLandmark], cord="y", target=lower_most)
                        right_join_pt = search_point(pts_list=[wrist_pixelCoordinatesLandmark, thumbtip_pixelCoordinatesLandmark, index_fingertip_pixelCoordinatesLandmark, mid_fingertip_pixelCoordinatesLandmark, ring_fingertip_pixelCoordinatesLandmark, pinkytip_pixelCoordinatesLandmark], cord="x", target=right_most)

                        up_join_dist = distance(a=up_join_pt, b=left_join_pt)
                        low_join_dist = distance(a=right_join_pt, b=low_join_pt)

                        top_left_corner = (int(up_join_pt[0]-up_join_dist-50), up_join_pt[1]-50)
                        bottom_right_corner = (int(low_join_pt[0]+low_join_dist+30), low_join_pt[1]+50)

                        # cv2.rectangle(frame, top_left_corner, bottom_right_corner, (255,0,0), thickness=2)

                        if dist_OA <= 170 and dist_OB >= 230 and dist_OC >= 230 and dist_OD <= 170 and dist_OE <= 130:
            
                            result = "Scissor"

                            img = frame[top_left_corner[1]:bottom_right_corner[1], top_left_corner[0]:bottom_right_corner[0]]
                            cv2.imwrite('images/user_result.jpg', img)

                            # print(result)

                            return result
                        
                        elif dist_OA <= 165 and dist_OB <= 148 and dist_OC <= 138 and dist_OD <= 132 and dist_OE <= 115:

                            result = "Rock"

                            img = frame[top_left_corner[1]:bottom_right_corner[1], top_left_corner[0]:bottom_right_corner[0]]
                            cv2.imwrite('images/user_result.jpg', img)

                            # print(result)

                            return result

                        elif dist_OA >= 110 and dist_OB >= 170 and dist_OC >= 170 and dist_OD >= 145 and dist_OE >= 100:

                            result = "Paper"

                            img = frame[top_left_corner[1]:bottom_right_corner[1], top_left_corner[0]:bottom_right_corner[0]]
                            cv2.imwrite('images/user_result.jpg', img)

                            # print(result)

                            return result

#                         data = [dist_OA,dist_OB,dist_OC,dist_OD,dist_OE]

#                         with open('tracking-scissors.csv', 'a', encoding='UTF8') as f:
#                             writer = csv.writer(f) 
#                             writer.writerow(data)
    
#             cv2.imshow('Rock, Paper, Scissors!', frame)

    
#             if cv2.waitKey(1) == 27:
#                 break
    
#     cv2.destroyAllWindows()
#     capture.release()

# landmark_recognition()