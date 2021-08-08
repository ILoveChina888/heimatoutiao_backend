from flask import request, g

from utils.jwt_util import verify_jwt


def jwt_authentication():
    # 获取请求头中的 Token
    #  Authorization: Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJzb21lIjoicGF5bG9hZCJ9.4twFt5NiznN84AWoo1d7KO1T_yoc0Z6XOpOVswacPZg

    g.user_id = None
    g.is_refresh = False

    token_with_more = request.headers.get('Authorization')
    if token_with_more is not None and token_with_more.startswith('Bearer '):
        token = token_with_more[7:]

        # 验证 Token
        payload = verify_jwt(token)
        if payload is not None:
            # 保存到 g 对象中
            g.user_id = payload.get('user_id')
            g.is_refresh = payload.get('is_refresh', False)













