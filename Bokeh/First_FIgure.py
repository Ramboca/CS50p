# Bokeh Libraries
from tkinter import N
from bokeh.io import output_file
from bokeh.plotting import figure, show

# render the static HTML to file called out_file
output_file('output_file_test.html', title='Empty Bokeh figure')

# set up a geneic figure()object
fig = figure(background_fill_color='gray',
             background_fill_alpha=0.5,
             border_fill_color='blue',
             border_fill_alpha=0.25,
             plot_height=300,
             plot_width=500,
             x_axis_label='X Label',
             x_axis_type='datetime',
             x_axis_location='above',
             x_range=('2018-01-01', '2018-06-30'),
             y_axis_label='Y Label',
             y_axis_type='linear',
             y_axis_location='left',
             y_range=(0, 100),
             title='Example Figure',
             title_location='right',
             toolbar_location='below',
             tools='save')
# remove the grid color
fig.grid.grid_line_color = None
# See what it look like
show(fig)

