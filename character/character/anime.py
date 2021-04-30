from requests import post

def main(id):
    query = '''
    query ($id: Int, $asHtml: Boolean, $version: Int) {
        Media (id: $id) {
            bannerImage
            title {
                romaji
            }
            description (asHtml: $asHtml)
            startDate{
                day
                month
                year
            }
            endDate{
                day
                month
                year
            }
            status (version: $version)
            genres
            meanScore
            characters{
                nodes{
                    id
                    name{
                        full
                    }
                    image{
                        large
                    }
                }
            }
        }
    }
    '''

    variables = {
        'id': id,
        'asHtml': True,
        'version': 2
    }

    url = 'https://graphql.anilist.co'

    response = post(url, json={'query': query, 'variables': variables}).json()['data']
    
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
        <title>{response['Media']['title']['romaji']}</title>
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

        p{
            margin-top: 1rem;
        }

        a {
            color: #fff;
        }

        a:hover {
            color: #f00;
        }

        .navbar img{
            height: 30px;
        }

        .navbar a{
            margin: 0;
            padding-left: 15px;
        }

        .banner {
            height: 400px;
            background-position: 50%;
            background-repeat: no-repeat;
            background-size: cover;
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

        .scroll{
            overflow-x: auto;
            white-space: nowrap;
        }

        .scroll b{
            padding-left: 30px;
        }

        .result{
            text-align: center;
            margin: auto 30px;
        }

        .description{
            font-size: medium;
            color: #fff;
            text-align: left;
            padding: 2vh 3vh 2vh 3vh;
        }

        .result-card{
            border-radius: 20px;
            margin: 30px auto;
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

            .banner {
                height: 210px;
            }
        }

        /* width */
        ::-webkit-scrollbar {
            width: 5px;
            height: 5px;
        }

        /* Track */
        ::-webkit-scrollbar-track {
            background: none;
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

        <section class="banner"
            style="background-image: url({response['Media']['bannerImage']})">
        </section>
        <!--anime definitions-->


        <section class="dark-blue result">

            <div class="result-card light-blue">
                <div class="heading">{response['Media']['title']['romaji']}</div>
            </div>

            <div class="result-card light-blue">
                <div class="description scroll">
                    <b>Status:</b> {response['Media']['status']}
                    <b>Start Date:</b> {response['Media']['startDate']['day']}/{response['Media']['startDate']['month']}/{response['Media']['startDate']['year']} (DD/MM/YY)
                    <b>End Date:</b> {response['Media']['endDate']['day']}/{response['Media']['endDate']['month']}/{response['Media']['endDate']['year']} (DD/MM/YY)
                    <b>Genres:</b> '''
                    
    for i in response['Media']['genres']:
        code += f' {i}'
        
    code += f'''
                    <b>Mean Score:</b> {response['Media']['meanScore']}
                </div>
            </div>

            <div class="result-card light-blue">
                <div class="description">{response['Media']['description']}</div>
            </div>

            <div class="result-card light-blue">
                <div class="heading">Characters Featured</div>'''

    for i in response['Media']['characters']['nodes']:
        code += f'''            

                <div class="card text-white light-blue">
                    <a href="/character/{i['id']}">
                        <img src="{i['image']['large']}"
                            class="card-img-top" alt={i['name']['full']}>
                        <div class="card-body">
                            <h5 class="card-title">{i['name']['full'][:35]}</h5>
                        </div>
                    </a>
                </div>'''

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
