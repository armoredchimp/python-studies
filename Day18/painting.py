import colorgram

colors = colorgram.extract('Ault abandoned cabin.png', 6)


rgb_colors = []


for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)
