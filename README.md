# YouTube 野生字幕组

为中文 YouTuber 提供英文字幕的志愿字幕组。

联络方式：
- [Issues](https://github.com/immoonancient/YTSubtitles/issues) 仅限正式工作
- [微信群](docs/wechat.md) 灌水吐槽混脸熟打酱油皆可

## GitHub 使用教程

不熟悉 GitHub 的同学可参考 [GitHub 简易教程](tutorial/README.md)。

## 工作流程

每期视频的字幕制作分为以下阶段：
1. **通知**：[新建一个 issue](https://github.com/immoonancient/YTSubtitles/issues/new)，标题格式为 "\[频道名称\]视频名称 - 链接"，例如 "\[美食作家王刚\]川式炒猪肝 - https://youtu.be/xaLMdLEGZKQ"
2. **认领**：一位热心的同学（下称“同学 A”）在 issue 中留言认领该视频的字幕工作。有权限的同学看到后请将该 issue assign 给同学 A
3. **翻译**：同学 A 撰写该视频的中英文字幕对照翻译稿并提交 pull requst (PR)
   - 翻译稿及 pull request 具体要求请参考[翻译细则](docs/translation.md)
   - 如果同学 A 不熟悉 GitHub 可以在 issue 或微信群留言并附上翻译稿，请其他同学代为提交 PR
4. **校对**：按照 GitHub 的 review 流程进行，校对完毕后 merge PR
5. **上传**：同学 A 在 YouTube 按照审核后的翻译稿添加字幕，具体方法参考 [YouTube 帮助](https://support.google.com/youtube/answer/6054623)
   - 若条件允许，请同学 A 尽量[非匿名上传](https://support.google.com/youtube/answer/6392394)
6. **发布**：同学 A 在 issue 或微信群通知其他同学去 YouTube 审核通过该字幕以便其尽早发布。字幕发布后关闭 issue
7. **广告**：字幕发布后，同学 A 可在视频留言推广本字幕组。[留言模版](docs/promotion.md)

## 校对组

英语好且愿意进行更多校对工作的同学请发 issue 加入[校对组](subtitles/CODEOWNERS)。

## 许可

本项目采用知识共享署名-非商业性使用-相同方式共享 4.0 国际许可协议进行许可。
