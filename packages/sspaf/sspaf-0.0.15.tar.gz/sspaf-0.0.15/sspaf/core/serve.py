import os
import time
import flask
import threading
from sspaf.core import render
import waitress
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class ChangeDetector(FileSystemEventHandler):
    def __init__(self, path: str):
        super().__init__()
        self.path = path
        self.last_modified = {}
        self.stop = False

    def on_any_event(self, event):
        render.render(self.path)

    @staticmethod
    def run(path: str):
        event_handler = ChangeDetector(path)
        observer = Observer()
        observer.schedule(event_handler, path, recursive=True)
        
        observer.start()
        try:
            while not event_handler.stop:
                time.sleep(1)
        except KeyboardInterrupt:
            observer.stop()
        except:
            pass
        observer.join()

def serve(output_path: str) -> None:
    if output_path == ".":
        output_path = os.getcwd()

    print(f'Serving project {output_path}')

    app = flask.Flask(__name__, static_folder=os.path.join(output_path, 'output'))

    @app.route('/sspaf.js')
    def send_sspaf():
        return flask.send_file(output_path + '/output/sspaf.js')
    
    # jsons
    @app.route('/<path:path>.json')
    def send_json(path):
        return flask.send_file(output_path + '/output/' + path + '.json')

    @app.route('/')
    def send_index():
        return flask.send_file(output_path + '/output/index.html')

    @app.route('/<path:path>')
    def send_page(path):
        return flask.send_file(output_path + '/output/' + path)

    t = threading.Thread(target=ChangeDetector.run, args=(output_path,))
    t.start()
    render.render(output_path)
    print(f"Starting server on http://localhost:8080/")
    os.system("start http://localhost:8080/")
    waitress.serve(app, host='127.0.0.1', port=8080)

    t.stop = True
    t.join()