from tornado.web import Application, RequestHandler
from tornado.ioloop import IOLoop
from loan_decision import LoanDecision
import json

class LoanDecisionApi(RequestHandler):
    def get(self):
        self.write({'message': 'hello world'})

    def post(self):
        body = json.loads(self.request.body)
        decision = LoanDecision.validate_loan(requested_amount=body['requested_amount'])

        self.write({'decision':decision})

def make_app():
    urls = [
    ("/validate_loan", LoanDecisionApi)
    ]
    return Application(urls, debug=True)

if __name__ == '__main__':
    app = make_app()
    app.listen(3000)
    IOLoop.instance().start()
