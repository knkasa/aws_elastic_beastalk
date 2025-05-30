'''
my_dash_app/
│── application.py       # WSGI entry point (required by Elastic Beanstalk)
│── app.py               # Your Dash application
│── requirements.txt     # List of Python dependencies
│── .ebextensions/       # (Optional) Configuration files for Elastic Beanstalk
│── Procfile             # (Optional) Defines the startup command
│── Dockerrun.aws.json   # (Optional) If using a Docker container

1. zip the my_dash_app.  Open Elastic beanstalk in AWS, upload the zip file.
2. During setup, for "EC2 instance profile", if the app needs to access like s3, you will need to create a role with EC2 service & s3 policies. Attach it here.
3. For instance profile, create a role for EC2 service with AWSElasticBeanstalkMulticontainerDocker, AWSElasticBeanstalkWebTier, AWSElasticBeanstalkWorkerTier policies.
4. In last page, for Environment properties, use the default Name and Value. (you'll need this if your app using python, for package management)

'''

import dash
from dash import dcc, html
import flask

server = flask.Flask(__name__)
app = dash.Dash(__name__, server=server)

app.layout = html.Div([
    html.H1("My Dash App on AWS"),
    dcc.Graph(
        figure={
            "data": [{"x": [1, 2, 3], "y": [4, 1, 2], "type": "bar"}],
            "layout": {"title": "Sample Graph"}
        }
    )
])

if __name__ == "__main__":
    server.run(debug=True, host="0.0.0.0", port=5000)
