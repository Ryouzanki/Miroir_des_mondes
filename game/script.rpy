label start:

    "Blablabla..."

    return

label splashscreen: # Ryou > Code pour la petite vidéo quand on lance le jeu.
    $ renpy.pause(0)
    scene black
    $ renpy.movie_cutscene('opening.avi') # Ryou > On n'a pas encore opening.avi avec la bonne réso.
    with Pause(3.0)
    return
