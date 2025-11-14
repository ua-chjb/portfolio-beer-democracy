import pandas as pd
import numpy as np

from dash import html, dcc, _dash_renderer
import dash_mantine_components as dmc
from dash_iconify import DashIconify
_dash_renderer._set_react_version('18.2.0')

import plotly.express as px
import plotly.graph_objs as go

from load_data import beer, dem, pop
from charts import fig_A_heatmap
from color import scientific_layout

# # # # # # # # # # # # # # # # block0 # # # # # # # # # # # # # # # # # # #

comp0_select_country = dmc.Card(
    [
        dmc.MultiSelect(
            label="COUNTRY",
            placeholder="select...",
            data=beer.index,
            searchable=True,
            clearable=True,
            maxValues=20,
            id="comp0_SELECTselect_country",
            comboboxProps={"w": "100%"},
            className="k"
        ),
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp0_select_country"
)

comp0point5_text_des = dmc.Card(
    [
        dmc.Text(
            "correlation, not causation",
            fw=500,
            size="l",
            className="text_subheader"
        ),
        dmc.Text(
            [
            """This data is gathered from the World Happiness Report """,
            dmc.Anchor("(WHR)", href="https://worldhappiness.report/data/", target="_blank"),
            """, """,
            dmc.Anchor(" Our World in Data", href="https://ourworldindata.org/", target="_blank"),
            """, and""",
            dmc.Anchor(" Statista", href="https://www.statista.com/", target="_blank"),
            """, merged by country."""
            ],
            c="gray",
            size="sm",
            className="text_standard"
        ),
        dmc.Text (
            """It is important to note that "correlation does not equal causation." There is likely a colinear variable such as "Quality of Life" that better explains the relationship.""",
            c="gray",
            size="sm",
            className="text_standard"
        ),
        dmc.Text (
            """Still - cheers to world happiness!""",
            c="gray",
            size="sm",
            className="text_standard"
        ),

    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp0point5_text_des"
)

exp_inl = html.Div(
    [
        comp0_select_country,
        comp0point5_text_des
    ],
    className="inline"
)

comp1_fig_bubb = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp1_FIGfig_bubb", style={"height": "80vh",})
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp1_fig_bubb"
)

block0 = html.Div(
    [
        exp_inl,
        comp1_fig_bubb
    ],
    className="d d0"
)

# # # # # # # # # # # # # # # # block1 # # # # # # # # # # # # # # # # # # #

comp2_fig_statchart = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp2_FIGfig_statchart")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp2_fig_statchart"
)

comp3_fig_demchart = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp3_FIGfig_demchart")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp3_fig_demchart"
)

comp4_fig_beerchart = dmc.Card(
    [
        dcc.Graph(figure={}, id="comp4_FIGfig_beerchart")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp4_fig_beerchart"
)

comp5_select_year = dmc.Card(
    [
        dcc.RangeSlider(
            min=2008,
            max=2018,
            step=1,
            marks=dict(zip( range(2008, 2019, 2), [str(k) for k in range(2008, 2019, 2)] )),
            value=[2008, 2018],
            id="comp5_SELECTselect_year"
        )
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp5_select_year"
)

block1 = html.Div(
    [
        comp2_fig_statchart,
        comp3_fig_demchart,
        comp4_fig_beerchart,
        comp5_select_year
    ],
    className="d d1"
)

# # # # # # # # # # # # # # # # block2 # # # # # # # # # # # # # # # # # # #

comp6_fig_heatmap = dmc.Card(
    [
        dcc.Graph(figure=scientific_layout(fig_A_heatmap()), id="comp6_fig_heatmap")
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t comp6_fig_heatmap"
)


block2 = html.Div (
    [
        comp6_fig_heatmap
    ],
    className="d d2"
)


# # # # # # # # # # # # # # footer # # # # # # # # # # # # # #
color = "white"

icon_github = DashIconify(icon="simple-icons:github", width=30, color=color, className="bb")
link_github = "https://www.github.com/ua-chjb"
icon_linkedin = DashIconify(icon="devicon-plain:linkedin", width=30, color=color, className="bb")
link_linkedin = "https://linkedin.com/in/benjaminbnoyes"
icon_email = DashIconify(icon="mdi:email", width=30, color=color, className="bb")
link_email = "mailto:noyesbenjamin@gmail.com"
icon_spotify = DashIconify(icon="cib:spotify", width=30, color=color, className="bb")
link_spotify = "https://open.spotify.com/playlist/2s1oHEgwqxVKoqNdOC1Zs4?si=17fbc35fb4c9421c"
icon_soundcloud = DashIconify(icon="cib:soundcloud", width=40, color=color, className="bb")
link_soundcloud = "https://soundcloud.com/bennoyes-onb"  


comp20_footer0_github = dmc.Anchor(
    icon_github, href=link_github, target="_blank", 
    size="xl",
    className="footnt comp20_footer0_github"
)

comp21_footer1_linkedin = dmc.Anchor(
    icon_linkedin, href=link_linkedin, target="_blank", 
    size="xl",
    className="footnt comp21_footer1_linkedin"
)

comp22_footer2_email = dmc.Anchor(
    icon_email, href=link_email, target="_blank", 
    size="sm",
    className="footnt comp22_footer2_email"
)

comp23_footer3_spotify = dmc.Anchor(
    icon_spotify, href=link_spotify, target="_blank", 
    size="xl",
    className="footnt comp23_footer3_spotify"
)

comp24_footer4_soundcloud = dmc.Anchor(
    icon_soundcloud, href=link_soundcloud, target="_blank",
    size="xl",
    className="footnt comp24_footer4_soundcloud"
)

comp25_copyrightfooter = html.P(
    "© Benjamin Noyes 2024 all rights reserved",
    className="footertinytext"
)

footer = dmc.Card(
    [
        comp20_footer0_github,
        comp21_footer1_linkedin,
        comp22_footer2_email,
        comp23_footer3_spotify,
        comp24_footer4_soundcloud,
        comp25_copyrightfooter
    ],
    withBorder=True,
    shadow="sm",
    radius="md",
    className="t f"
)

# # # # # # # # # # # # # # title # # # # # # # # # # # # # #


title = dmc.Card(
    [
        dmc.Text(
            "beer: for democracy",
            size="xl",
            fw=600
            )
    ],
    className="t tit",
    withBorder=True,
    shadow="sm",
    radius="md",
)

# # # # # # # # # # # # # # # # composition # # # # # # # # # # # # # # # # # # #


lyt = dmc.MantineProvider(
    [
        title,
        block0,
        block1,
        block2,
        footer
    ]
)