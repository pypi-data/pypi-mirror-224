import requests

"""
欢迎使用windpower_upc
简要介绍一下参数
api_base_url:是固定的api接口:http://172.24.187.133:5446/windpowerapi
api_key:是发放给您的一个独有的密钥
fill:True->对0值和空缺值进行填充 False->不对0值和空缺值进行填充
deduplication:True->去除时间重复数据 False->不去除时间重复数据
outlier:True->对离群点检测并修正 False->不处理离群点
normal:True->数据归一化处理 False->不进行归一化
resample:True->进行重采样 False->不进行重采样
figure:True->保存图片 False->不保存图片
file:True->保存预测结果文件 False->不保存预测结果文件
train:True->使用您的数据集进行训练并预测 False->使用我们现有的模型进行预测
ai:Ture->AI结果分析 False->不分析
"""


class windpowerapi:
    def __init__(self, api_base_url, api_key):
        self.api_base_url = api_base_url
        self.api_key = api_key


    def savepredictfile(self, csv_file, figure=False, file=False, train=False):
        # """
        # csv_file是您要进行预测的文件的地址
        # """
        figure = str(figure)
        file = str(file)
        train = str(train)
        url = self.api_base_url + 'savepredictfile'
        # 增加身份验证头部
        headers = {
            'Authorization': self.api_key,
            'figure': figure,
            'file': file,
            'train': train,
        }
        files = {'file': open(csv_file, 'rb')}
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
            print('预测文件保存成功~')
            if file == 'True' and figure == 'False':
                with open('predictions.csv', 'wb') as resfile:
                    resfile.write(response.content)
            elif file == 'False' and figure == 'True':
                with open('res_picture.png', 'wb') as resfile:
                    resfile.write(response.content)
            else:
                with open('res.zip', 'wb') as resfile:
                    resfile.write(response.content)

    def processingdata(self, csv_file, fill=False, outlier=False, normal=False, resample=False, deduplication=False):
        fill = str(fill)
        outlier = str(outlier)
        normal = str(normal)
        resample = str(resample)
        deduplication = str(deduplication)
        url = self.api_base_url + 'processingdata'
        # 增加身份验证头部
        headers = {
            'Authorization': self.api_key,
            'fill': fill,
            'outlier': outlier,
            'normal': normal,
            'resample': resample,
            'deduplication': deduplication,
        }
        files = {'file': open(csv_file, 'rb')}
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
            print('数据处理结果文件保存成功~')
            with open('processed_dataset.csv', 'wb') as resfile:
                resfile.write(response.content)

    def aianalysis(self, csv_file, ai=True):
        print('AI分析中...')
        ai = str(ai)
        url = self.api_base_url + 'aianalysis'
        headers = {
            'Authorization': self.api_key,
            'ai': ai
        }
        files = {'file': open(csv_file, 'rb')}
        response = requests.post(url, files=files, headers=headers)
        if response.status_code == 200:
            ans = response.json()
            ans = ans['ans']
            ans = 'AI分析结果:' + ans
            new_ans = ""
            for i in range(len(ans)):
                if ans[i] != "\n":
                    new_ans = new_ans + ans[i]
            for i in range(len(new_ans)):
                print(new_ans[i],end='')
                if i % 100 == 0 and i != 0:
                    print()

