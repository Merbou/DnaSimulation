import pandas as pd
import pandas_bokeh


class chart():

    def __init__(self, data):
        """
        @params dict
        init Data
        @return Object
        """
        self.__data = data

    def histo_chart(self, index, typeGraph, ylabel, title):
        """
        @parms String,String,String,String
        View histogram chart 
        @return None
        """
        df = pd.DataFrame(self.__data).set_index(index)

        df.plot_bokeh(
            kind=typeGraph,
            ylabel=ylabel,
            title=title,
            figsize=(1300, 650),
            alpha=0.6)

    def pie_chart(self, title):
        """
        @parms String
        View peizza chart
        @return None
        """
        df = pd.DataFrame(self.__data)
        df.plot_bokeh.pie(
            x="Nucleotide",
            colormap=["grey", "blue"],
            title=title,
            line_color="purple",
            figsize=(1200, 700)
        )
