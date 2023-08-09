# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['nonebot_plugin_saa',
 'nonebot_plugin_saa.adapters',
 'nonebot_plugin_saa.types',
 'nonebot_plugin_saa.utils']

package_data = \
{'': ['*']}

install_requires = \
['anyio>=3.6.2,<4.0.0',
 'nonebot2>=2.0.0,<3.0.0',
 'pydantic>=1.10.5,<2.0.0',
 'strenum>=0.4.8,<0.5.0']

setup_kwargs = {
    'name': 'nonebot-plugin-send-anything-anywhere',
    'version': '0.3.0',
    'description': 'An adaptor for nonebot2 adaptors',
    'long_description': '<div align="center">\n\n~logo征集中，假装有图片~\n\n# Nonebot Plugin<br>Send Anything Anywhere\n\n你只管业务实现，把发送交给我们\n\n![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/felinae98/nonebot-plugin-send-anything-anywhere/test.yml)\n![Codecov](https://img.shields.io/codecov/c/github/felinae98/nonebot-plugin-send-anything-anywhere)\n![PyPI - Python Version](https://img.shields.io/pypi/pyversions/nonebot-plugin-send-anything-anywhere)\n![PyPI](https://img.shields.io/pypi/v/nonebot-plugin-send-anything-anywhere)\n![GitHub](https://img.shields.io/github/license/felinae98/nonebot-plugin-send-anything-anywhere)\n\n</div>\n\n这个插件可以做什么\n\n- 为常见的消息类型提供抽象类，自适应转换成对应 adapter 的消息\n- 提供一套统一的，符合直觉的发送接口\n- 为复杂的消息提供易用的生成接口（规划中）\n\n本插件通过传入 bot 的类型来自适应生成对应 bot adapter 所使用的 Message\n\n## 安装\n\n- 使用 nb-cli 安装  \n  `nb plugin install nonebot-plugin-send-anything-anywhere`\n- 使用 poetry 安装  \n  `poetry add nonebot-plugin-send-anything-anywhere`\n- 使用 pip 安装  \n  `pip install nonebot-plugin-send-anything-anywhere`\n\n## 使用\n\n在 handler 中回复消息的情况：\n\n```python\n@matcher.handle()\nasync def handle(event: MessageEvent):\n    # 直接调用 MessageFactory.send() 在 handler 中回复消息\n    await MessageFactory("你好").send(reply=True, at_sender=True)\n    await MessageFactory("需要回复的内容").send()\n    await matcher.finish()\n```\n\n主动发送的情况：\n\n```python\nfrom nonebot_plugin_saa import TargetQQGroup\n\n# 发送目标为 QQ 号 10000, 以私聊形式发送\ntarget = TargetQQGroup(group_id=2233)\nawait MessageFactory("早上好").send_to(target)\n```\n\n从消息事件中提取发送目标:\n\n```python\nfrom nonebot_plugin_saa import extract_target, get_target\n\n@matcher.handle()\nasync def handle(event: MessageEvent):\n    target = extract_target(event)\n\n@matcher.handle()\nasync def handle(target: PlatformTarget = Depends(get_target)):\n    ...\n```\n\n发送目标的序列化与反序列化:\n\n```python\nfrom nonebot_plugin_saa import PlatformTarget, TargetQQPrivate\n\ntarget = TargetQQPrivate(user_id=112233)\nserialized_target = target.json()\ndeserialized_target = PlatformTarget.deserialize(serialized_target)\nassert deserialized_target == target\n```\n\n## 支持情况\n\n✅:支持 ✖️:支持不了 🚧:等待适配\n\n### 支持的 adapter\n\n| OneBot v11 | OneBot v12 | QQ Guild | Kaiheila |\n| :--------: | :--------: | :------: | :------: |\n|     ✅     |     ✅     |    ✅    |    ✅    |\n\n### 支持的消息类型\n\n|      | OneBot v11 | OneBot v12 | QQ Guild | 开黑啦 |\n| :--: | :--------: | :--------: | :------: | :----: |\n| 文字 |     ✅     |     ✅     |    ✅    |   ✅   |\n| 图片 |     ✅     |     ✅     |    ✅    |   ✅   |\n|  at  |     ✅     |     ✅     |    ✅    |   ✅   |\n| 回复 |     ✅     |     ✅     |    ✅    |   ✅   |\n\n### 支持的发送目标\n\n|                   | OneBot v11 | OneBot v12 | QQ Guild | Kaiheila |\n| :---------------: | :--------: | :--------: | :------: | :------: |\n|       QQ 群       |     ✅     |     ✅     |          |          |\n|      QQ 私聊      |     ✅     |     ✅     |          |          |\n| QQ 频道子频道消息 |            |     ✅     |    ✅    |          |\n|    QQ 频道私聊    |            |     ✅     |    ✅    |          |\n|  开黑啦私聊/频道  |            |            |          |    ✅    |\n\n注：对于使用 Onebot v12，但是没有专门适配的发送目标，使用了 TargetOB12Unknow 来保证其可以正常使用\n\n## 问题与例子\n\n因为在现在的 Nonebot 插件开发中，消息的构建和发送是和 adapter 高度耦合的，这导致一个插件要适配不同的 adapter 是困难的\n\nbefore:\n\n```python\nfrom nonebot.adapters.onebot.v11.event import MessageEvent as V11MessageEvent\nfrom nonebot.adapters.onebot.v11.message import MessageSegment as V11MessageSegment\nfrom nonebot.adapters.onebot.v12.event import MessageEvent as V12MessageEvent\nfrom nonebot.adapters.onebot.v12.message import MessageSegment as V12MessageSegment\nfrom nonebot.adapters.onebot.v12.bot import Bot as V12Bot\n\npic_matcher = nonebot.on_command(\'发送图片\')\n\npic_matcher.handle()\nasync def _handle_v11(event: V11MessageEvent):\n    pic_content = ...\n    msg = V11MessageSegment.image(pic_content) + V11MessageSegment.text("这是你要的图片")\n    await pic_matcher.finish(msg)\n\npic_matcher.handle()\nasync def _handle_v12(bot: V12Bot, event: V12MessageEvent):\n    pic_content = ...\n    pic_file = await bot.upload_file(type=\'data\', name=\'image\', data=pic_content)\n    msg = V12MessageSegment.image(pic_file[\'file_id\']) + V12MessageSegment.text("这是你要的图片")\n    await pic_matcher.finish(msg)\n```\n\n现在只需要:\n\n```python\nfrom nonebot.adapters.onebot.v11.event import MessageEvent as V11MessageEvent\nfrom nonebot.adapters.onebot.v12.event import MessageEvent as V12MessageEvent\nfrom nonebot.internal.adapter.bot import Bot\nfrom nonebot_plugin_saa import Image, Text, MessageFactory\n\npic_matcher = nonebot.on_command(\'发送图片\')\n\npic_matcher.handle()\nasync def _handle_v12(bot: Bot, event: Union[V12MessageEvent, V11MessageEvent]):\n    pic_content = ...\n    msg_builder = MessageFactory([\n        Image(pic_content), Text("这是你要的图片")\n    ])\n    # or msg_builder = Image(pic_content) + Text("这是你要的图片")\n    await msg_builder.send()\n    await pic_matcher.finish()\n```\n\n## 类似项目\n\n- [nonebot-plugin-all4one](https://github.com/nonepkg/nonebot-plugin-all4one) 解决了类似的问题，但是用了不同路径\n- [nonebot-plugin-params](https://github.com/iyume/nonebot-plugin-params) 通过 Rule 定制订阅的平台，与本插件联合使用也许会有奇效\n\n## License\n\nMIT\n',
    'author': 'felinae98',
    'author_email': '731499577@qq.com',
    'maintainer': 'None',
    'maintainer_email': 'None',
    'url': 'None',
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
