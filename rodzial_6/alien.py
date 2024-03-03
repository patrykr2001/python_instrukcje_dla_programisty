alien_0 = {'color': 'green', 'points': 5}

new_points = alien_0['points']
print(f"Zdobyłeś {new_points} punktów!")

alien_0['x_position'] = 0
alien_0['y_position'] = 25
print(alien_0)

alien_0['color'] = 'żółty'
print(alien_0)

del alien_0['points']
print(alien_0.get('points', 'Brak przypisanych punktów'))
