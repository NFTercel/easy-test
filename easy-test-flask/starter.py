"""
    :copyright: © 2019 by the Lin team.
    :license: MIT, see LICENSE for more details.
"""
import sys
from app.app import create_app

from app.libs.init import celery

app = None
environment = None
env_param = [i for i in sys.argv if i.startswith('--env') or i.startswith('--host')]
if env_param:
    environment = env_param[0].split('=')[1]
if not environment or environment == 'dev':
    # 开发环境
    app = create_app(environment='development')
elif environment == 'prod':
    # 生产环境
    app = create_app()

celery.conf.update(imports='app.libs.tasks')


@app.route('/', methods=['GET'], strict_slashes=False)
def lin_slogan():
    return """<style type="text/css">*{ padding: 0; margin: 0; } div{ padding: 4px 48px;} a{color:#2E5CD5;cursor: 
    pointer;text-decoration: none} a:hover{text-decoration:underline; } body{ background: #fff; font-family: 
    "Century Gothic","Microsoft yahei"; color: #333;font-size:18px;} h1{ font-size: 100px; font-weight: normal; 
    margin-bottom: 12px; } p{ line-height: 1.6em; font-size: 42px }</style><div style="padding: 24px 48px;"><p> 
    <br/><span style="font-size:30px">遇事不决 可问春风</span></p></div> """


if __name__ == '__main__':
    app.run(host='0.0.0.0')
