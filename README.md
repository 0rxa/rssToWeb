#### Pyrana Earthquake Hackathon

## Currently
This is the product of pulling an all nighter to fix your infrastructure and then deciding to change it.
It is a flask web server which takes post requsts which must contain an rss feed. It parses the rss feed
and converts uses its data to populate a database which stores every earthquake instance detected. To send
the rss feed we've used the utility entr to stat the rss feed file and every time it changes to send the data
to the web server.

## In production
We obviously won't be installing such an over-engineered solution. We'll just make a python script to monitor
the file and send the data when necessary.
