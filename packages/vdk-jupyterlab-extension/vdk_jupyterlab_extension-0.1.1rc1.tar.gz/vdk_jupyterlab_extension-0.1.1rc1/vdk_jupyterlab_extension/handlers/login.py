from tornado.auth import OAuth2Mixin
from tornado import gen, web
from tornado.escape import json_decode, json_encode, url_escape
from tornado.httpclient import HTTPRequest, AsyncHTTPClient
from tornado.options import define, options, parse_command_line

define("port", default=8888, help="run on the given port", type=int)
define("oauth_provider_url", default="https://YOUR_OAUTH_PROVIDER.com", help="OAuth2 provider URL", type=str)
define("client_id", default="YOUR_CLIENT_ID", help="OAuth2 client ID", type=str)
define("client_secret", default="YOUR_CLIENT_SECRET", help="OAuth2 client secret", type=str)

class OAuth2Handler(web.RequestHandler, OAuth2Mixin):
    @gen.coroutine
    def get(self):
        redirect_uri = "http://localhost:8888/auth"
        code = self.get_argument("code", False)
        if code:
            http_client = AsyncHTTPClient()
            headers = {"Content-Type": "application/x-www-form-urlencoded"}
            body = f"redirect_uri={redirect_uri}&code={code}&client_id={options.client_id}&client_secret={options.client_secret}&grant_type=authorization_code"
            request = HTTPRequest(
                f"{options.oauth_provider_url}/token",
                method="POST",
                headers=headers,
                body=body,
            )
            response = yield http_client.fetch(request)
            user_json = json_decode(response.body)
            self.set_secure_cookie("user", json_encode(user_json))
            self.redirect("/")
        else:
            yield self.authorize_redirect(
                redirect_uri=redirect_uri,
                client_id=options.client_id,
                scope=["profile", "email"],
                response_type="code",
                extra_params={"approval_prompt": "auto"},
            )

def main():
    parse_command_line()
    app = web.Application(
        [
            (r"/", MainHandler),
            (r"/auth", OAuth2Handler),
        ],
        cookie_secret="YOUR_RANDOM_SECRET",
        login_url="/auth",
    )
    app.listen(options.port)
    print(f"Application is ready and listening on 0.0.0.0:{options.port}")
    tornado.ioloop.IOLoop.current().start()

if __name__ == "__main__":
    main()
