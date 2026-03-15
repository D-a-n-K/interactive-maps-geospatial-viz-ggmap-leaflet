from shiny import App, render, ui
import numpy as np
import matplotlib.pyplot as plt

# Define UI
app_ui = ui.page_fluid(
    ui.panel_title("PyShiny"),
        ui.page_sidebar(
    ui.sidebar(
            ui.input_slider("bins", "Number of bins:", min=1, max=50, value=30)
        ),
            ui.output_plot("distPlot")
        )
    )


# Define server logic
def server(input, output, session):
    @output
    @render.plot
    def distPlot():
        # Generate random data similar to Old Faithful waiting times
        # (In R Shiny this uses the built-in faithful dataset)
        np.random.seed(42)
        x = np.random.normal(70, 13, 272)
        
        # Create histogram with specified number of bins
        fig, ax = plt.subplots()
        ax.hist(x, bins=input.bins(), color='darkgray', edgecolor='white')
        ax.set_xlabel('Waiting time to next eruption (in mins)')
        ax.set_ylabel('Frequency')
        ax.set_title('Histogram of waiting times')
        return fig

# Create the app
app = App(app_ui, server)