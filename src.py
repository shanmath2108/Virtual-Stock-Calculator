import cv2
from ultralytics import YOLO
import random


model = YOLO("yolov8n.pt")
objects = model.names

def generate_market_price(field):#Dictionary with item names and prices --> Returns price of item passed
          catalogue={ 'person' : 00 , 'sneakers' : 2499,'chair' : 5500, 'othershoes ' : 1499, 'hat ' : 450, 'car ' : 750,'lamp' : 800,'glasses' : 789,'bottle': 250,'desk':3400,'cup':650,'cabinet': 12000,'handbag': 1499, 'bracelet':650,'plate':300,'picture':850,'helmet':1700,'book':350,'gloves':150,'storagebox':200,'leathershoes':4500,'flower':45,'bench':6000,'pottedplant':450,'bowl':425,'flag':120,'pillow':550,'boots':2799,'vase':1350,'microphone':1500,'necklace':650,'ring':75,'wineglass':225,'belt':200,'monitor':25000,'backpack':2500,'umbrella':575,'speaker':2599,'watch':1999,'tie':759,'trash' : 290,'slippers' : 680,'bicycle': 10000,'stool' : 850,'bucket' : 300,'couch' : 8000,'pen':45, 'carpet':6000, 'cellphone' : 34000,'bread' : 65,'camera':24000,'towel' : 145,'laptop' : 35000,'bed' : 8600,'apple' : 35,'airconditioner' : 27000,'knife' : 60 ,'fork' : 75,'spoon' : 80 ,'clock' : 1200 , 'keyboard' : 2700 ,'fan' : 3500, 'banana': 20 ,'mouse' : 350 ,'luggage' : 3000 , 'telephone' : 2200,'trolley': 2700 , 'headphone': 1700, 'remote' : 1350 , 'refrigerator' : 22000,'oven' : 11000,'lemon':7,'scissors':60,'marker':45, 'candy':5,'briefcase':950,'paintbrush':90,'extensioncord': 650,'earphone':350, 'mask':15, 'kettle':850,'projector':6500,'printer':7000,'watermelon':200, 'tissue':30, 'toothbrush':35, 'icecream' : 20 ,'broom':160, 'router':2500, 'notepaper':50,'pliers':340,'cd':250, 'hammer':350, 'flask':799, 'screwdriver':170, 'soap':40, 'coconut':25,'ruler':30,'stapler':85, 'pomegranate' : 23, 'ricecooker':2300, 'calculator' : 1500,'hairdryer':1400,'lighter' : 120,'grapefruit':50,'gameboard':2200,  'mop':180,'pencilcase':190, 'chainsaw' : 7000, 'eraser':5, 'lipstick':850, 'cosmeticsmirror' : 700,'tv':15000}    
          if field in catalogue :
                return int(catalogue[field])



def Inventory(accuracy):# Used to calculate the inventory stock

    detections=[]
    neo=[]
    inventory={}
    track_color=[(255,0,0),(153, 51, 255),(0, 179, 0),(255, 51, 51),(0, 230, 230),(230, 230, 0),(255, 153, 0),(255, 153, 255)]

    video = cv2.VideoCapture(0)
    video.set(3, 1080)
    video.set(4, 720)

    bar_width = 400
    bar_height = 25
    bar_x = int((video.get(3) - bar_width) / 2)
    bar_y = int(video.get(4) - bar_height - 20)

    progress = 0
    Callibrate_factor = accuracy
    
    while(progress <= 1):
        obj=[]
        ret, frame = video.read()

        frame = cv2.flip(frame,1)

        results = model(frame)

        for result in results:
                for box in result.boxes: 
                        if box.cls != None and objects[int(box.cls)] not in ['person','cat']: 
                            obj.append(objects[int(box.cls)])

                            for (x,y,w,h) in [(int(i) for i in j) for j in box.xywh]:
                                color=track_color[random.randint(0,len(track_color)-1)]
                                x, y = int(x-w/2), int(y-h/2)
                                cv2.rectangle(frame, (x,y), (x+w,y+h),color, 2)
        detections.append(obj)



        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + int(bar_width * progress), bar_y + bar_height), (0, 255, 0), -1)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), 2)
        cv2.putText(frame, f"CALCULATING STOCK : {int(progress*100)}%", (bar_x + 10, bar_y + bar_height - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        cv2.imshow('Inventory', frame)

        progress = ((Callibrate_factor-accuracy)/Callibrate_factor )
        accuracy = accuracy - 1 
        cv2.waitKey(1)

    video.release()
    cv2.destroyAllWindows()

    for lst in detections:
        if len(lst) > len(neo):
            neo=lst

    for key in neo:
                inventory[key]=neo.count(key)
    
    return inventory


def sale(accuracy,inventory):

    detections=[]
    neo=[]
    stock_after_sale={}
    sale={}
    
    track_color=[(255,0,0),(153, 51, 255),(0, 179, 0),(255, 51, 51),(0, 230, 230),(230, 230, 0),(255, 153, 0),(255, 153, 255)]

    video = cv2.VideoCapture(0)
    video.set(3, 1080)
    video.set(4, 720)

    bar_width = 400
    bar_height = 25
    bar_x = int((video.get(3) - bar_width) / 2)
    bar_y = int(video.get(4) - bar_height - 20)

    progress = 0
    Callibrate_factor = accuracy
    
    while(progress <= 1):
        obj=[]
        ret, frame = video.read()

        frame = cv2.flip(frame,1)

        results = model(frame)
        for result in results:
                for box in result.boxes:
                        if box.cls != None and objects[int(box.cls)] not in ['person','cat']: 
                            obj.append(objects[int(box.cls)])

                            for (x,y,w,h) in [(int(i) for i in j) for j in box.xywh]:
                                color=track_color[random.randint(0,len(track_color)-1)]
                                x, y = int(x-w/2), int(y-h/2)
                                cv2.rectangle(frame, (x,y), (x+w,y+h),color, 2)
        detections.append(obj)


        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + int(bar_width * progress), bar_y + bar_height), (0, 255, 0), -1)
        cv2.rectangle(frame, (bar_x, bar_y), (bar_x + bar_width, bar_y + bar_height), (255, 255, 255), 2)
        cv2.putText(frame, f"CALCULATING SALE : {int(progress*100)}%", (bar_x + 10, bar_y + bar_height - 5), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)
        
        cv2.imshow('Frame', frame)
        # Increment the progress value
        progress = ((Callibrate_factor-accuracy)/Callibrate_factor )
        accuracy = accuracy - 1 
        cv2.waitKey(1)
                
    video.release()
    cv2.destroyAllWindows()

    for lst in detections:
        if len(lst) > len(neo):
            neo=lst    
    
    for key in neo:
                stock_after_sale[key]=neo.count(key)

    ## Calculate sale
    for key in inventory:
            if key == 'person' or key == 'Person':
                  continue
            if key not in stock_after_sale:
                  sale[key]= inventory[key]
            else:
                  sale[key]= inventory[key] - stock_after_sale[key] if (inventory[key] != stock_after_sale[key]) else None 

    return stock_after_sale,sale


def Bill(sale):
      bill=[]
      for obj in sale:
            if sale[obj] != None:
                bill.append([obj,sale[obj],generate_market_price(obj),generate_market_price(obj)*sale[obj]])
      return bill


def LiveCheck():  
            video = cv2.VideoCapture(0)
            video.set(3, 1080)
            video.set(4, 720)
            while(True):
                ret, frame = video.read()

                frame = cv2.flip(frame,1)
                results = model(frame)
                for result in results:
                        for box in result.boxes: 
                                if box.cls != None and objects[int(box.cls)] !="person":
                                    video.release()
                                    cv2.destroyAllWindows()
                                    return False
                                
                                else:
                                      break
                                      
                cv2.putText(frame, f"FPS : {video.get(cv2.CAP_PROP_FPS)}", (75,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 2)
                cv2.imshow('Live Tracking', frame)
                cv2.waitKey(1)