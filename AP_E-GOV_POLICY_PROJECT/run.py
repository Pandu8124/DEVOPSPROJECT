from flask import Flask, render_template, request, redirect, url_for, flash
from flask_mysqldb import MySQL
from werkzeug.security import generate_password_hash
from flask import Flask, render_template, request, redirect, url_for, flash, session
from werkzeug.security import check_password_hash, generate_password_hash
from flask import Flask, render_template, request, redirect, flash, url_for
import os
from werkzeug.utils import secure_filename


app = Flask(__name__)
app.secret_key = 'your_secret_key'


# <--- MySQL Configurations  ----->
app.config['MYSQL_HOST'] = 'localhost'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = 'root'
app.config['MYSQL_DB'] = 'ecitizen_db'
app.config['MYSQL_CURSORCLASS'] = 'DictCursor'

mysql = MySQL(app)




UPLOAD_FOLDER = 'static/uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER



#<------Main Page---->
@app.route("/")
def main():
    return render_template("new.html")

#<------Home page------>
@app.route("/home")
def home():
    return render_template("home.html")


#<----Registration Form ----->
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        surname = request.form.get('surname', '').strip()
        name = request.form.get('name', '').strip()
        lastname = request.form.get('lastname', '').strip()
        dob = request.form.get('dob', '').strip()
        age = request.form.get('age', '').strip()
        password = request.form.get('password', '').strip()
        confirm_password = request.form.get('confirm_password', '').strip()

        if not all([surname, name, lastname, dob, age, password, confirm_password]):
            flash("All fields are required!", "danger")
            return redirect(url_for('register'))

        if password != confirm_password:
            flash("Passwords do not match!", "danger")
            return redirect(url_for('register'))

        try:
            age = int(age) 
            cur = mysql.connection.cursor()
            cur.execute(
                "INSERT INTO users (surname, name, lastname, dob, age, password) VALUES (%s, %s, %s, %s, %s, %s)",
                (surname, name, lastname, dob, age, password) 
            )
            mysql.connection.commit()
            cur.close()
            flash("Registration successful! Please log in.", "success")
            return redirect(url_for('login'))
        
        except ValueError:
            flash("Invalid age format! Please enter a valid number.", "danger")
            return redirect(url_for('register'))
        
        except Exception as e:
            flash(f"Database error: {str(e)}", "danger")
            return redirect(url_for('register'))
    return render_template('register.html')

#<-----Login Form----->
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        username = request.form["username"].strip()
        password = request.form["password"].strip()

        cur = mysql.connection.cursor()
        cur.execute("SELECT password FROM users WHERE name = %s", (username,))
        user = cur.fetchone() 
        cur.close()

        if user and password == password: 
            return redirect(url_for("home")) 
        else:
            flash("Invalid username or password!", "danger")
            return redirect(url_for("login"))
    return render_template("login.html")


@app.route("/ammavadi")
def ammavadi():
    return render_template("ammavadi.html")



#<--------------------Ammavadi------------------>
@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        student_name = request.form['student_name']
        age = request.form['age']
        parent_name = request.form['parent_name']
        caste = request.form['caste']
        disabled = request.form['disabled']
        school_name = request.form['school_name']
        principal_name = request.form['principal_name']
        address = request.form['address']
        contact_number = request.form['contact_number']
        aadhar_card = request.form['aadhar_card']
        ration_card = request.form['ration_card']
        bank_account = request.form['bank_account']
        ifsc_code = request.form['ifsc_code']
        district = request.form['district']
        mandal = request.form['mandal']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO ammavadi (student_name, age, parent_name, caste, disabled, school_name, principal_name, address, contact_number, aadhar_card, ration_card, bank_account, ifsc_code, district, mandal)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (student_name, age, parent_name, caste, disabled, school_name, principal_name, address, contact_number, aadhar_card, ration_card, bank_account, ifsc_code, district, mandal))

        mysql.connection.commit()
        cursor.close()

        flash("Application Submitted Successfully!", "success")
        return redirect('/emoji_review')


#<--------amma vadi application submited ------------->

@app.route('/application1sub')
def ammavadi_applications():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM ammavadi")
    data = cursor.fetchall()
    # print(data)  
    
    cursor.close()
    return render_template('application1sub.html', applications=list(data)) 

# <------policies Revies----->
@app.route('/review')
def review_page():
    return render_template('review.html')

positive_words = {"good", "excellent", "amazing", "great", "satisfied", "happy", "nice", "love", "best", "helpful", "wonderful", "beneficial"}
negative_words = {"bad", "worst", "poor", "terrible", "disappointed", "awful", "horrible", "hate", "useless", "waste"}
neutral_words = {"okay", "average", "fine", "normal"}

def classify_review(review):
    words = review.lower().split()
    pos_count = sum(1 for word in words if word in positive_words)
    neg_count = sum(1 for word in words if word in negative_words)
    
    if pos_count >= 2:  
        return "Good"
    elif neg_count >= 2:  
        return "Bad"
    elif pos_count == 1 and neg_count == 0:
        return "Good"
    elif neg_count == 1 and pos_count == 0:
        return "Bad"
    else:
        return "Average"



    
#<------Review Submission------------>
@app.route('/submit_review', methods=['POST'])
def submit_review():
    policy = request.form['policy']
    review_text = request.form["review"]
    sentiment = classify_review(review_text)
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO policy_reviews (policy, review, sentiment) VALUES (%s, %s,%s)", (policy, review_text, sentiment))
    mysql.connection.commit()
    flash("Review submitted successfully!", "success")
    return redirect('/review')

#<-------Display Reviews----------->
# @app.route('/reviews')
# def show_reviews():
#     cursor = mysql.connection.cursor()
#     cursor.execute("SELECT * FROM policy_reviews")
#     reviews = cursor.fetchall()
#     return render_template('reviews.html', reviews=reviews)


@app.route('/reviews')
def reviews():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM policy_reviews ORDER BY id DESC")
    reviews = cursor.fetchall()
    cursor.close()
    return render_template('reviews.html', reviews=reviews)


#<--------contact page---------->
@app.route('/contact')
def contact():
    return render_template('contact.html')

#<--------contact submited page---------->
@app.route("/submit_contact", methods=["POST"])
def submit_contact():
    name = request.form["name"]
    email = request.form["email"]
    message = request.form["message"]
    cursor = mysql.connection.cursor()
    query = "INSERT INTO contact_messages (name, email, message) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, message))
    mysql.connection.commit()

    flash("Message submitted successfully!", "success")
    return redirect("/contact")

#<-------About page----------->
@app.route('/about')
def about():
    return render_template('about.html')


#<------Rythu Bandhu ------->
@app.route("/rythubandhu")
def rythubandhu():
    return render_template("rythubandhu.html")


# Route to Handle Form Submission for Rythu Bandhu
@app.route('/submit_rythu_bandhu', methods=['POST'])
def submit_rythu_bandhu():
    if request.method == 'POST':
        farmer_name = request.form['farmer_name']
        age = request.form['age']
        aadhar_card = request.form['aadhar_card']
        land_certificate = request.form['land_certificate']
        pan_card = request.form['pan_card']
        landtype = request.form['landtype']
        landarea = request.form['landarea']
        district = request.form['district']
        mandal = request.form['mandal']
        
        cursor = mysql.connection.cursor()
        sql = """INSERT INTO rythu_bandhu (farmer_name, age, aadhar_card, land_certificate, 
                 pan_card, landtype, landarea, district, mandal) 
                 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
        values = (farmer_name, age, aadhar_card, land_certificate, pan_card, landtype, landarea, district, mandal)

        cursor.execute(sql, values)
        mysql.connection.commit()
        cursor.close()

        flash("Application Submitted Successfully!", "success")
        return redirect('/emoji_review')

#<------Rythu bandhu applications------------>
@app.route('/rythu_bandhu_applications')
def rythu_bandhu_applications():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM rythu_bandhu")
    applications = cursor.fetchall()
    cursor.close()
    return render_template('rythubandhuappsub.html', applications=applications)


#<------new Emoji Review------------>

@app.route('/emoji_review')
def emoji_review():
    return render_template('newpolicy.html')



@app.route('/submit_emoji_review', methods=['POST'])
def submit_emoji_review():
    policy = request.form['policy']
    text_review = request.form['text_review']
    emoji_image = request.files['emoji_image']

    emoji_image_path = None

    # ✅ Automatically classify the review
    sentiment = classify_review(text_review)

    if emoji_image:
        filename = secure_filename(emoji_image.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        emoji_image.save(filepath)
        emoji_image_path = filepath  # Save the file path in the database

    try:
        cursor = mysql.connection.cursor()
        sql = "INSERT INTO policy_reviews (policy, review, sentiment, emoji_image) VALUES (%s, %s, %s, %s)"
        values = (policy, text_review, sentiment, emoji_image_path)  # ✅ Save classified sentiment
        cursor.execute(sql, values)
        cursor.connection.commit()
        cursor.close()
        
        flash("Review submitted successfully!", "success")
    except mysql.connector.Error as err:
        flash(f"Error: {err}", "danger")

    return redirect(url_for('emoji_review'))


#<----------aarogyasri policys-------------->
@app.route("/aarogyasri")
def aarogyasri():
    return render_template("aarogyasri.html")


@app.route('/submit_aarogyasri', methods=['POST'])
def submit_aarogyasri():
    if request.method == 'POST':
        patient_name = request.form['patient_name']
        age = request.form['age']
        guardian_name = request.form['guardian_name']
        aadhar_card = request.form['aadhar_card']
        ration_card = request.form['ration_card']
        disease_category = request.form['disease_category']
        hospital_name = request.form['hospital_name']
        doctor_name = request.form['doctor_name']
        contact_number = request.form['contact_number']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO aarogyasri (patient_name, age, guardian_name, aadhar_card, ration_card, disease_category, hospital_name, doctor_name, contact_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (patient_name, age, guardian_name, aadhar_card, ration_card, disease_category, hospital_name, doctor_name, contact_number))

        mysql.connection.commit()
        cursor.close()

        flash("Aarogyasri Application Submitted Successfully!", "success")
        return redirect('/emoji_review')


@app.route("/aarogyasri_applications")
def aarogyasri_applications():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM aarogyasri")
    applications = cursor.fetchall()
    cursor.close()
    
    return render_template("aarogyasri_applications.html", applications=applications)

#<------------housing schemm-------------->
@app.route("/housing_scheme")
def housing_scheme():
    return render_template("housing_scheme.html")

@app.route('/submit_housing_scheme', methods=['POST'])
def submit_housing_scheme():
    if request.method == 'POST':
        applicant_name = request.form['applicant_name']
        age = request.form['age']
        family_income = request.form['family_income']
        aadhar_card = request.form['aadhar_card']
        ration_card = request.form['ration_card']
        occupation = request.form['occupation']
        district = request.form['district']
        state = request.form['state']
        contact_number = request.form['contact_number']

        cursor = mysql.connection.cursor()
        cursor.execute("""
            INSERT INTO housing_scheme (applicant_name, age, family_income, aadhar_card, ration_card, occupation, district, state, contact_number)
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, (applicant_name, age, family_income, aadhar_card, ration_card, occupation, district, state, contact_number))

        mysql.connection.commit()
        cursor.close()

        flash("Housing Scheme Application Submitted Successfully!", "success")
        return redirect('/emoji_review')

@app.route("/housing_scheme_applications")
def housing_scheme_applications():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM housing_scheme")
    applications = cursor.fetchall()
    cursor.close()
    
    return render_template("housing_scheme_applications.html", applications=applications)


@app.route('/example')
def example():
    return render_template('example.html')


if __name__ == "__main__":
    app.run(debug=True)
