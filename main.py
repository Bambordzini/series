from flask import Flask, render_template, url_for
from data import queries
import math
from dotenv import load_dotenv

load_dotenv()
app = Flask("codecool_series")


@app.route("/")
def index():
    shows = queries.get_shows()
    return render_template("index.html", shows=shows)




@app.route("/design")
def design():
    return render_template("design.html")


@app.route("/shows/most-rated")
@app.route("/shows/most-rated/<int:page_number>")
def shows_most_rated(page_number=1):
    print(page_number)
    number_of_elements_to_display = 15
    total_number_of_shows = queries.get_total_number_of_shows()[0]["total_rows"]
    most_rated_shows_list = queries.get_most_rated_shows(
        number_of_elements_to_display, page_number
    )
    total_number_of_pages = math.ceil(
        total_number_of_shows / number_of_elements_to_display
    )
    return render_template(
        "most-rated-shows.html",
        most_rated_shows_list=most_rated_shows_list,
        total_number_of_pages=total_number_of_pages,
        current_page=page_number,
    )


@app.route("/show/<int:id>")
def show(id):
    show_detail = queries.get_show(id)
    print(show_detail)    
    return render_template ("show_detail.html", show=show_detail)


def main():
    app.run(debug=False)


if __name__ == "__main__":
    main()
