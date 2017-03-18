from github import Github
from github import UnknownObjectException
from flask import Flask
from github import RateLimitExceededException
import sys

app = Flask(__name__)
command_line_arguement = sys.argv[1].split("/")

for n in range(len(command_line_arguement)):
    if "github" in command_line_arguement[n]:
        username = command_line_arguement[n+1]
        repository = command_line_arguement[n + 2]
        break

if n==len(command_line_arguement):
    git_hub = "invalid url"

try:
    git_hub = Github().get_user(username).get_repo(repository)
except UnknownObjectException:
    git_hub = "repository does not exist. Please check link supplied"
except Exception as e:
    git_hub = "err : %s" % e


def response(file_configuration):
    try:
        return git_hub.get_file_contents(file_configuration).content.decode(git_hub.get_contents(file_configuration).encoding)
    except UnknownObjectException as e:
        return "exception : File not found"
    except RateLimitExceededException:
        return "exception : git rate limit reached"
    except Exception as e:
        return "exception occured: %s" % e

@app.route("/v1/<config_file>")
def controller(config_file):
    if isinstance(git_hub, basestring):
        return git_hub
    else:
        return response(config_file)

if __name__ == "__main__":
    app.config["url"] = sys.argv[1]
app.run(debug=True,host='0.0.0.0')
