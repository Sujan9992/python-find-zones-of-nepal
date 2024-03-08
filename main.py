from turtle import Turtle, _Screen, shape

from pandas import DataFrame, read_csv

screen: _Screen = _Screen()
screen.title("Name all the districts")
image_path: str = "Zones of Nepal\map.gif"
screen.addshape(image_path)
shape(image_path)

zone_series_df: DataFrame = read_csv("Zones of Nepal\zones.csv")
zones_list: list = zone_series_df.zone.to_list()

correct_answer: list[str] = []
while len(correct_answer) < 14:
    answer: str = (
        screen.textinput(
            title=f"{len(correct_answer)}/14 Correct", prompt="Input the zone nepal"
        )
        or ""
    )  # Handle None case by providing default empty string value
    answer = answer.lower()
    if answer in zones_list:
        correct_answer.append(answer)
        zone_series_data = zone_series_df[zone_series_df.zone == answer]
        turtle = Turtle()
        turtle.color("red")
        turtle.hideturtle()
        turtle.penup()
        turtle.goto(int(zone_series_data.x), int(zone_series_data.y))
    turtle.write(answer.title())
