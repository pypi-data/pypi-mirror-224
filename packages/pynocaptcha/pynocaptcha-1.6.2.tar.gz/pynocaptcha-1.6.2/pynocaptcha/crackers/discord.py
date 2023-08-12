from .base import BaseCracker

import warnings
warnings.filterwarnings('ignore')


class DiscordCracker(BaseCracker):
    
    cracker_name = "discord"
    cracker_version = "group"    

    """
    discord cracker
    :param authorization: discord 账号登录凭证
    :param group_id: 群 id
    :param cookies: 
    调用示例:
    cracker = DiscordCracker(
        user_token="xxx",
        authorization="MTExNzI1NDQ3NzA2NjU0MzE5NQ.xxx",
        group_id='645607528297922560',

        # debug=True,
    )
    ret = cracker.crack()
    """
    
    # 必传参数
    must_check_params = ["authorization", "group_id"]
