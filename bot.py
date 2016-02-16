from twitter import *
import sys

from time import strftime

Consumer = ""
ConsumerSecret = ""
AccessToken = ""
AccessTokenSecret = ""
t = Twitter(auth=OAuth(AccessToken, AccessTokenSecret, Consumer, ConsumerSecret))
t.statuses.update(status="I'm back online! %s #RaspberryPi #IoT #Dev #PythonBot"% strftime("%Y-%m-%d %H-%M-%S"))
sys.exit(0)


