# 进度条模块
import os
import time
import requests

'''

'''
def progressbar(url, filename, parentpath='', redownload=False):
    if parentpath:
        if not os.path.exists(parentpath):  # 看是否有该文件夹，没有则创建文件夹
            os.mkdir(parentpath)
    filepath = parentpath + ('' if (not parentpath) or (parentpath.endswith('\\') or parentpath.endswith(
        '/')) else '\\') + filename  # 设置图片name，注：必须加上扩展名
    if not redownload:
        if os.path.exists(filepath):
            print(f' Download {filename} completed! exist,ignore')
            return

    start = time.time()  # 下载开始时间
    response = requests.get(url, stream=True)  # stream=True必须写上
    size = 0  # 初始化已下载大小
    chunk_size = 1024  # 每次下载的数据大小
    content_size = int(response.headers['content-length'])  # 下载文件总大小
    try:
        if response.status_code == 200:  # 判断是否响应成功
            print('Start download,[File size]:{size:.2f} MB'.format(
                size=content_size / chunk_size / 1024))  # 开始下载，显示下载文件大小

            with open(filepath, 'wb') as file:  # 显示进度条
                for data in response.iter_content(chunk_size=chunk_size):
                    file.write(data)
                    size += len(data)
                    print('\r' + '[下载进度]:%s%.2f%%' % (
                        '>' * int(size * 50 / content_size), float(size / content_size * 100)), end=' ')
        end = time.time()  # 下载结束时间
        print(f'Download {filename} completed!,times: %.2f秒' % (end - start))  # 输出下载用时时间
    except Exception as e:
        raise Exception(f"error download:{str(e)}")
