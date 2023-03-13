var http = require('http');


http.createServer(function (req, res) {
    console.log(req.method, req.headers, req.body);

    let body = '';

    if (req.method == "POST"){

        req.on('data', (chunk) => {
            body += chunk;
        });


        req.on('end', () => {

            let sysarg = body;
            const spawn = require("child_process").spawn;
            const pythonProcess = spawn('python', ["fourpartresponse.py", sysarg]);

            pythonProcess.stdout.on('data', (data) => {
                res.write(data);
                res.end()
            });

        });
    }
//    res.writeHead(200, {'Content-Type': 'text/html'});
//
//
//    res.end('Hello World!');
}).listen(8080);







console.log("Server Running on Port: 8000");
