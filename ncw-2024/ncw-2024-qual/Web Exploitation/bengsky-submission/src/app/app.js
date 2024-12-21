const express = require('express');
const app = express();
const cookieParser = require('cookie-parser');
const bodyParser = require('body-parser');
const nunjucks = require('nunjucks');
const path = require('path');

app.use((req, res, next) => {
    res.setHeader('Content-Security-Policy', `default-src *; script-src 'self' *; style-src 'self' *; img-src *; object-src 'none';`);
    next();
});

app.use('/static', express.static(path.join(__dirname, 'static')));

nunjucks.configure('views', {
    autoescape: true,
    express: app
});

app.use(cookieParser());
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: true }));

const userRouter = require('./routes/routes');
app.use('/', userRouter);

const PORT = 3000;
app.listen(PORT, () => {
    console.log(`Server running on port ${PORT}`);
});