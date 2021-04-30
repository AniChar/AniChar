from requests import post

def main(name):

    query = '''
    query ($search: String, $page: Int, $perPage: Int){
        characters: Page (page: $page, perPage: $perPage){
            characters (search: $search){
                id
                name{
                    full
                }
                image{
                    large
                }
            }
        }

        anime: Page (page: $page, perPage: $perPage){
            media (search: $search){
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
    '''

    variables = {
        'search': name,
        'page': 1,
        'perPage': 15
    }

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
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

    a {
        color: #fff;
    }

    a:hover {
        color: #f00;
    }

    .navbar {
        justify-content: space-between;
        position: sticky;
        top: 0;
        z-index: 100;
    }

    .navbar img{
        height: 30px;
    }

    .navbar a{
        margin: 0;
        padding-left: 15px;
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

    .heading {
        color: white;
        text-align: center;
        padding-top: 5vh;
        padding-bottom: 5vh;
        font-size: x-large;
    }

    .heading2 {
        color: white;
        text-align: center;
        padding-top: 3vh;
        font-size: large;
    }

    .searchbar {
        border: 0;
        color: #fff;
        width: 65%;
        display: inline-block;
        padding: 15px;
    }

    .searchbar:focus {
        background: #152232;
        border: 0;
        color: #fff;
    }

    .searchbarbutton {
        width: 25%;
        margin-top: -3px;
        padding: 15px;
    }

    .search-box{
        margin: 30px auto;
        padding: 30px;
        text-align: center;
    }

    .result{
        text-align: center;
        margin: auto 30px;
    }

    .result-card{
        border-radius: 20px;
        margin: 100px auto;
        padding-bottom: 5vh;
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
        </div>
    </nav>

    <section class="search-box">
        <input id="searchbar" class="form-control me-2 light-blue searchbar" type="search" placeholder="Search"
            aria-label="Search">
        <button onClick="search();" id="searchbarbutton" class="search btn light-blue searchbarbutton"
            type="button">Search</button>
    </section>

    <section class="dark-blue result">
    <div class="result-card light-blue">
            

    '''

    code += '<div class="heading">Characters</div>'

    if len(response['characters']['characters']) == 0:
        code += '<div class="heading2">No characters found</div>'

    for i in response['characters']['characters']:
        code += f'''
            <div class="card text-white light-blue">
                <a href="/character/{i['id']}">
                    <img src="{i['image']['large']}"
                        class="card-img-top" alt={i['name']['full']}>
                    <div class="card-body">
                        <h5 class="card-title">{i['name']['full'][:35]}</h5>
                    </div>
                </a>
            </div>
        '''

    code += '''
    </div>
    <div class="result-card light-blue">
    <div class="heading">Anime & Manga</div>
    '''

    if len(response['anime']['media']) == 0:
        code += '<div class="heading2">No anime or manga found</div>'

    for i in response['anime']['media']:
        code += f'''
            <div class="card text-white light-blue">
                <a href="/anime/{i['id']}">
                    <img src="{i['coverImage']['large']}"
                        class="card-img-top" alt={i['title']['romaji']}>
                    <div class="card-body">
                        <h5 class="card-title">{i['title']['romaji'][:35]}</h5>
                    </div>
                </a>
            </div>
        '''    

    code += '''
        </div>
        </div>
    </section>

    <footer class="footer">
        <p class="p-3">AniChar | Unofficial website</p>
        <p class="p-3">Contact us: anichar36@gmail.com</p>
    </footer>

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