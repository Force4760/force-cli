#TODO: Implement show deck stats
#TODO: web view


f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link href="//cdn.jsdelivr.net/npm/mana-font@latest/css/mana.min.css" rel="stylesheet" type="text/css" />
    <link rel="stylesheet" href="./web/style.css">
    <title>{deck_name}</title>
</head>
<body>
    <header>
        <h1>{deck_name}</h1>
        <h2 class="format">{deck_format}</h2>
    </header>
    <main>
        <div class="card-view">
            <img src="" alt="Card Image">
        </div>
        <div class="list">
            <h2>Main Board</h2>
            <a href="#"><span class="number">Number</span>&nbsp;&nbsp;&nbsp;&nbsp; Name &nbsp;&nbsp;&nbsp;&nbsp;<span class="cost">{W}{W}</span></a>
            <a href="#"><span class="number">Number</span>&nbsp;&nbsp;&nbsp;&nbsp; Name</a>
            <h2>Side Board</h2>
        </div>
    </main>
    

</body>
</html>
"""