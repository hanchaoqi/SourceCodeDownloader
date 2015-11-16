# SourceCodeDownloader
>一个下载器，从一些软件的官方网站下载源代码

###使用方法：
将软件版本号按行写入以软件名命名的txt文件中，使用命令: python downloader.py yoursoftwareName

###支持的软件：
- chrome
    - 下载地址：https://chromium.googlesource.com/chromium/src.git/+refs
    - 支持所有版本
- linux_kernel
    - 下载地址：https://www.kernel.org/pub/linux/kernel/
    - 支持所有版本
- firefox
    - 下载地址： http://ftp.mozilla.org/pub/mozilla.org/firefox/releases/
    - 支持除以lastest开头的所有版本