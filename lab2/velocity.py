velocity_car_1 = 80
velocity_car_2 = 70
at_the_beginning_distance= 490
at_the_end_distance = 150
duration_hour = (at_the_beginning_distance-at_the_end_distance)/(velocity_car_1+velocity_car_2)
duration_minutes = duration_hour*60
print(duration_minutes)