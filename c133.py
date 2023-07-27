import pandas as pd
import plotly.express as px

df = pd.read_csv('star_with_gravity.csv')
radius_list = df['Radius'].tolist()
mass_list = df['Mass'].tolist()
threshold = 1.0  # Mass in solar masses
similar_mass_indices = [i for i, mass in enumerate(mass_list) if abs(mass - 1.0) <= threshold]
similar_mass_radius = [radius_list[i] for i in similar_mass_indices]
similar_mass_mass = [mass_list[i] for i in similar_mass_indices]
fig = px.scatter(x=similar_mass_mass, y=similar_mass_radius, labels={'x': 'Mass (Solar Masses)', 'y': 'Radius (Solar Radii)'})

fig.show()
