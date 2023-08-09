# from DataRecorder import Recorder
#
# r = Recorder('data.csv')  # 创建对象
# r.add_data('abc')  # 添加数据
# r.record()  # 记录数据

# from DataRecorder import Recorder
#
# r = Recorder('data.csv')
# r.add_data(((1, 2), (3, 4)))  # 用二维数据一次添加多行
# r.add_data('abc')  # 添加单行数据
# r.record()  # 记录数据

# from DataRecorder import Filler
#
# f = Filler('data.xlsx')
# f.add_data((1, 2, 3, 4), 'a2')  # 从A2单元格开始，写入一行数据
# f.add_data(((1, 2), (3, 4)), 'd4')  # 以D4单元格为左上角，写入一片二维数据
# f.record()

from DataRecorder import Recorder


class Rd(Recorder):
    def cache_head_true(self, data):
        global __default_head__
        __default_head__ = tuple(list(__default_head__) + list(data.keys()))
        __default_head__ = tuple(list(dict.fromkeys(__default_head__).keys()))
        return __default_head__

    def cache_head_false(self):
        return __default_head__

    def add_dict_data(self, data, mode=False):
        """
        自动根据表头把数据存储到对应列

        mode = True
        依据数据动态更新表头，允许存在缺失值
        mode = False
        固定表头，不会保存表头字段之外的数据
        :param default_head: 设置默认表头
        :param data: 字典数据
        :return:
        """
        head = self.cache_head_true(data) if mode else self.cache_head_false()
        r.set.head(head)
        init_head = dict.fromkeys(head, None)
        data = {**init_head, **data} if mode else {key: data.get(key, init_head[key]) for key in init_head}
        self.add_data(data)


open('data1.csv', 'w', encoding='utf-8-sig')  # 这个不会自动创建文件，补了行这个
r = Rd('data1.csv')
data = {
    '姓名': 'jay',
    '性别': '女',
    '学历': '本科',
    '评分': 9.7,
    '身高': 1.9,
    'll': 0,
    '年龄': 111
}
data2 = {
    '状态': '良好'
}
data3 = data
# 必须全局参数，固定变量名，缓存默认表头
__default_head__ = ('姓名', '性别', '年龄', '学历', '身高', '状态')
r.add_dict_data(data, mode=False)  # 默认模式是False，可以不传参数
r.add_dict_data(data2, mode=False)
# 执行代码后从演示中可以看到，
# 表头顺序只与__default_head__配置有关，与数据无关
# 允许缺失值，key-value模式

# r.add_dict_data(data3, mode=True)
# True模式下会根据dict_data对default_head进行修改，因此表头会动态更新
# 默认设置： ('姓名', '性别', '年龄', '学历', '身高', '状态')
# True模式下： ('姓名', '性别', '年龄', '学历', '身高', '状态', '评分', 'll')
# print('默认设置：',__default_head__)
# print('True模式下：', __default_head__)
r.record()
