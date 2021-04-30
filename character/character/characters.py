from requests import post

def main(id):
    query = '''
    query ($id: Int, $asHtml: Boolean) {
        Character (id: $id){
            name{
                full
                native
            }
            image{
                large
            }
            gender
            dateOfBirth{
                month
                day
            }
            age
            description (asHtml: $asHtml)
            media{
                nodes{
                    id
                    title{
                        romaji
                    }
                    coverImage{
                        large
                    }
                }
            }
        }
    }
    '''

    # Define our query variables and values that will be used in the query request
    variables = {
        'id': id,
        'asHtml': True
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = post(url, json={'query': query, 'variables': variables}).json()['data']

    desc = response['Character']['description']


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
            href="https://lh3.googleusercontent.com/eE451QtDmxNiFfrtz10c0bFKSQ9IUd28jFMHNjgJUhOgQyrImxSY_e-YbehMoO5nVxm3a4JK-1O85QN7-d0qmAw4a1SMmEtw8rzJkTc6vXHpg5kXI6rpAxsumYlnaO0x7i5XLwOk=w2400"
            rel="shortcut icon" type="image/x-icon">'''

    code += f'''
        <title>{response['Character']['name']['full']}</title>
        '''

    code += '''

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

        .navbar img{
            height: 30px;
        }

        .navbar a{
            margin: 0;
            padding-left: 15px;
        }

        .markdown_spoiler{
            color: #434b57;
            background: #434b57;
            width: fit-content;
        }

        .markdown_spoiler:hover, .markdown_spoiler:focus{
            color: #fff;
            background: none;
        }

        a {
            color: #fff;
        }

        a:hover {
            color: #f00;
        }

        p a{
            pointer-events: none;
            color: inherit;
            text-decoration: none;
        }

        .navbar {
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 100;
        }

        .search {
            box-shadow: inset 0 0 0 0;
            transition: ease-out 0.3s;
            outline: none;
            color: #fff;
        }

        .search:hover,
        .search:focus {
            box-shadow: inset 1000px 0 0 0 #0B1622;
            cursor: pointer;
            color: #fff;
        }

        .img-info{
            margin: 30px;
        }

        .cover {
            border-radius: 20px;
            margin-bottom: 30px;
        }

        .quick-info {
            position: absolute;
            width: 55%;
            left: 290px;
            top: 85px;
        }

        .info-card {
            border-radius: 20px;
        }

        .card-body {
            position: absolute;
            bottom: 0;
            width: 150px;
            background: rgb(0, 0, 0, 0.5);
            border-radius: 0 0 10px 10px;
            backdrop-filter: blur(4px);
        }

        .card {
            position: relative;
            width: 150px;
            margin: 20px 20px;
            display: inline-block;
            border-radius: 10px;
            border: 0;
        }

        .card-img-top {
            height: 230px;
            width: 150px;
            border-radius: 10px;
        }

        .card-title {
            text-align: center;
            margin: auto;
            font-size: medium;
        }

        .result {
            text-align: center;
            margin: auto 30px;
        }

        .title {
            font-size: x-large;
            color: #fff;
            text-align: left;
            padding: 2vh 3vh 0vh 3vh;
        }

        .paragraph {
            font-size: medium;
            color: #fff;
            text-align: left;
            padding: 2vh 3vh 2vh 3vh;
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

        .searchbar {
            border: 0;
            color: #fff;
            width: 75%;
            float: left;
            padding: 15px;
        }

        .searchbar:focus {
            background: #152232;
            border: 0;
            color: #fff;
        }

        .searchbarbutton {
            width: 15%;
            float: right;
            padding: 15px;
        }

        .modal-content {
            margin-top: 125px;
        }

        @media only screen and (max-width: 537px) {
            .card {
                width: 87%;
                margin: 10px auto;
                height: 100px;
            }

            .card-body {
                top: 0;
                right: 0;
                width: 75%;
                height: 100%;
                float: right;
                border-radius: 0 10px 10px 0;
            }

            .card-img-top {
                height: 100%;
                width: 25%;
                float: left;
                border-radius: 10px 0 0 10px;
            }

            .card-title {
                position: absolute;
                top: 50%;
                left: 50%;
                transform: translate(-50%, -50%)
            }

            .searchbar {
                width: 100%;
                margin-bottom: 15px;
            }

            .searchbarbutton {
                width: 100%;
            }
        }

        @media only screen and (max-width: 800px) {

            .img-info{
                text-align: center;
            }

            .quick-info{
                width: 100%;
                position: initial;
            }
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
                <a href="/"><img src="https://lh3.googleusercontent.com/eE451QtDmxNiFfrtz10c0bFKSQ9IUd28jFMHNjgJUhOgQyrImxSY_e-YbehMoO5nVxm3a4JK-1O85QN7-d0qmAw4a1SMmEtw8rzJkTc6vXHpg5kXI6rpAxsumYlnaO0x7i5XLwOk=w2400" alt="AniChart logo"></a>
                <a class="navbar-brand" href="/">AniChar</a>
                <form class="d-flex">
                    <button id="button1" class="search btn light-blue" type="button" data-bs-toggle="modal"
                        data-bs-target="#mymodal">Search</button>
                </form>
            </div>
        </nav>'''

    code += f'''

        <section class="img-info">
            <img class="cover" src="{response['Character']['image']['large']}" alt="{response['Character']['name']['full']}">
            <div class="quick-info">
                <div class="info-card light-blue">
                    <div class="name title">{response['Character']['name']['full']}</div>
                    <p class="paragraph">{response['Character']['name']['native']}</p>
                </div>
                <div class="info paragraph info-card light-blue">Gender: {response['Character']['gender']}<br>Birthday: {response['Character']['dateOfBirth']['month']}/{response['Character']['dateOfBirth']['day']} (MM/DD)<br>Age: {response['Character']['age']}</div>
            </div>
        </section>


        <!--anime definitions-->


        <section class="dark-blue result">
            <div class="result-card light-blue">
                <div class="paragraph">
                    {desc}
                </div>
            </div>

            <div class="result-card light-blue">
                <div class="heading">Character featured in</div>'''

    for i in response['Character']['media']['nodes']:
        code += f'''

                <div class="card text-white light-blue">
                    <a href="/anime/{i['id']}">
                        <img src="{i['coverImage']['large']}"
                            class="card-img-top" alt="{i['title']['romaji']}">
                        <div class="card-body">
                            <h5 class="card-title">{i['title']['romaji'][:35]}</h5>
                        </div>
                    </a>
                </div>
                
                '''

    code += '''

            </div>
        </section>

        <footer class="footer">
        <p class="p-3">AniChar | Unofficial website</p>
        <p class="p-3">Contact us: anichar36@gmail.com</p>
    </footer>

        <div class="modal fade" tabindex="-1" id="mymodal">
            <div class="modal-dialog modal-lg">
                <div class="modal-content dark-blue">
                    <div class="modal-body">
                        <input id="searchbar" class="form-control me-2 light-blue searchbar" type="search"
                            placeholder="Search" aria-label="Search">
                        <button onClick="search();" id="searchbarbutton" class="search btn light-blue searchbarbutton"
                            type="button">Search</button>
                    </div>
                </div>
            </div>
        </div>

        <!-- JavaScript Bundle with Popper -->
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js"
            integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf"
            crossorigin="anonymous"></script>

        <script>

            search = () => {
                query = document.getElementById('searchbar').value

                window.location = "/search/" + query
            }

        </script>

    </body>

    </html>

    '''

    return code

