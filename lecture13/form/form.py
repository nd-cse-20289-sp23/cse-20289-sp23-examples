#!/usr/bin/env python3

import tornado.ioloop
import tornado.options
import tornado.web

# Constants

PORT = 9999

# Handlers

class FormHandler(tornado.web.RequestHandler):
    def get(self):
        # Get value for user argument from form submission
        user = self.get_argument('user', '')

        # Display greeting if user is specified
        if user:
            self.write(f'<b>Hello, {user}</b>')

        # To get input from the user, we must create a form where each input
        # element has a name we can use to retrieve data.
        self.write(f'''
<h1>Enter Your Name:</h1>
<form>
    <input type="text" name="user" value="{user}">
    <input type="submit" value="Echo!">
</form>
''')

# Main Execution

def main():
    application = tornado.web.Application([
        (r'/', FormHandler),
    ])
    application.listen(PORT)

    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
