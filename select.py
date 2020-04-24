import csv
import os


def save_data(filename, data):
    if os.path.isfile(filename):
        is_exist = True
    else:
        is_exist = False
    with open(filename, "a", newline="", encoding="utf_8_sig") as f:
        c = csv.writer(f)
        if not is_exist:
            """need = [user_id, user_name, created_at, source,
                    content, reposts_count, comments_count, attitudes_count,
                    pics_url, video_url, retweeted_status, retweeted_url,
                    topic_num, topics]"""
            c.writerow(['用户id', '昵称', '发表时间', '发布设备', 'scheme_url', '正文', '转发数', '评论数', '点赞数',
                        '图片链接', '视频链接', '是否转发', '转发链接', '话题数', '话题', '微博链接'])
        for line in data:
            c.writerow(line)


def read_csv():
    with open('因雀思听.csv', 'r', encoding="utf_8_sig") as f:
        next(f)
        reader = csv.reader(f)
        for row in reader:
            print(row)
            break
            # if '故宫' in row[5]:
            #     print(row)
            #     save_data(filename='汇总---故宫', data=[row])


if __name__ == '__main__':
    read_csv()
