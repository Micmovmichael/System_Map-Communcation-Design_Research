const express = require('express');
const fs = require('fs');
const app = express();
const port = 3000;


// 设置CORS头部
app.use((req, res, next) => {
    res.setHeader('Access-Control-Allow-Origin', 'http://10.20.99.214:8000'); // 允许的域名
    res.setHeader('Access-Control-Allow-Methods', 'GET, POST, PUT, DELETE'); // 允许的HTTP方法
    res.setHeader('Access-Control-Allow-Headers', 'Content-Type'); // 允许的请求头
    next();
});

app.use(express.json());

// 路由，用于处理保存数据的请求
// 路由，用于处理保存数据的请求
// 路由，用于处理保存数据的请求
// 路由，用于处理保存数据的请求
// 路由，用于处理保存数据的请求

app.post('/saveData', (req, res) => {
    // 接收从前端发送过来的数据
    const newData = req.body;

    // 读取原始的JSON文件数据
    fs.readFile('data.json', 'utf8', (err, data) => {
        if (err) {
            console.error(err);
            res.status(500).send('Error reading file');
            return;
        }

        // 解析原始数据
        let jsonData = JSON.parse(data);

        // 更新原始数据
        // 这里可以根据具体的需求，根据前端发送过来的数据进行更新操作
        // 这里简单地合并新旧数据，你可能需要根据实际情况进行更复杂的更新操作
        Object.assign(jsonData, newData);

        // 将更新后的数据写回JSON文件
        fs.writeFile('data.json', JSON.stringify(jsonData, null, 2), 'utf8', (err) => {
            if (err) {
                console.error(err);
                res.status(500).send('Error writing file');
                return;
            }
            console.log('Data saved:', JSON.stringify(jsonData, null, 2));
            res.status(200).send('Data saved successfully');
        });
    });
});

// 启动服务器
app.listen(port, '10.20.99.214', () => {
    console.log(`Server listening at http://10.20.99.214:${port}`);
});

