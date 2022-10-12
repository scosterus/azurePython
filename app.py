from flask import Flask
import mysql.connector
from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

db = mysql.connector.connect(
    host = "bigdata-database.mysql.database.azure.com",
    port = "3306",
    user = "bigData",
    password = "qwer1234QWER!@#$",
    database = "skillapp"
    )

mycursor = db.cursor()

# @app.route("/")
# def index():
#     return "hallo"

# When this URL is called, the function intro() will run
# The function intro() will create a new item in the database with the parameters given in the URL
# The function will return the id of the newly created user
# So when the URL is called, an id will be returned
@app.route("/intro/<vnaam>/<age>")
def intro(vnaam,age):
    # create new item in database, assign values name and age
    mycursor.execute("INSERT INTO users (name, age) VALUES ('%s', '%s')" % (vnaam, age))
    db.commit()
    # get corresponding id of new user from the database and assign it to variable id
    mycursor.execute("SELECT MAX(ID) FROM users")
    id = mycursor.fetchone()[0]
    print(id, vnaam, age, "added")
    # let this function return the id, so when this function is called you will get the id back
    return str(id)


@app.route("/fits/<country>/<education>/<job>/<email>/<password>/<data>")
def fits(country, education, job, email, password, data):
    mycursor.execute("INSERT INTO users (country, education, job, email, password) VALUES ('%s', '%s','%s','%s','%s') WHERE id = '%s''" % (country, education, job, email, password, data))
    db.commit()
    print("fits added!")
    return 'fits.html'

@app.route("/home")
def home():
    return 'home.html'


@app.route("/quiz/<qid>")
def quiz(qid):
    
    questions_string = {
        "1": "endurance;Your friends asks you if you\'d like to sign up for a charity run with them. What do you say?;\
            You\'ll cheer them on from the sidelines.;If it\'s no more than 5 km, you\'ll consider it.;Absolutely!",
        "2": "strength;You are helping your friends with moving to their new appartment. What kind of stuff would you prefer to carry?;\
            The plants and other light stuff;The heavier moving Boxes;Carrying the couches and fridge",
        "3": "power;You are at a theme park where you can win prizes by shooting or throwing the ball really hard. How many prices could you win?;\
            Participating is more important than winning;Winning the small prices;Getting all the big prices",
        "4": "speed;If you would descripe your speed in the form of animals, which animal would you been?;\
            A Tortoise;A rabbit;A cheetah",
        "5": "agility;If we refer to the movement of your body, how would you describe it?;\
            I don't move easily and I am not quick;I move easily but I am not really quick;I move easy and quick",
        "6": "flexibility;If you were to take a yoga class, what would it look like?;\
            Nope;Doing alright;Master",
        "7": "nerve;How do you feel about adrenaline sports?;\
            Nope nope nope;Rollercoasters are fine but skydiving is a bit much;Skydiving is my biggest dream",
        "8": "durability;How do you feel about adrenaline sports?;\
            Nope nope nope;Rollercoasters are fine but skydiving is a bit much;Skydiving is my biggest dream",
        "9": "hand-eye coordination;When someone throws you a ball, you are confident you'll catch it.;\
            Nervous, you're not usually good at catching things;Focused, you'll probably catch it if you pay attention;Yes!",
        "10": "analytical aptitude;Are you comfortable with making fast important decissions under pressure for yourself or a group?;\
            I am bad at making fast descissions under pressure;I am oke with it if it's at least for my own businesses;I can take the pressure and do what is the best for myself and the group"
    }

    data = questions_string[qid]
    return str(data)

