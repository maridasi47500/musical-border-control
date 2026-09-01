from flask import Flask, render_template, request, session, redirect
from myplace import Myplace
from bs4 import BeautifulSoup
import subprocess
import os
from yourappdb import query_db, get_db
from flask import g

app = Flask(__name__)
app.secret_key="any string"
def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()
init_db()

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

@app.route("/")
def hello_world():
    user = query_db('select * from contacts')
    the_username = "anonyme"
    one_user = query_db('select * from contacts where first_name = ?',
                [the_username], one=True)
    return render_template("hey.html", users=user, one_user=one_user, the_title="my title")
@app.route("/add_one_user", methods=["GET","POST"])
def add_one_user():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into user (username,email,password,country_id,phone) values (:username,:email,:password,:country_id,:phone)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from user')


        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        session["current_user_id"]=last_user["id"]
        for x in ['username','email','password','country_id','phone']:
            session[x]=hey[x]


        return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from user')
    one_user = query_db("select * from user limit 1", one=True)
    return render_template("userform.html", users=user, one_user=one_user, the_title="add new user", touslescountry=touslescountry)


@app.route("/user_sign_out", methods=["GET","POST"])
def user_sign_out():
    if request.method == 'POST':
        session["current_user_id"]=""
        for x in ['username','email','password','country_id','phone']:
            session[x]=""
        return redirect("/")


@app.route("/user_log_in", methods=["GET","POST"])
def user_login():
    if request.method == 'POST':
        hey=request.form
        last_user = query_db("select * from user where email = ? and password = ?",[hey["email"], hey["password"]], one=True)
        try:
            session["current_user_id"]=last_user["id"]
            for x in ['username','email','password','country_id','phone']:
                session[x]=hey[x]
        except:
            return render_template("userlogin.html")
    return render_template("userlogin.html")
@app.route("/add_one_custom_officer", methods=["GET","POST"])
def add_one_custom_officer():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescountry= query_db("select * from country")

        one_user = query_db("insert into custom_officer (name,country_id) values (:name,:country_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from custom_officer')


        return render_template("custom_officerform.html", custom_officers=user, one_user=one_user, the_title="add new custom_officer", touslescountry=touslescountry)


    touslescountry= query_db("select * from country")

    user = query_db('select * from custom_officer')
    one_user = query_db("select * from custom_officer limit 1", one=True)
    return render_template("custom_officerform.html", custom_officers=user, one_user=one_user, the_title="add new custom_officer", touslescountry=touslescountry)

@app.route("/add_one_country", methods=["GET","POST"])
def add_one_country():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into country (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from country')


        return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")


    user = query_db('select * from country')
    one_user = query_db("select * from country limit 1", one=True)
    return render_template("countryform.html", countrys=user, one_user=one_user, the_title="add new country")

@app.route("/add_one_customofficierhasuser", methods=["GET","POST"])
def add_one_customofficierhasuser():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslescustom_officer= query_db("select * from custom_officer")

        touslesuser= query_db("select * from user")

        one_user = query_db("insert into customofficierhasuser (custom_officer_id,user_id) values (:custom_officer_id,:user_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from customofficierhasuser')


        return render_template("customofficierhasuserform.html", customofficierhasusers=user, one_user=one_user, the_title="add new customofficierhasuser", touslescustom_officer=touslescustom_officer, touslesuser=touslesuser)


    touslescustom_officer= query_db("select * from custom_officer")

    touslesuser= query_db("select * from user")

    user = query_db('select * from customofficierhasuser')
    one_user = query_db("select * from customofficierhasuser limit 1", one=True)
    return render_template("customofficierhasuserform.html", customofficierhasusers=user, one_user=one_user, the_title="add new customofficierhasuser", touslescustom_officer=touslescustom_officer, touslesuser=touslesuser)

@app.route("/add_one_hit", methods=["GET","POST"])
def add_one_hit():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into hit (artist,title) values (:artist,:title)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from hit')


        return render_template("hitform.html", hits=user, one_user=one_user, the_title="add new hit")


    user = query_db('select * from hit')
    one_user = query_db("select * from hit limit 1", one=True)
    return render_template("hitform.html", hits=user, one_user=one_user, the_title="add new hit")

@app.route("/add_one_musicalinstrument", methods=["GET","POST"])
def add_one_musicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into musicalinstrument (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from musicalinstrument')


        return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")


    user = query_db('select * from musicalinstrument')
    one_user = query_db("select * from musicalinstrument limit 1", one=True)
    return render_template("musicalinstrumentform.html", musicalinstruments=user, one_user=one_user, the_title="add new musicalinstrument")

@app.route("/add_one_userhasmusicalinstrument", methods=["GET","POST"])
def add_one_userhasmusicalinstrument():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesmusicalinstrument= query_db("select * from musicalinstrument")

        one_user = query_db("insert into userhasmusicalinstrument (musicalinstrument_id,user_id) values (:musicalinstrument_id,:user_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from userhasmusicalinstrument')


        return render_template("userhasmusicalinstrumentform.html", userhasmusicalinstruments=user, one_user=one_user, the_title="add new userhasmusicalinstrument", touslesmusicalinstrument=touslesmusicalinstrument)


    touslesmusicalinstrument= query_db("select * from musicalinstrument")

    user = query_db('select * from userhasmusicalinstrument')
    one_user = query_db("select * from userhasmusicalinstrument limit 1", one=True)
    return render_template("userhasmusicalinstrumentform.html", userhasmusicalinstruments=user, one_user=one_user, the_title="add new userhasmusicalinstrument", touslesmusicalinstrument=touslesmusicalinstrument)

@app.route("/add_one_userhashit", methods=["GET","POST"])
def add_one_userhashit():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into userhashit (hit_id,user_id) values (:hit_id,:user_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from userhashit')


        return render_template("userhashitform.html", userhashits=user, one_user=one_user, the_title="add new userhashit")


    user = query_db('select * from userhashit')
    one_user = query_db("select * from userhashit limit 1", one=True)
    return render_template("userhashitform.html", userhashits=user, one_user=one_user, the_title="add new userhashit")

@app.route("/add_one_userhasrythme", methods=["GET","POST"])
def add_one_userhasrythme():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesuser= query_db("select * from user")

        one_user = query_db("insert into userhasrythme (hit_id,rythme,user_id) values (:hit_id,:rythme,:user_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from userhasrythme')


        return render_template("userhasrythmeform.html", userhasrythmes=user, one_user=one_user, the_title="add new userhasrythme", touslesuser=touslesuser)


    touslesuser= query_db("select * from user")

    user = query_db('select * from userhasrythme')
    one_user = query_db("select * from userhasrythme limit 1", one=True)
    return render_template("userhasrythmeform.html", userhasrythmes=user, one_user=one_user, the_title="add new userhasrythme", touslesuser=touslesuser)

@app.route("/add_one_userhassignaturemusicale", methods=["GET","POST"])
def add_one_userhassignaturemusicale():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into userhassignaturemusicale (motif_musical,hit_id,style_id) values (:motif_musical,:hit_id,:style_id)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from userhassignaturemusicale')


        return render_template("userhassignaturemusicaleform.html", userhassignaturemusicales=user, one_user=one_user, the_title="add new userhassignaturemusicale")


    user = query_db('select * from userhassignaturemusicale')
    one_user = query_db("select * from userhassignaturemusicale limit 1", one=True)
    return render_template("userhassignaturemusicaleform.html", userhassignaturemusicales=user, one_user=one_user, the_title="add new userhassignaturemusicale")

@app.route("/add_one_style", methods=["GET","POST"])
def add_one_style():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        one_user = query_db("insert into style (name) values (:name)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from style')


        return render_template("styleform.html", styles=user, one_user=one_user, the_title="add new style")


    user = query_db('select * from style')
    one_user = query_db("select * from style limit 1", one=True)
    return render_template("styleform.html", styles=user, one_user=one_user, the_title="add new style")

@app.route("/add_one_performance", methods=["GET","POST"])
def add_one_performance():

    if request.method == 'POST':

        the_username = "anonyme"
        hey=dict(request.form)


        touslesstyle= query_db("select * from style")

        one_user = query_db("insert into performance (user_id,style_id,artist,composer,title) values (:user_id,:style_id,:artist,:composer,:title)",hey, one=True)
        mylastrowid=str(one_user["myid"])
        user = query_db('select * from performance')


        return render_template("performanceform.html", performances=user, one_user=one_user, the_title="add new performance", touslesstyle=touslesstyle)


    touslesstyle= query_db("select * from style")

    user = query_db('select * from performance')
    one_user = query_db("select * from performance limit 1", one=True)
    return render_template("performanceform.html", performances=user, one_user=one_user, the_title="add new performance", touslesstyle=touslesstyle)

