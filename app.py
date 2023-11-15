import flask
import os
import subprocess

app = flask.Flask(__name__)

@app.route("/")
def get_ros2_topic_list():
    # I hope current environment can run ros2 commands!
    env_var = os.environ.copy()
    command = "ros2 topic list"

    proc = subprocess.run(
        command,
        shell=True,
        text=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        env=env_var
    )
    topics = {"no_slash": []}
    for topic in proc.stdout.split("\n"):
        if topic == '': # empty string
            continue

        topic_slice = topic.split("/")
        if topic_slice[0] == "": # topic starts with /, like /sensing/lidar...
            if topic_slice[1] not in topics:
                topics[topic_slice[1]] = []
            topics[topic_slice[1]].append(topic)
        else: # topic starts without /, like cmd_vel
            topics["no_slash"].append(topic)

    return flask.render_template("index.html", topics=topics)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
