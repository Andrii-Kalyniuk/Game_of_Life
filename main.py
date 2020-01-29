from flask import Flask

from generation_zero_patterns import glider_raw
from life import show_generations, extend_playground, str_2_list_playground

app = Flask(__name__)


@app.route('/')
@app.route('/<int:steps>')
def get_home(steps=0):
    glider_gen = str_2_list_playground(glider_raw)
    glider_gen = extend_playground(glider_gen,
                                   lines=3, columns=3,
                                   lines_before=3, cols_before=3)
    generation = show_generations(glider_gen, number_of_gen=steps, ignore_borders=True)
    # TODO: add template.html
    return f"<table border=1px solid black><tr><td style='font-family: mono'>{generation}</td><tr></table>"


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
