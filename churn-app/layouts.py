import dash_core_components as dcc
import dash_html_components as html
import dash_bootstrap_components as dbc

theme = {'font-family': 'Raleway', 'background-color': '#caf1de'}


def graph_1():
    graph = dbc.Row([
        dbc.Col(
            dcc.Graph(id='Graph1',
                      ),
            width={"size": 14, "offset": 0},
            md={"size": 10, "offset": 1},
            lg={"size": 6, "offset": 0}),
        dbc.Col(
            dcc.Graph(id='Graph4',
                      ),
            width={"size": 14, "offset": 0},
            md={"size": 10, "offset": 1},
            lg={"size": 6, "offset": 0}),
    ])
    return [graph]


def graph2_3():
    graph_2 = dbc.Col(html.Div(
        dcc.Graph(id='Graph2',
                  )),
        width={"size": 14, "offset": 0},
        md={"size": 10, "offset": 3},
        lg={"size": 4, "offset": 0})

    graph_5 = dbc.Col(html.Div(
        dcc.Graph(id='Graph5',
                  )),
        width={"size": 14, "offset": 0},
        md={"size": 10, "offset": 0},
        lg={"size": 4, "offset": 0})
    graph_3 = dbc.Col(html.Div(
        dcc.Graph(id='Graph3',
                  )),
        width={"size": 14, "offset": 0},
        md={"size": 10, "offset": 0},
        lg={"size": 4, "offset": 0})

    # Return of the graphs in all the row
    return dbc.Row([graph_2, graph_3, graph_5])


def create_footer():
    p = html.P(
        children=[
            html.Span('Developed By: '),
            html.A('Akash, Rushikesh, Sachin and Prathamesh',
                   style={'text-decoration': 'none', 'color': '#ffffff'})
        ], style={'float': 'right', 'margin-top': '8px',
                  'font-size': '15px', 'color': '#ffffff'}
    )

    span_style = {'horizontal-align': 'right',
                  'padding-left': '1rem',
                  'font-size': '15px',
                  'vertical-align': 'middle'}

    datatables = html.A(
        children=[
            html.I([]),
            html.Span('Machine Learning Project', style=span_style)
        ], style={'text-decoration': 'none', 'color': '#ffffff', 'margin-right': '20px'}, target='_blank')

    ul1 = html.Div(
        children=[
            html.Li(datatables, style={
                    'display': 'inline-block', 'color': '#ffffff'}),
        ],
        style={'list-style-type': 'none', 'font-size': '30px'},
    )


    li_right_first = {'line-style-type': 'none', 'display': 'inline-block'}
    li_right_others = {k: v for k, v in li_right_first.items()}
    li_right_others.update({'margin-left': '10px'})
    div = html.Div([p, ul1])

    footer_style = {
        'font-size': '2.2rem',
        'background-color': '#F1948A',
        # 'padding': '2.5rem',
        'margin-top': '3rem',
        'display': 'inline-block', 'padding': '16px 32px 8px'
    }
    footer = html.Footer(div, style=footer_style, className='twelve columns')
    return footer


def header_logo():
    h1_title = html.Div(
        children='Customer Churn Prediction',
        className="font-xl bold bottom16 margin-auto",
    )
    subtitle = html.Div(html.Div([html.Span("Churn rate ", className="bold"),
            ' is like a "break-up" measure between a company and its customers.\
                It shows the percentage of customers who end their relationship with the company by canceling their service within a certain time.\
                    This could happen because customers are unhappy, find better deals elsewhere, or the competition does a better job at attracting them.\
                        It is a sign that the company might need to improve its services, pricing, or how it markets to customers.'], className="font-md margin-auto"))
    return [h1_title, subtitle]



def paragraphs():
    div = html.Div("Revenue Churn",

                   className="font-xl bold bottom16 margin-auto",
                   )
    paragra = html.Div(html.Div([html.Span("Revenue churn ", className="bold"), "is the monetary amount of \
        recurring revenue lost in a period divided by the total revenue at the beginning of \
            the period. Revenue churn is commonly used in Software as a Service (SaaS) \
                and other business models that rely on recurring revenue models."]),
                       className="font-md bottom32 margin-auto"
                 
                       )

    return [div, paragra]
