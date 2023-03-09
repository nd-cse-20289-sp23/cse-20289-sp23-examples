#!/usr/bin/env python3

import tornado.ioloop
import tornado.options
import tornado.web

# Constants

PORT = 9999

# Handlers

class TemplateHandler(tornado.web.RequestHandler):
    def get(self):
        user = self.get_argument('user', '')
        self.render('template.html', user=user)     # Render template with arguments

# Main Execution

def main():
    application = tornado.web.Application([
        (r'/', TemplateHandler),
    ])
    application.listen(PORT)

    tornado.options.parse_command_line()
    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()

