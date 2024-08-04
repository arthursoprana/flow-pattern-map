from ipywidgets import widgets, Layout

continuous_update = True

layout = Layout(width='50%', justify_content ='space-between',  align_content='space-around')

ρ_L_button = widgets.FloatSlider(
    min=800.0,
    max=1200.0,
    value=1000.0,
    step=0.5,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Liquid Density [kg/m3]',
    layout=layout
)

ρ_G_button = widgets.FloatSlider(
    min=0.5,
    max=300.0,
    value=2.0,
    step=0.5,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Gas Density [kg/m3]',
    layout=layout
)

# Viscosity
μ_L_button = widgets.FloatSlider(
    min=1e-3,
    max=1e-2,
    value=1e-3,
    step=1e-5,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Liquid Viscosity [Pa.s]',
    readout_format='.2e',
    layout=layout
)

μ_G_button = widgets.FloatSlider(
    min=1e-5,
    max=1e-3,
    value=1e-5,
    step=1e-6,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Gas Viscosity [Pa.s]',
    readout_format='.2e',
    layout=layout
)

# Surface Tension
σ_button = widgets.FloatSlider(
    min=0.01,
    max=0.10,
    value=0.07,
    step=0.001,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Surface Tension [N/m]',
    layout=layout
)

# Pipe Diameter
D_button = widgets.FloatSlider(
    min=0.001,
    max=0.60,
    value=0.1,
    step=0.001,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Pipe Diameter [m]',
    readout_format='.3f',
    layout=layout
)

# Pipe Inclination
θ_button = widgets.FloatSlider(
    min=0.0,
    max=90.0,
    value=0.0,
    step=0.5,
    continuous_update=continuous_update,
    orientation='horizontal',
    description='Pipe Inclination [deg]',
    layout=layout
)

# Pipe Roughness
k_s_button = widgets.FloatSlider(
    min=0.0,
    max=1e-3,
    value=1e-5,
    step=1e-6,
    continuous_update=continuous_update,
    description='Pipe Roughness [m]',
    readout_format='.2e',
    layout=layout
)

interface_button = widgets.Dropdown(
    options={'Smooth': 1, 'Wavy': 2},
    value=1,
    description='Interface:',
    layout=layout
)

# Pipe Roughness
k_s_button = widgets.FloatSlider(
    min=0.0,
    max=1e-3,
    value=1e-5,
    step=1e-6,
    continuous_update=continuous_update,
    description='Pipe Roughness [m]',
    readout_format='.2e',
    layout=layout
)

# Superficial velocity
us_G_button = widgets.FloatSlider(
    min=1e-3,
    max=100.0,
    value=0.1,
    step=1e-3,
    continuous_update=continuous_update,
    description='Gas Superficial Velocity [m/s]',
    readout_format='.3f',
    layout=layout
)

us_L_button = widgets.FloatSlider(
    min=1e-3,
    max=100.0,
    value=0.01,
    step=1e-3,
    continuous_update=continuous_update,
    description='Liquid Superficial Velocity [m/s]',
    readout_format='.3f',
    layout=layout
)