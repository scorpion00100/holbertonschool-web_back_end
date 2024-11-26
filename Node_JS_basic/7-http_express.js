const express = require('express');
const countStudents = require('./3-read_file_async');
const DebugHolberton = require('./debug');

const app = express();
const port = 1245;

const d = new DebugHolberton();
d.fetch();

app.get('/', (req, res) => {
  res.send('Hello Holberton School!');
});
app.get('/students', async (req, res) => {
  try {
    const result = await countStudents(process.argv[2]);
    res.send(`This is the list of our students\n${result}`);
    res.status(200);
  } catch (err) {
    res.send('This is the list of our students\nCannot load the database');
    res.status(200);
  }
});

app.listen(port, () => {
  console.log(`Example app listening on port ${port}`);
});

module.exports = app;
