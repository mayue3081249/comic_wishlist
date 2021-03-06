from comic_wishlist import db
from comic_wishlist.models import Colors
from datetime import datetime as dt

colors = {
    'steel': ['#14213d', '#fca311', '#282e3c', '#fca311', '#284b63'],
    'blue': ['#7EA3CC', '#B3001B', '#262626', '#255C99', '#CEDFF3'],
    'pink': ['#b7b7a4', '#cb997e', '#a5a58d', '#eddcd2', '#fff1e6'],
    'green': ['#588b8b', '#c8553d', '#e29578', '#ffddd2', '#83c5be'],
    'yellow': ['#fcbf49', '#f95738', '#083d77', '#083d77', '#ebebd3']
}

def add_color():
    for k, v in colors.items():
        color = Colors(name=k, selected=False, bgcolor=v[0], primary=v[1],
                      secondary=v[2], third=v[3], mute=v[4])
        db.create_all()
        db.session.add(color)

        db.session.add(color)
        db.session.commit()


def retrieve_oldest_comic_date(comics):
    dates = []
    for name, comic in comics.items():
        for title, issues in comic.items():
            for issue in issues:
                if 'date' in issue:
                    if issue['date'] is not None:
                        dates.append(int(issue['date'].split('-')[0]))
    dates = sorted(dates)
    return dates[0]

def generate_date_options(oldest_comic_year):
    current_year = int(dt.now().strftime('%Y'))
    return [x for x in range(oldest_comic_year, current_year + 1)]


