# Instalar en terminal: pip install python-wordpress-xmlrpc

from wordpress_xmlrpc import Client, WordPressPost
from wordpress_xmlrpc.methods.posts import NewPost


def publish_wordpress_post(username, password, url, title, content):

    # Se crea el cliente de WordPress
    wordpress_post = Client(url, username, password)

    # Se crea un nuevo objeto tipo WordPressPost
    post = WordPressPost()
    post.title = title
    post.content = content
    post.post_status = 'publish'

    # Se publica el post en WordPress
    wordpress_post.call(NewPost(post))


# Ejemplo de uso
if __name__ == "__main__":

    username = 'alfarogjohn@gmail.com'
    password = 'Sistema2023.'
    # importante terminar la url con xmlrpc.php
    url = 'https://alfarogjohn.wordpress.com/xmlrpc.php'
    title = 'Título de la prueba'
    content = 'Contenido del post'

    publish_wordpress_post(username, password, url, title, content)
