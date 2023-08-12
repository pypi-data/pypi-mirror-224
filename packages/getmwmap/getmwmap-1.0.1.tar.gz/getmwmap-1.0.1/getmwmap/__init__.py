import random


def getMap(num: int,limit:list) -> list:

    # mapL为全部地图list
    mapL = ['绿地', '风暴', '未开发岩石区', '北极圈', '失落之城', '冰岛', '维京湾', '岩峰']

    # maps为随机获得的地图list
    maps = []

    # 判断num值是否大于13
    if int(num) > 13:

        # 返回-1
        return -1

    else:

        # 判断limit是否为空
        if limit == []:
            pass

        else:

            # 删除limit禁用的地图
            for i in limit:
                if i in mapL:
                    mapL.remove(i)

        # 如果经过禁用后的地图数量大于随机次数，地图将不会重复
        if len(mapL) > num:
            for i in range(0, num):
                # 随机获取mapL中的地图
                rd = random.choice(mapL)

                # 将随机结果传入maps
                maps.append(rd)

                # 删除已经出现的地图，避免重复
                mapL.remove(rd)

                # 打乱地图顺序
                random.shuffle(mapL)

            # 返回maps
            return maps
        else:

            for i in range(0,num):

                # 将随机结果传入maps
                maps.append(random.choice(mapL))

                # 打乱地图顺序
                random.shuffle(mapL)

            # 返回maps
            return maps