"""App = Flask(__name__)
@App.route("/")
def Home_Page():
    return '''
            <p>Who is the greatest of all time. Enter 1 for Messi, 0 for Ronaldo: </p>
            <form action="/" method = "POST">
            <label for="lname">Fooballer_score:</label>
            <input type="text" id="lname" name="lname"><br><br>
            <input type="submit" value="Submit">
            </form>'''

@App.route("/",methods = ["POST"])
def submit_score():
    result = {"Messi":0, "Ronaldo":0}
    score = None 
    if request.method == "POST":
        score == request.form["lname"]
        #name == request.form["Fooballer_Name"]
        if score == 0:
            result["Messi"] += 1
        else:
            result["Ronaldo"] += 1
w
    x = result.keys()
    y = result.values()
    fig, ax = plt.subplots()
    plt.bar(x,y)
    fig.savefig('my_plot.png')
    #plt.show()
    #return "<img src='my_plot.png'/>"
    return "testing"""

"""s = pd.Series([1, 2, 3])
fig, ax = plt.subplots()
s.plot.bar()
fig.savefig('my_plot.png')


<img src='my_plot.png'/>"""



'''def selecting_greatness():

    players = {"Messi":0, "Ronaldo":0}
    while players["Messi"] < 3 or players["Ronaldo"] < 3:
        
        if players["Messi"] >= 3 or players["Ronaldo"] >= 3:
            break
        user = input("Who is the greatest of all time. Enter 1 for Messi, 0 for Ronaldo: " )
        if int(user) == 1:
            players["Messi"] += 1
        else:
            players["Ronaldo"] += 1
        print(f"Messi scored: {players["Messi"]} and Ronaldo scored {players["Ronaldo"]}")
    # = "Messi wins" if players["Messi"] > players["Ronaldo"] else "Ronaldo wins"

    df = pd.DataFrame([players])
    print(df)
    x = ["Messi", "Ronaldo"]
    y = [players["Messi"], players["Ronaldo"]]
    plt.bar(x,y)
    plt.show()


print(selecting_greatness())'''
 