#traffic light for raspberry pi simlulating in pycham with GUI
import turtle
import time
wn= turtle.getscreen()
wn.title("Stoplight By Gogulkrish")
wn.bgcolor("white")

pen= turtle.Turtle()
pen.color("black")
pen.width(5)
pen.hideturtle()
pen.penup()
pen.goto(-30, 60)
pen.pendown()
pen.fd(60)
pen.rt(90)
pen.fd(120)
pen.rt(90)
pen.fd(60)
pen.rt(90)
pen.fd(120)



#red-light
red_light =turtle.Turtle()
red_light.shape("circle")
red_light.color("grey")
red_light.penup()
red_light.goto(0, 40)

#Yellow-light
yellow_light =turtle.Turtle()
yellow_light.shape("circle")
yellow_light.color("grey")
yellow_light.penup()
yellow_light.goto(0, 0)

#Green-light
green_light =turtle.Turtle()
green_light.shape("circle")
green_light.color("grey")
green_light.penup()
green_light.goto(0, -40)

while True:
    yellow_light.color("grey")
    red_light.color("red")
    print("Red light on - Now vehicle are Prohibited to go. ")
   # print("Red Light Blinked")
    time.sleep(1)
    print("Red Light Blinked")

    red_light.color("grey")
    green_light.color("lime green")
    print("Green light on - Now vehicle can go.")
   # print("Green Light Blinked")
    time.sleep(1)
    print("Green Light Blinked")

    green_light.color("grey")
    yellow_light.color("yellow")
    print("Yellow light on - Now vehicle Ready to go.")
    #print("Yellow Light Blinked")
    time.sleep(1)
    print("Yellow Light Blinked")
    break