from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from loan_decision import LoanDecision
import json
import tornado.httpserver
import os

class LoanDecisionApi(RequestHandler):
    def get(self):
        self.write({'message': 'hello world'})

    def post(self):
        body = json.loads(self.request.body)
        print(body)

        decision = LoanDecision.validate_loan(requested_amount=body['requested_amount'])

        self.write({'decision':decision, 'requested_amount':body['requested_amount']})

def make_app():
    urls = [
    ("/validate_loan", LoanDecisionApi)
    ]
    return Application(urls, debug=True)

if __name__ == '__main__':
    app = make_app()
    http_server = tornado.httpserver.HTTPServer(app)
    port = int(os.environ.get("PORT", 5000))
    http_server.listen(port)
    IOLoop.instance().start()
