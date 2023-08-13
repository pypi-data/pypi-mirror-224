import requests

"""
欢迎使用windpower_upc
简要介绍一下参数
api_base_url:是固定的api接口:http://172.24.187.133:5446/longyuanapi
api_key:是发放给您的一个独有的密钥
fill:True->对0值和空缺值进行填充->False不填充
outlier:True->对离群点检测并修正->不处理离群点
normal:True->数据归一化处理->不进行归一化
resample:True->进行重采样->不进行重采样
figure:True->保存图片 False->不保存图片
file:True->保存预测结果文件 False->不保存预测结果文件
train:True->使用您的数据集进行训练并预测False->使用我们现有的模型进行预测
ai:Ture->AI结果分析->不分析
"""


class windpowerapi:
    def __init__(self, api_base_url, api_key, fill, outlier, normal, resample, figure, file, train, ai):
        self.api_base_url = api_base_url
        self.api_key = api_key
        self.fill = str(fill)
        self.outlier = str(outlier)
        self.normal = str(normal)
        self.resample = str(resample)
        self.figure = str(figure)
        self.file = str(file)
        self.train = str(train)
        self.ai = str(ai)

    def savepredictfile(self, csv_file):
        # """
        # csv_file是您要进行预测的文件的地址
        # """
        url = self.api_base_url
        # 增加身份验证头部
        headers = {
            'Authorization': self.api_key,
            'show': self.show,
            'output': self.output,
            'train': self.train,
        }
        files = {'file': open(csv_file, 'rb')}
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
            if self.output == 'True' and self.show == 'False':
                with open('predictions.csv', 'wb') as file:
                    file.write(response.content)
            elif self.output == 'False' and self.show == 'True':
                with open('res_picture.png', 'wb') as file:
                    file.write(response.content)
            else:
                with open('res.zip', 'wb') as file:
                    file.write(response.content)
