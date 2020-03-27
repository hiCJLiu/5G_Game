

import tkinter as tk     
import random

time = 0
class People:

    def __init__(self):
        self.xpos = random.randint(0, 254)
        self.ypos = random.randint(0, 310)
        speed_list = [0.4,0.5,0.6,0.7,0.8,0.9,1.0]
        self.xspeed = speed_list[random.randint(0, len(speed_list)-1)]
        self.yspeed = speed_list[random.randint(0, len(speed_list)-1)]

class Obstacle:

	def __init__(self):

		self.length = 20
		self.breadth = 60
		start_x_list = [50, 100, 600, 140, 190, 580, 520, 630, 250]
		start_y_list = [50, 110, 670, 520, 400, 210, 590, 310, 270]
		self.start_x = start_x_list[random.randint(0, len(start_x_list)-1)]
		self.start_y = start_y_list[random.randint(0, len(start_y_list)-1)]


class Tower:

	def __init__(self):

		first_list = [280,320,360,400,430,460]
		self.first = first_list[random.randint(0, len(first_list)-1)]



class MyCanvas(tk.Canvas):

    def __init__(self, master):

        super().__init__(master, width=800, height=900, bg="snow2", bd=0, highlightthickness=0, relief="ridge")
        self.pack()

        self.people = []   
        self.bs = []      
        for _ in range(5):
            people = People()
            self.people.append(people)
            self.bs.append(self.create_oval(people.xpos - 10, people.ypos - 10, people.xpos + 10, people.ypos + 10, fill="brown"))

        # self.create_polygon(400,400,430, 400, 400, 430,430, 430)
        # self.create_polygon(280,280,310, 280, 280, 310,310, 310)
        self.tower_object = []
        for _ in range(2):
        	tow = Tower()
        	self.create_polygon(tow.first,tow.first,tow.first + 30, tow.first, tow.first, tow.first+30,tow.first+30, tow.first+30)
        	self.tower_object.append(tow)

        #self.create_polygon(400,400,430, 400, 400, 430,430, 430)
        self.obstacle_object = []

        for _ in range(6):
        	obs = Obstacle()
        	self.create_rectangle(obs.start_x, obs.start_y, obs.start_x + obs.length, obs.start_y + obs.breadth, outline="#f11", fill="blue", width='1')
        	self.obstacle_object.append(obs)

       
        self.create_text(100,10,fill="darkblue",font="Times 20 italic bold",text="5G Simulation")
        self.create_text(550,10,fill="black",font="Times 10 italic bold",text="Brown Circles: People")
        self.create_text(700,10,fill="black",font="Times 10 italic bold",text="Blue rectangles: Obstacles")
        self.create_text(370,15,fill="black",font="Times 15 italic bold",text="Seconds")
        
        for i in range(len(self.tower_object)):
            x_cord_1 = self.tower_object[i].first + 15
            y_cord_1 = self.tower_object[i].first + 15
            self.create_oval(x_cord_1-50, y_cord_1 - 50, x_cord_1+ 50, y_cord_1+50)
            self.create_text(x_cord_1, y_cord_1 - 35, fill="black",font="Times 12 italic",text="10 Gbps")
            self.create_oval(x_cord_1-200, y_cord_1 - 200, x_cord_1+ 200, y_cord_1+200)
            self.create_text(x_cord_1, y_cord_1 - 180, fill="black",font="Times 12 italic",text="5 Gbps")
            self.create_oval(x_cord_1-300, y_cord_1 - 300, x_cord_1+ 300, y_cord_1+300)
            self.create_text(x_cord_1, y_cord_1 - 280, fill="black",font="Times 12 italic",text="1 Gbps")



        #self.create_text(400,385,fill="black",font="Times 10 italic bold",text="Tower")

        self.time_id = self.create_text(300,15,fill="black",font="Times 15 italic bold",text= str(00.00))
        self.run()

    def run(self):
        global time
        time +=0.01
        self.delete(self.time_id)
        self.time_id = self.create_text(300,15,fill="black",font="Times 15 italic bold",text= str(round(time,2)))
        for p, people in zip(self.bs, self.people):
            self.move(p, people.xspeed, people.yspeed)
            pos = self.coords(p)
            #print(pos)
            if pos[3] >= 720 or pos[1] <= 0:
                people.yspeed = - people.yspeed
            if pos[2] >= 800 or pos[0] <= 0:
                people.xspeed = - people.xspeed
            for i in range(len(self.obstacle_object)):
            	x_cord_1 = self.obstacle_object[i].start_x
            	y_cord_1 = self.obstacle_object[i].start_y
            	x_cord_2 = self.obstacle_object[i].start_x + self.obstacle_object[i].length
            	y_cord_2 = self.obstacle_object[i].start_y + self.obstacle_object[i].breadth
            	if(pos[0] >= x_cord_1 - 5 and pos[0] <= x_cord_2 + 5 and pos[1] >= y_cord_1 -5 and pos[1] <= y_cord_2 +5):
            		people.xspeed = - people.xspeed
            for i in range(len(self.tower_object)):
            	x_cord_1 = self.tower_object[i].first -10
            	y_cord_1 = self.tower_object[i].first -10
            	x_cord_2 = x_cord_1 + 50
            	y_cord_2 = y_cord_1 + 50
            	if(pos[0] >= x_cord_1  and pos[0] <= x_cord_2  and pos[1] >= y_cord_1  and pos[1] <= y_cord_2 ):
            		people.xspeed = - people.xspeed            		


        self.after(10, self.run)
        


if __name__ == '__main__':

    simulation_window = tk.Tk()
    simulation_window.title('5G Simulation')
    simulation_window.geometry("1000x1000")
    c = MyCanvas(simulation_window)

    simulation_window.mainloop()
