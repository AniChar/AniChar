def main():
    code = '''
    
    <!DOCTYPE html>
    <html lang="en">


    <head>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/css/bootstrap.min.css" rel="stylesheet"
            integrity="sha384-eOJMYsd53ii+scO/bJGFsiCZc+5NDVN2yr8+0RDqr0Ql0h+rP48ckxlpbzKgwra6" crossorigin="anonymous">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <meta charset="UTF-8">
        <meta name="description" content="Anime character details">
        <meta name="keywords" content="Anime, character, waifu">
        <meta name="author" content="Chirag">
        <!--logo-->
        <link
            href="https://lh3.googleusercontent.com/k8iFdthr_fCkxXwxxJ1_4OJ3v4s4QZG-fbInIHBCh7rBseAAQJ1ir9mJ9h5ENgZDQIF8uBQeJwyf4-80NSSfkOEqjBYefFmgXuchQRHXYYRBhL9WZE3SNReIci1hV3QGAxck9NLLbQ=w2400"
            rel="shortcut icon" type="image/x-icon">
        <title>AniChar</title>

    </head>

    <style>
        .dark-blue {
            background: #0B1622;
        }

        .medium-blue {
            background: #152232;
        }

        .light-blue {
            background: #151F2E;
        }

        .footer {
            background: #11161D;
            color: #fff;
            display: flex;
            justify-content: space-between;
        }

        .footer p{
            margin: auto 10px;
            overflow-wrap: anywhere;
        }

        .navbar {
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .result {
            padding-top: 24vh;
            text-align: center;
            margin: auto 30px;
            padding-bottom: 24vh;
        }

        .paragraph {
            font-size: medium;
            color: #fff;
            text-align: center;
            padding-bottom: 5vh;
        }

        .result-card {
            border-radius: 20px;
            margin: 50px auto;
        }

        .heading {
            color: white;
            text-align: center;
            padding-top: 5vh;
            padding-bottom: 5vh;
            font-size: x-large;
        }

        /* width */
        ::-webkit-scrollbar {
            width: 5px;
        }

        /* Track */
        ::-webkit-scrollbar-track {
            background: #333;
        }

        /* Handle */
        ::-webkit-scrollbar-thumb {
            background: #777;
            border-radius: 10px;
            opacity: 0.3;
        }

        /* Handle on hover */
        ::-webkit-scrollbar-thumb:hover {
            background: #555;
        }
    </style>

    <body class="dark-blue">
        <!--header-->
        <nav class="navbar navbar-expand-lg navbar-dark medium-blue">
            <div class="container-fluid">
                <a class="navbar-brand" href="/">AniChar</a>
                <form class="d-flex">
                    <button id="button1" class="search btn light-blue" type="button" data-bs-toggle="modal"
                        data-bs-target="#mymodal">Search</button>
                </form>
            </div>
        </nav>

        <section class="dark-blue result">
            <div class="result-card light-blue">
                <div class="heading">
                    Page not found
                </div>
            <div id='notfound' class="paragraph">Redirecting to main page in 3 seconds...</div>
            </div>
        </section>

        <footer class="footer">
            <p class="p-3">AniChar | Unofficial website</p>
            <p class="p-3">Contact us: anichar36@gmail.com</p>
        </footer>

        <script>
            var seconds=3;
            function displaySecond(){
                seconds -= 1;
                document.getElementById("notfound").innerText="Redirecting to main page in "+seconds+" seconds..."
            }
            setInterval(displaySecond,1000);

            function redirect(){
                window.location="/"
            }
            setTimeout('redirect()', 3000)
        </script>

    </body>

    </html>
    
    '''

    return code