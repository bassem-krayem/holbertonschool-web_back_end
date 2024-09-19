// creating server part 8.5
const express = require('express');
const indexRouter = require('./routes/index');

const app = express();
const PORT = 1245;

app.use('/', indexRouter);
app.use('/students', indexRouter);
app.use('/students/:major', indexRouter);

app.listen(PORT, () => {
});

module.exports = app;
