from requests import post

def main():
    variables = {
        'search': 'a',
        'page': 1,
        'perPage': 15
    }

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
        }

        '''


    

    url = 'https://graphql.anilist.co'

    # Make the HTTP Api request
    response = post(url, json={'query': query, 'variables': variables}).json()['data']['characters']['characters']

    background = 'https://lh3.googleusercontent.com/hzZwhjmfaOqp--Yzo6jg2MTrIr6ab9MhdhMUvfXMqkaz4QP8f6trFKDN5hYQ6roD3EY-2Xk44xogbK9SwkTWVD8lIyzWU2pGNBA1oxusAgKMj4s-QMr1DkxyR_pyxzMUzKFs-aJeTw=w2400?source=screenshot.guru'

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
.dark-blue{
    background: #0B1622;
}

.medium-blue{
    background: #152232;
}

.light-blue{
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

a{
    color: #fff;
}

a:hover{
    color: #f00;
}

.navbar img{
    height: 30px;
}

.navbar a{
    margin: 0;
    padding-left: 15px;
}

.background{
    background-size: cover;
    background-position: center;
    background-repeat: no-repeat;
    height: 100vh;
    position: sticky;
    top: 55px;
    z-index: -100;
}

.no-bg{
    background: none;
    display: inline-block;
    margin-bottom: 100px;
}

.transparent{
    position: absolute;
    top: 50%;
    left: 50%;
    transform: translate(-50%, -50%);
    width: 80%;
    margin-top: 25px;
}

.overlay{
    backdrop-filter: blur(20px);
    background: rgba(0,0,0,0.3);
    color: #fff;
    padding: 3%;
    border-radius: 15px;
}

.navbar{
    justify-content: space-between;
    position: sticky;
    top: 0;
    z-index: 100;
}

.search{
    box-shadow: inset 0 0 0 0;
    transition: ease-out 0.3s;
    outline: none;
    color: #fff;
}

.search:hover, .search:focus{
    box-shadow: inset 1000px 0 0 0 #0B1622;
    cursor: pointer;
    color: #fff;
}

.card-body{
    position: absolute;
    bottom: 0;
    width: 150px;
    background: rgb(0,0,0,0.5);
    border-radius: 0 0 10px 10px;
    backdrop-filter: blur(4px);
}

.card{
    position: relative;
    width: 150px;
    margin: 20px 20px;
    display: inline-block;
    border-radius: 10px;
    border: 0;
}

.card-img-top{
    height: 230px;
    width: 150px;
    border-radius: 10px;
}

.card-title{
    text-align: center;
    margin: auto;
    font-size: medium;
}

#popular{
    text-align: center;
    background: rgb(0,0,0, 0.5);
    margin: auto;
    width: 90%;
    border-radius: 20px;
    padding-bottom: 5vh;
}

.heading{
    color: white;
    text-align: center;
    padding-top: 5vh;
    padding-bottom: 5vh;
    font-size: x-large;
}

.searchbar{
    border: 0;
    color: #fff;
    width: 75%;
    float: left;
    padding: 15px;
}

.searchbar:focus{
    background: #152232;
    border: 0;
    color: #fff;
}

.searchbarbutton{
    width: 15%;
    float: right;
    padding: 15px;
}

.modal-content{
    margin-top: 125px;
}

@media only screen and (max-width: 537px){
    .card {
        width: 87%;
        margin: 10px auto;
        height: 100px;
    }

    .card-body{
        top: 0;
        right:0;
        width: 75%;
        height: 100%;
        float: right;
        border-radius: 0 10px 10px 0;
    }

    .card-img-top{
        height: 100%;
        width: 25%;
        float: left;
        border-radius: 10px 0 0 10px;
    }

    .card-title{
        position: absolute;
        top: 50%;
        left: 50%;
        transform: translate(-50%, -50%)
    }

    .searchbar{
    width: 100%;
    margin-bottom: 15px;
    }

    .searchbarbutton{
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
            <form class="d-flex">
                <button id="button1" class="search btn light-blue" type="button" data-bs-toggle="modal" data-bs-target="#mymodal">Search</button>
            </form>
        </div>
    </nav>'''

    code += f'<section class="background" style="background-image: url({background})"></section>'

    code += '''
    <!--anime definitions-->
    <section class="transparent">
        <div class="overlay">
            <p class="m-0">Anime (Japanese: アニメ, IPA: [aɲime]) is hand-drawn and
                computer animation originating from Japan. In Japan and in Japanese, anime (a term
                derived from the English word animation) describes all animated works, regardless of
                style or origin. However, outside of Japan and in English, anime is colloquial for
                Japanese animation and refers specifically to animation produced in Japan.</p>
        </div>
    </section>

    <section class="dark-blue no-bg">
        <div id="popular">
        <div class="heading">Popular Characters</div>
        '''

    for i in response:
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
    </section>

    <footer class="footer">
        <p class="p-3">AniChar | Unofficial website</p>
        <p class="p-3">Contact us: anichar36@gmail.com</p>
    </footer>

    <div class="modal fade" tabindex="-1" id="mymodal">
        <div class="modal-dialog modal-lg">
            <div class="modal-content dark-blue">
                <div class="modal-body">
                        <input id="searchbar" class="form-control me-2 light-blue searchbar" type="search" placeholder="Search" aria-label="Search">
                        <button onClick="search();" id="searchbarbutton" class="search btn light-blue searchbarbutton" type="button">Search</button>
                </div>
            </div>
        </div>
    </div>

    <!-- JavaScript Bundle with Popper -->
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.0.0-beta3/dist/js/bootstrap.bundle.min.js" integrity="sha384-JEW9xMcG8R+pH31jmWH6WWP0WintQrMb4s7ZOdauHnUtxwoG2vI5DkLtS3qm9Ekf" crossorigin="anonymous"></script>

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

