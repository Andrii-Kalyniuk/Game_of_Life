from flask import Flask

from generation_zero_patterns import glider_raw
from life import show_generations, extend_playground, str_2_list_playground

app = Flask(__name__)


@app.route('/')
def get_home():
    glider_gen = str_2_list_playground(glider_raw)
    glider_gen = extend_playground(glider_gen,
                                   lines=1, columns=1,
                                   lines_before=1, cols_before=1)
    return show_generations(glider_gen, 1, ignore_borders=True)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=5000)
