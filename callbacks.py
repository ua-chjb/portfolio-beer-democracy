from dash import Input, Output
from load_data import beer, dem, pop
from charts import fig_B_bubblechart, fig_C_scatter, fig_D_top_line_dem, fig_E_top_line_beer
from color import scientific_layout


def callbacks_baby(app):
    @app.callback(
        Output(component_id="comp2_FIGfig_statchart", component_property="figure"),
        Output(component_id="comp3_FIGfig_demchart", component_property="figure"),
        Output(component_id="comp4_FIGfig_beerchart", component_property="figure"),
        Input(component_id="comp5_SELECTselect_year", component_property="value")
    )
    def aragorn_returns(years):
        year1 = years[0]
        year2 = years[1]
        return scientific_layout(fig_C_scatter(beer, dem, year1, year2)), scientific_layout(fig_D_top_line_dem(dem, "Average", year1, year2)), scientific_layout(fig_E_top_line_beer(beer, "Average", year1, year2))
    @app.callback(
        Output("comp1_FIGfig_bubb", "figure"),
        Input("comp0_SELECTselect_country", "value")
    )
    def impossible_excl(countries):

        fig = scientific_layout(fig_B_bubblechart(beer, dem, pop))

        if not countries:
            pass
        else:
            for country in countries:
                ann_x = beer[2017][beer.index == country].values
                ann_y = dem[2017][dem.index == country].values
                label = country

                print(ann_x, ann_y)

                ann = {
                    "x": ann_x[0],
                    "y": ann_y[0],
                    "text": label,
                }
                fig.add_annotation(ann)


        return fig