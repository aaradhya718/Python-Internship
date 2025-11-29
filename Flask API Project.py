from flask import Flask
app = Flask(__name__)

@app.route("/")  # for redirecting the oage u want to land like homepage
def home():
    return"""
    
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>My Personal Homepage - [Chitransh]</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            margin: 0;
            padding: 0;
            background-color: #f7f7f7;
            color: #333;
            line-height: 1.6;
        }
        .container {
            width: 80%;
            margin: 30px auto;
            padding: 20px;
            background-color: white;
            box-shadow: 0 4px 8px rgba(0, 0, 0, 0.1);
            border-radius: 8px;
        }
        header {
            text-align: center;
            padding-bottom: 20px;
            border-bottom: 2px solid #ccc;
        }
        header h1 {
            color: #007bff;
            margin-bottom: 5px;
        }
        .section {
            margin: 30px 0;
            padding: 15px;
            border-left: 5px solid #007bff;
            background-color: #fefefe;
            border-radius: 4px;
        }
        .section h2 {
            color: #555;
            margin-top: 0;
        }
        ul {
            list-style: square;
            padding-left: 20px;
        }
        footer {
            text-align: center;
            padding-top: 20px;
            color: #777;
            font-size: 0.9em;
        }
    </style>
</head>
<body>

    <div class="container">
        
        <header>
            <h1>Hello, I'm [Chitransh]!</h1>
            <p><strong>[Programmer] | Enthusiast of Technology and Innovation</strong></p>
        </header>

        <section class="section" id="intro">
            <h2>👋 About Me</h2>
            <p>I am a passionate individual currently focused on python programming. I love exploring new concepts, particularly in the realm of AI automation. My goal is to create something using technologythat makes human life easier.</p>
            <p>I believe in continuous learning and leveraging technology to solve everyday problems.</p>
        </section>

        <section class="section" id="skills">
            <h2>🧠 Skills & Interests</h2>
            <ul>
                <li>**Technical Skills:** HTML, CSS, JavaScript, Python, [Other Language/Tool]</li>
                <li>**Soft Skills:** Problem-Solving, Teamwork, [Other Soft Skill]</li>
                <li>**Interests:** Reading Sci-Fi, Hiking, Cricket</li>
            </ul>
        </section>

        <section class="section" id="contact">
            <h2>📬 Get in Touch</h2>
            <p>Feel free to connect with me!</p>
            <p>
                Email: <a href="mailto:your.email@example.com">your.email@example.com</a><br>
                LinkedIn: <a href="[Your LinkedIn URL]" target="_blank">linkedin.com/in/[YourProfile]</a><br>
                GitHub: <a href="[Your GitHub URL]" target="_blank">github.com/[YourUsername]</a>
            </p>
        </section>

        <footer>
            <p>Updated: November 2025</p>
        </footer>

    </div>

</body>
</html>
    """
if __name__=='__main__':
    app.run()