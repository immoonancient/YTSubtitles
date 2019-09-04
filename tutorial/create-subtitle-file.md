# 制作中英对照字幕文件

## 制作步骤

1. 使用 YouTube 的字幕添加功能制作英文字幕。可参考[官方帮助](https://support.google.com/youtube/answer/6054623)或[视频教程](https://youtu.be/_3MMKHqoZrs)
2. 英文字幕制作好后，下载字幕文件，如下图所示<br><img src="resources/download-subtitles.png" width="400px">
3. 在字幕文件中加入用于审核的其他信息，包括视频链接、每行英文字幕的中文对照，乃至视频的标题描述（如果视频有提供的话），甚至可以以此注明自己某处没看懂或者译法不确定等等。原则上可以加入任何对审核有帮助的信息。
   - 上述信息都应当以 `#` 开头以标示
   - 成品范例可参考 [/subtitles/wang-gang/20190826-shao-zhu-shu.sbv](/subtitles/wang-gang/20190826-shao-zhu-shu.sbv)
   - 如果不知道如何直接编辑字幕文件，也可以先跳过这一步，等到[上传完 pull request](upload-subtitle-pr.md) 之后再以[修改稿件](Commit-change.md)的形式加入这些信息

## 附注

如果觉得制作字幕文件麻烦，可以简单制作一份不带时间轴的中英对照翻译稿（[范例](/subtitles/wang-gang/20190825-ma-feng-wo)）。然而不推荐此法，因为定稿后依然需要在 YouTube 花时间添加时间轴，总体而言工作量并没有减少，反而流程更为琐碎。
