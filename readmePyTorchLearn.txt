一、安装PyTorch（参考官网https://pytorch.org/）:pip3 install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu117

二、将python项目部署到docker（参考http://www.manongjc.com/detail/29-kkcifkeroaiirao.html）
1、requirements.txt生成方法：cmd命令，进入到【D:\python\EF_NFCS】目录，也就是工程目录，package的同级目录，执行命令：pip freeze > requirements.txt，就在该目录下生成了一个requirements.txt文件：
2、

三、python学习
1、第一个示例程序：https://www.w3cschool.cn/pytorch/pytorch-5ubt3bby.html，运行通过202308171453

四、gitHub提交步骤
1、项目根目录依次输入命令 git init / git add / git commit -m "说明注释、自己写"
2、在GitHub上建和本地项目同名的仓库
3、在vscode源代码管理中点击“发布Branch”,完成代码发布
4、如果报错“failed to connect to github port 443 after 21040”，请设置vscode全局翻墙代理，如下：
git config --global http.proxy socks5 127.0.0.1:9909
git config --global https.proxy socks5 127.0.0.1:9909
git config --global http.proxy 127.0.0.1:9910
git config --global https.proxy 127.0.0.1:9910

五、commit一直等待，请在设置-拓展-GIT:use Editor As commit input的勾选去掉即可解决.https://blog.csdn.net/qq_42632840/article/details/134581517
